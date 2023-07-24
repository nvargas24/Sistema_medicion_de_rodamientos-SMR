from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time
import numpy as np
import os

import paho.mqtt.client as mqtt
from peewee import *

NUM_ENSAYOS = 2

class Mqtt:
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

        self.mcp_ant = False
        self.mag_mcp_ant = False
        self.freq_mcp_ant = False
        self.temp_obj_ant = 0.0
        self.acel_axial_ant = 0.0
        self.acel_radial_ant = 0.0

        self.mcp_pos = False
        self.mag_mcp_pos = False
        self.freq_mcp_pos = False
        self.temp_obj_pos = 0.0
        self.acel_axial_pos = 0.0
        self.acel_radial_pos = 0.0


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conexión exitosa al broker")
        else:
            print(f"No se pudo conectar al broker. Código de retorno: {rc}")

    def start(self):
        try:
            self.client.on_connect = self.on_connect
            self.client.connect(self.broker_host, self.broker_port)
            self.client.loop_start()
        except ConnectionError as err:
            print(f"No se pudo conectar. ERROR: {str(err)}")
    
    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

    def send(self, topic, message):
        self.client.publish(topic, message)

    def on_message(self, client, userdata, msg):
        print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
        self.topic = msg.topic
        self.msg = msg.payload.decode()
        self.qualify_data_bytopic()

    def suscrip(self, topic):
        self.client.subscribe(topic)
        self.client.on_message = self.on_message 

    def desuscrip(self, topic):
        self.client.unsubscribe(topic)

    def qualify_data_bytopic(self):
        # Verifico si hay datos recibidos por broker y doy formato
        if self.topic == "rodAnt/tempObj":
            self.temp_obj_ant = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelAxial":
            self.acel_axial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelRadial":
            self.acel_radial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/mcp":
            self.mcp_ant = self.msg
        if self.topic == "rodAnt/mcpMag":
            self.mag_mcp_ant = self.msg
        if self.topic == "rodAnt/mcpFreq":
            self.freq_mcp_ant = self.msg

        if self.topic == "rodPos/tempObj":
            self.temp_obj_pos = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelAxial":
            self.acel_axial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelRadial":
            self.acel_radial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/mcp":
            self.mcp_pos = self.msg
        if self.topic == "rodPos/mcpMag":
            self.mag_mcp_pos = self.msg
        if self.topic == "rodPos/mcpFreq":
            self.freq_mcp_pos = self.msg

    def suscrip_topics(self):
        self.suscrip("rodAnt/tempObj")
        self.suscrip("rodAnt/acelAxial")
        self.suscrip("rodAnt/acelRadial")
        self.suscrip("rodAnt/mcp")
        self.suscrip("rodAnt/mcpMag")

        self.suscrip("rodPos/tempObj")
        self.suscrip("rodPos/acelAxial")
        self.suscrip("rodPos/acelRadial")
        self.suscrip("rodPos/mcp")
        self.suscrip("rodPos/mcpMag")

    def desuscrip_topics(self):
        self.desuscrip("rodAnt/tempObj")
        self.desuscrip("rodAnt/acelAxial")
        self.desuscrip("rodAnt/acelRadial")
        self.desuscrip("rodAnt/mcp")
        self.desuscrip("rodAnt/mcpMag")

        self.desuscrip("rodPos/tempObj")
        self.desuscrip("rodPos/acelAxial")
        self.desuscrip("rodPos/acelRadial")
        self.desuscrip("rodPos/mcp")
        self.desuscrip("rodPos/mcpMag")

class Measure():
    
    def __init__(self, widgets):
        super().__init__()
        # Atributo para acceder a los widgets
        self.widgets = widgets
        
        self.mqtt_obj = Mqtt("192.168.51.203", 1883)
        #self.mqtt_obj = Mqtt("192.168.1.103", 1883)
        #self.mqtt_obj = Mqtt("192.168.68.203", 1883)
        #self.mqtt_obj = Mqtt("192.168.149.203", 1883)
        #self.mqtt_obj.start()
        #self.mqtt_obj.suscrip("rodAnt/keepalive")
        self.num_temporal = 1
        self.cont_ensayos = 1
        self.samples = np.arange(0, 1024, 1)
        #self.reset_widgets()
        self.widgets_config()

    def init_conf(self):
        """
        Modo configuracion - Usuario debe ingresar parametros de configuracion
        """
        self.widgets_config()
        #self.reset_widgets()    
        self.notificacion("Esperando configuracion")
        self.widgets.ui.progress_bar_programa.setValue(0)
        self.widgets.ui.progress_bar_ensayo.setValue(0)

    def init_ensayo(self):
        """
        Callback de boton 'Iniciar' - Obtiene parametros del ui y los envia por mqtt
        """
        # Inicio conexion mqtt
        self.mqtt_obj.start()
        # Obtengo tiempo de cada ensayo
        self.selected_time = self.widgets.ui.time_ensayo.time()
        self.minutes = self.selected_time.minute()
        self.seconds = self.selected_time.second()

        # Obtengo tiempo total en segundos
        self.seconds_total = (self.minutes * 60 + self.seconds)
        self.seconds_total_aux = self.seconds_total

        # Obtengo tiempo de intervalo entre ensayo
        self.seconds_standby = self.widgets.ui.time_standby.time().second()
        self.seconds_standby_aux = self.seconds_standby
        
        print("Configuracion realizada")
        print("Tiempo de ensayo:"+ str(self.seconds_total)+ "seg")
        print("Tiempo de intervalo:"+ str(self.seconds_standby)+ "seg")

        # Asigno rango dinamico a progressbar
        self.widgets.ui.progress_bar_ensayo.setRange(0, int(self.seconds_total))
        self.widgets.ui.progress_bar_programa.setRange(0, NUM_ENSAYOS)

        # Enviar por mqtt los datos de configuracion
        self.mqtt_obj.send("smr/start", True)

        # Des/habilito widget para modo ensayo
        self.widgets_ensayo()
        self.mqtt_obj.suscrip_topics()
        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.widgets.timer1.start(1000)

    def forzar_finish_ensayo(self):
        """
        Fuerza finalizacion de ensayo actual y arranca el siguiente (si es que lo hay)
        """
        print("Finaliza ensayo "+ str(self.cont_ensayos) +" - Forzado")
        self.widgets.timer1.stop()

        # Seteo widget como si hubiese terminado ensayo
        #self.widgets.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        self.reset_widgets()
        self.widgets.ui.progress_bar_ensayo.setValue(int(self.seconds_total_aux))
        self.widgets.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
        
        # En el caso de que se cumplan los 5 ensayos pase a modo config
        if self.cont_ensayos == NUM_ENSAYOS:
            self.cont_ensayos = 1
            self.mqtt_obj.send("smr/stop", True)
            # Se vuelve a modo configuracion
            self.mqtt_obj.stop()
            self.init_conf()
        else:
            # Inicializo contador de modo stanby
            self.widgets.timer2.start(1000)
            self.seconds_total = self.seconds_total_aux
    
    def finish_test(self):
        print("Finalizo test")
        # Finalizo contadores
        self.widgets.timer1.stop()
        self.widgets.timer2.stop()
        self.reset_widgets()
        self.cont_ensayos = 1
        self.mqtt_obj.send("smr/stop", True)
        # Se vuelve a modo configuracion
        self.mqtt_obj.stop()
        self.init_conf()

    def save_image(self):
        """
        Metodo para capturar grafico temporal en tiempo real
        """
        name_temporal_ant = os.path.join("capture", f"Temporal_ant_{self.num_temporal}.tiff")
        name_temporal_pos = os.path.join("capture", f"Temporal_pos_{self.num_temporal}.tiff")

        self.widgets.grafica.fig.savefig(name_temporal_ant)
        self.widgets.grafica2.fig.savefig(name_temporal_pos)

        self.num_temporal += self.num_temporal

    def widgets_config(self):
        """
        Des/habilita widgets en modo configuracion
        """
        self.widgets.ui.time_ensayo.setEnabled(True)
        self.widgets.ui.time_standby.setEnabled(True)

        self.widgets.ui.btn_finish.setEnabled(False)
        self.widgets.ui.btn_init.setEnabled(True)
        
        self.widgets.ui.led_ant.setEnabled(False)
        self.widgets.ui.led_pos.setEnabled(False)
        self.widgets.ui.lcd_time_ensayo.setEnabled(False)
        self.widgets.ui.progress_bar_ensayo.setEnabled(False)
        self.widgets.ui.btn_forzar.setEnabled(False)

        self.widgets.ui.lcd_temp_ant.setEnabled(False)
        self.widgets.ui.lcd_axial_ant.setEnabled(False)
        self.widgets.ui.lcd_radial_ant.setEnabled(False)
        self.widgets.ui.lcd_temp_pos.setEnabled(False)
        self.widgets.ui.lcd_axial_pos.setEnabled(False)
        self.widgets.ui.lcd_radial_pos.setEnabled(False)

    def widgets_ensayo(self):
        """
        Des/habilita widgets en modo ensayo
        """
        self.widgets.ui.time_ensayo.setEnabled(False)
        self.widgets.ui.time_standby.setEnabled(False)

        self.widgets.ui.btn_finish.setEnabled(True)
        self.widgets.ui.btn_init.setEnabled(False)

        self.widgets.ui.led_ant.setEnabled(True)
        self.widgets.ui.led_pos.setEnabled(True)
        self.widgets.ui.lcd_time_ensayo.setEnabled(True)
        self.widgets.ui.progress_bar_ensayo.setEnabled(True)
        self.widgets.ui.btn_forzar.setEnabled(True)

        self.widgets.ui.lcd_temp_ant.setEnabled(True)
        self.widgets.ui.lcd_axial_ant.setEnabled(True)
        self.widgets.ui.lcd_radial_ant.setEnabled(True)
        self.widgets.ui.lcd_temp_pos.setEnabled(True)
        self.widgets.ui.lcd_axial_pos.setEnabled(True)
        self.widgets.ui.lcd_radial_pos.setEnabled(True)

    def timer_ensayo(self, ):
        """
        Timer de Modo ensayo - tiempo de contador asignado por usuario
        """
        self.notificacion("Ensayo "+ str(self.cont_ensayos) + " en proceso")
        # Se obtiene minutos y segundos a mostrar en lcd
        self.minutes = self.seconds_total//60
        self.seconds = self.seconds_total%60
        self.widgets.ui.lcd_time_ensayo.display(f"{self.minutes:02d}:{self.seconds:02d}")
        # Cargo valor a progressbar, segun avance el contador
        self.widgets.ui.progress_bar_ensayo.setValue(int(self.seconds_total_aux)-int(self.seconds_total))
        # Cada vez que se cumpla un 1 seg resto un valor del total de segundos
        self.seconds_total = self.seconds_total-1
        # Se verifica si el dispositivo publico algo en un topic
        self.data_recive()
        # Se detiene contador para que no siga con parte negativa
        if self.seconds_total<0 : 
            self.widgets.timer1.stop()
            # Cargo valor a progressbar cada vez que finaliza un ensayo
            self.widgets.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
            self.reset_widgets()
            self.mqtt_obj.desuscrip_topics()
            # Se vertfica si ya se cumplio el total de ensayos o no
            if self.cont_ensayos == NUM_ENSAYOS:            
                print("Ya se realizaron %d ensayos" %NUM_ENSAYOS)
                self.cont_ensayos = 1
                self.mqtt_obj.send("smr/stop", True)
                # Se vuelve a modo configuracion
                self.mqtt_obj.stop()
                self.init_conf()
            else:
                # Inicializo contador de modo stanby
                self.widgets.timer2.start(1000)
                self.seconds_total = self.seconds_total_aux

    def timer_standby(self):
        """
        Timer de Modo standby - tiempo de contador asignado por usuario
        """
        self.notificacion("Nuevo ensayo en "+ str(self.seconds_standby))
        self.seconds_standby = self.seconds_standby-1
        # Se detiene contador para que no siga con parte negativa
        if self.seconds_standby<0 : 
            self.widgets.timer2.stop()
            self.mqtt_obj.suscrip_topics()
            # Se inicia contador de nuevo ensayo
            self.widgets.timer1.start(1000)
            self.seconds_standby = self.seconds_standby_aux
            self.cont_ensayos = self.cont_ensayos +1
    
    def notificacion(self, msj):
        """
        Informa eventos
        """        
        self.widgets.ui.notificacion.setText(str(msj))
    
    def reset_widgets(self):
        """
        Reseteo estado de widgets
        """
        self.widgets.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")

        self.widgets.ui.lcd_temp_ant.display(f"{0:02d}.{0:02d}")
        self.widgets.ui.lcd_axial_ant.display(f"{0:02d}.{0:02d}")
        self.widgets.ui.lcd_radial_ant.display(f"{0:02d}.{0:02d}")

        self.widgets.ui.lcd_temp_pos.display(f"{0:02d}.{0:02d}")
        self.widgets.ui.lcd_axial_pos.display(f"{0:02d}.{0:02d}")
        self.widgets.ui.lcd_radial_pos.display(f"{0:02d}.{0:02d}")

        #   MODIFICAR PARAMETROS  A PASAR PARA GRAFICO TEMPORAL
        self.widgets.grafica.ax.clear()
        self.widgets.grafica.ax.set_title("Rodamiento anterior")
        self.widgets.grafica.upgrade_graph(self.samples, np.zeros(1024))

        self.widgets.grafica2.ax.clear()
        self.widgets.grafica2.ax.set_title("Rodamiento posterior")
        self.widgets.grafica2.upgrade_graph(self.samples, np.zeros(1024))

    def data_recive(self):
        """
        Muestra lecturas obtenidas de sensores en display
        """
        # Muestro datos recibidos en ui - rodamiento anterior
        if self.mqtt_obj.temp_obj_ant:
            self.widgets.ui.lcd_temp_ant.display(self.mqtt_obj.temp_obj_ant)
        if self.mqtt_obj.acel_axial_ant:
            self.widgets.ui.lcd_axial_ant.display(self.mqtt_obj.acel_axial_ant)
        if self.mqtt_obj.acel_radial_ant:
            self.widgets.ui.lcd_radial_ant.display(self.mqtt_obj.acel_radial_ant)
        if self.mqtt_obj.mag_mcp_ant:
            self.widgets.ui.mag_ant.setText("   Mag:"+str(self.mqtt_obj.mag_mcp_ant)+"    Freq: "+str(self.mqtt_obj.freq_mcp_ant))
        if self.mqtt_obj.mcp_ant:
            # paso de str a una lista numpy
            self.mcp_ant = np.fromstring(self.mqtt_obj.mcp_ant, dtype=float, sep=',')  # Convertir la cadena en una lista de NumPy
            self.widgets.grafica.ax.clear()
            self.widgets.grafica.ax.set_title("Rodamiento anterior")
            #   MODIFICAR PARAMETROS  A PASAR PARA GRAFICO TEMPORAL
            self.widgets.grafica.upgrade_graph(self.samples, self.mcp_ant)
        
        # Muestro datos recibidos en ui - rodamiento posterior
        if self.mqtt_obj.temp_obj_pos:
            self.widgets.ui.lcd_temp_pos.display(self.mqtt_obj.temp_obj_pos)
        if self.mqtt_obj.acel_axial_pos:
            self.widgets.ui.lcd_axial_pos.display(self.mqtt_obj.acel_axial_pos)
        if self.mqtt_obj.acel_radial_pos:
            self.widgets.ui.lcd_radial_pos.display(self.mqtt_obj.acel_radial_pos)
        if self.mqtt_obj.mag_mcp_pos:
            self.widgets.ui.mag_pos.setText("   Mag:"+str(self.mqtt_obj.mag_mcp_pos)+"    Freq: "+str(self.mqtt_obj.freq_mcp_pos))
        if self.mqtt_obj.mcp_pos:
            # paso de str a una lista numpy
            self.mcp_pos = np.fromstring(self.mqtt_obj.mcp_pos, dtype=float, sep=',')  # Convertir la cadena en una lista de NumPy
            self.widgets.grafica2.ax.clear()
            self.widgets.grafica2.ax.set_title("Rodamiento posterior")
            #   MODIFICAR PARAMETROS  A PASAR PARA GRAFICO TEMPORAL
            self.widgets.grafica2.upgrade_graph(self.samples, self.mcp_pos)

        # Reseteo buffer para topic y msg
        self.mqtt_obj.topic = None
        self.mqtt_obj.msg = None        