from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time
import numpy as np

import paho.mqtt.client as mqtt
from peewee import *

NUM_ENSAYOS = 2

# ---------------------Clases que contienen métodos para base de datos--------------------------------
try:
    db = SqliteDatabase(
        "registro_eventos.db"
    )  # Creo el objeto que indica el tipo y nombre de bd a la cual me voy a conectar (si no existe la crea).
except:
    print("No se pudo crear la base de datos")

class BaseModel(Model):
    """
    Clase que establece a que base de datos me conecto y su tipo.
    """

    class Meta:
        database = db  # Indico a que base me conecto y su tipo.

class RodAnterior(BaseModel):
    N_ensayo = IntegerField()
    Tiempo_de_ensayo = TimeField()
    #Tiempo_real = TimeField()
    BPFO = BooleanField()
    BPFI = BooleanField()
    FTF = BooleanField()
    BSF = BooleanField()
    Temp = FloatField()
    AcelAxial = FloatField()
    AcelRadial = FloatField()

class RodPosterior(BaseModel):
    N_ensayo = IntegerField()
    Tiempo_de_ensayo = TimeField()
    #Tiempo_real = TimeField()
    BPFO = BooleanField()
    BPFI = BooleanField()
    FTF = BooleanField()
    BSF = BooleanField()
    Temp = FloatField()
    AcelAxial = FloatField()
    AcelRadial = FloatField()

class BaseDatos:
    """
    Clase que contiene métodos para conectarme a la base de datos, y para manejar los registros de la misma.
    """

    def __init__(self):
        """
        Constructor para crear, conectarme, y agregar una tabla a la base de datos.
        """
        self.con = db
        self.con.connect()
        self.con.create_tables([RodAnterior()])
        self.con.create_tables([RodPosterior()])

    def agregar_db_ant(self, n_ensayo, time_ensayo, bpfo, bpfi, ftf, bsf, temp, acel_axial, acel_radial):

        reg = RodAnterior()

        time_ensayo_min = time_ensayo // 60
        time_ensayo_seg = time_ensayo % 60
        min_ensayo = str(time_ensayo_min).zfill(2)
        seg_ensayo = str(time_ensayo_seg).zfill(2)

        # Le asigno los valores ingresados a cada atributo(campo) del objeto.
        reg.N_ensayo = n_ensayo
        reg.Tiempo_de_ensayo = f"0:{min_ensayo}:{seg_ensayo}"
        #reg.Tiempo_real = time_real
        reg.BPFO = bpfo
        reg.BPFI = bpfi
        reg.FTF = ftf
        reg.BSF = bsf
        reg.Temp = temp
        reg.AcelAxial = acel_axial
        reg.AcelRadial = acel_radial

        try:
            reg.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

    def agregar_db_pos(self, n_ensayo, time_ensayo, bpfo, bpfi, ftf, bsf, temp, acel_axial, acel_radial):

        reg = RodPosterior()

        # Le asigno los valores ingresados a cada atributo(campo) del objeto.
        reg.N_ensayo = n_ensayo
        reg.Tiempo_de_ensayo = time_ensayo
        #reg.Tiempo_real = time_real
        reg.BPFO = bpfo
        reg.BPFI = bpfi
        reg.FTF = ftf
        reg.BSF = bsf
        reg.Temp = temp
        reg.AcelAxial = acel_axial
        reg.AcelRadial = acel_radial

        try:
            reg.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

class Mqtt:
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

        self.keepalive_ant = False
        self.temp_obj_ant = 0.0
        self.acel_axial_ant = 0.0
        self.acel_radial_ant = 0.0
        self.pres_bpfi_ant = False
        self.pres_bpfo_ant = False
        self.pres_bsf_ant = False
        self.pres_ftf_ant = False
        self.fft_ant = False
        self.temp_obj_pos = 0.0
        self.acel_axial_pos = 0.0
        self.acel_radial_pos = 0.0
        self.pres_bpfi_pos = False
        self.pres_bpfo_pos = False
        self.pres_bsf_pos = False
        self.pres_ftf_pos = False
        self.fft_pos = False

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
        if self.topic == "rodAnt/keepalive":
            self.keepalive_ant = True
        if self.topic == "rodAnt/tempObj":
            self.temp_obj_ant = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelAxial":
            self.acel_axial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelRadial":
            self.acel_radial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/presBPFO":
            self.pres_bpfo_ant = int(self.msg)
        if self.topic == "rodAnt/presBPFI":
            self.pres_bpfi_ant = int(self.msg)
        if self.topic == "rodAnt/presBSF":
            self.pres_bsf_ant = int(self.msg)
        if self.topic == "rodAnt/presFTF":
            self.pres_ftf_ant = int(self.msg)
        if self.topic == "rodAnt/fft":
            self.fft_ant = self.msg

        if self.topic == "rodPos/tempObj":
            self.temp_obj_pos = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelAxial":
            self.acel_axial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelRadial":
            self.acel_radial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/presBPFO":
            self.pres_bpfo_pos = self.msg
        if self.topic == "rodPos/presBPFI":
            self.pres_bpfi_pos = self.msg
        if self.topic == "rodPos/presBSF":
            self.pres_bsf_pos = self.msg
        if self.topic == "rodPos/presFTF":
            self.pres_ftf_pos = self.msg
        if self.topic == "rodPos/fft":
            self.fft_pos = self.msg

class Measure(BaseDatos):
    
    def __init__(self, widgets):
        super().__init__()
        # Atributo para acceder a los widgets
        self.widgets = widgets
        
        #self.mqtt_obj = Mqtt("192.168.68.168", 1883)
        self.mqtt_obj = Mqtt("192.168.1.103", 1883)
        #self.mqtt_obj = Mqtt("192.168.68.203", 1883)
        #self.mqtt_obj.start()
        #self.mqtt_obj.suscrip("rodAnt/keepalive")

        self.cont_ensayos = 1
        self.freq = np.arange(0, 512*37, 37)
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
        
        # Obtengo de frecuencias a buscar
        self.freq_bpfo = str(round(self.widgets.ui.slider_bpfo.value() / 500) * 500)
        self.freq_bpfi = str(round(self.widgets.ui.slider_bpfi.value() / 500) * 500)
        self.freq_ftf = str(round(self.widgets.ui.slider_ftf.value() / 500) * 500)
        self.freq_bsf = str(round(self.widgets.ui.slider_bsf.value() / 500) * 500)
        
        print("Configuracion realizada")
        print("Tiempo de ensayo:"+ str(self.seconds_total)+ "seg")
        print("Tiempo de intervalo:"+ str(self.seconds_standby)+ "seg")
        print("Frecuencia BPFO: "+ self.freq_bpfo+ "Hz")
        print("Frecuencia BPFI: "+ self.freq_bpfi+ "Hz")
        print("Frecuencia FTF: "+ self.freq_ftf+ "Hz")
        print("Frecuencia BSF: "+ self.freq_bsf+ "Hz")

        # Asigno rango dinamico a progressbar
        self.widgets.ui.progress_bar_ensayo.setRange(0, int(self.seconds_total))
        self.widgets.ui.progress_bar_programa.setRange(0, NUM_ENSAYOS)

        # Enviar por mqtt los datos de configuracion
        self.mqtt_obj.send("smr/start", True)
        self.mqtt_obj.send("rodAnt/frecBPFO", int(self.freq_bpfo))
        self.mqtt_obj.send("rodAnt/frecBPFI", int(self.freq_bpfi))
        self.mqtt_obj.send("rodAnt/frecBSF", int(self.freq_bsf))
        self.mqtt_obj.send("rodAnt/frecFTF", int(self.freq_ftf))
        self.mqtt_obj.send("rodPos/frecBPFO", int(self.freq_bpfo))
        self.mqtt_obj.send("rodPos/frecBPFI", int(self.freq_bpfi))
        self.mqtt_obj.send("rodPos/frecBSF", int(self.freq_bsf))
        self.mqtt_obj.send("rodPos/frecFTF", int(self.freq_ftf))

        # Des/habilito widget para modo ensayo
        self.widgets_ensayo()
        self.suscrip_topics()
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
        self.init_conf()

    def widgets_config(self):
        """
        Des/habilita widgets en modo configuracion
        """
        self.widgets.ui.time_ensayo.setEnabled(True)
        self.widgets.ui.time_standby.setEnabled(True)

        self.widgets.ui.btn_finish.setEnabled(False)
        self.widgets.ui.btn_init.setEnabled(True)
        
        self.widgets.ui.groupBox_freq.setEnabled(True)
        self.widgets.ui.slider_bpfo.setEnabled(True)
        self.widgets.ui.slider_bpfi.setEnabled(True)
        self.widgets.ui.slider_ftf.setEnabled(True)
        self.widgets.ui.slider_bsf.setEnabled(True)

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

        self.widgets.ui.groupBox_freq.setEnabled(False)
        self.widgets.ui.slider_bpfo.setEnabled(False)
        self.widgets.ui.slider_bpfi.setEnabled(False)
        self.widgets.ui.slider_ftf.setEnabled(False)
        self.widgets.ui.slider_bsf.setEnabled(False)

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

    def suscrip_topics(self):
        self.mqtt_obj.suscrip("rodAnt/fft")
        self.mqtt_obj.suscrip("rodAnt/tempObj")
        self.mqtt_obj.suscrip("rodAnt/acelAxial")
        self.mqtt_obj.suscrip("rodAnt/acelRadial")
        self.mqtt_obj.suscrip("rodAnt/presBPFO")
        self.mqtt_obj.suscrip("rodAnt/presBPFI")
        self.mqtt_obj.suscrip("rodAnt/presBSF")
        self.mqtt_obj.suscrip("rodAnt/presFTF")

        self.mqtt_obj.suscrip("rodPos/fft")
        self.mqtt_obj.suscrip("rodPos/tempObj")
        self.mqtt_obj.suscrip("rodPos/acelAxial")
        self.mqtt_obj.suscrip("rodPos/acelRadial")
        self.mqtt_obj.suscrip("rodPos/presBPFO")
        self.mqtt_obj.suscrip("rodPos/presBPFI")
        self.mqtt_obj.suscrip("rodPos/presBSF")
        self.mqtt_obj.suscrip("rodPos/presFTF")

    def desuscrip_topics(self):
        self.mqtt_obj.desuscrip("rodAnt/fft")
        self.mqtt_obj.desuscrip("rodAnt/tempObj")
        self.mqtt_obj.desuscrip("rodAnt/acelAxial")
        self.mqtt_obj.desuscrip("rodAnt/acelRadial")
        self.mqtt_obj.desuscrip("rodAnt/presBPFO")
        self.mqtt_obj.desuscrip("rodAnt/presBPFI")
        self.mqtt_obj.desuscrip("rodAnt/presBSF")
        self.mqtt_obj.desuscrip("rodAnt/presFTF")

        self.mqtt_obj.desuscrip("rodPos/fft")
        self.mqtt_obj.desuscrip("rodPos/tempObj")
        self.mqtt_obj.desuscrip("rodPos/acelAxial")
        self.mqtt_obj.desuscrip("rodPos/acelRadial")
        self.mqtt_obj.desuscrip("rodPos/presBPFO")
        self.mqtt_obj.desuscrip("rodPos/presBPFI")
        self.mqtt_obj.desuscrip("rodPos/presBSF")
        self.mqtt_obj.desuscrip("rodPos/presFTF")

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
            self.desuscrip_topics()
            # Se vertfica si ya se cumplio el total de ensayos o no
            if self.cont_ensayos == NUM_ENSAYOS:            
                print("Ya se realizaron %d ensayos" %NUM_ENSAYOS)
                self.cont_ensayos = 1
                self.mqtt_obj.send("smr/stop", True)
                # Se vuelve a modo configuracion
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
            self.suscrip_topics()
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

        self.widgets.ui.led_bpfo_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bpfi_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bsf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_ftf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

        self.widgets.ui.led_bpfo_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bpfi_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bsf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_ftf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

        self.widgets.grafica.ax.clear()
        self.widgets.grafica.ax.set_title("Rodamiento anterior")
        self.widgets.grafica.upgrade_fft(self.freq, np.zeros(512))

        self.widgets.grafica2.ax.clear()
        self.widgets.grafica2.ax.set_title("Rodamiento posterior")
        self.widgets.grafica2.upgrade_fft(self.freq, np.zeros(512))

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
        if self.mqtt_obj.pres_bpfo_ant:
            self.widgets.ui.led_bpfo_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_bpfi_ant:
            self.widgets.ui.led_bpfi_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_bsf_ant:
            self.widgets.ui.led_bsf_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_ftf_ant:
            self.widgets.ui.led_ftf_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.fft_ant:
            # paso de str a una lista numpy
            self.fft_ant = np.fromstring(self.mqtt_obj.fft_ant, dtype=float, sep=',')  # Convertir la cadena en una lista de NumPy
            self.widgets.grafica.ax.clear()
            self.widgets.grafica.ax.set_title("Rodamiento anterior")
            self.widgets.grafica.upgrade_fft(self.freq, self.fft_ant)
        
        # Muestro datos recibidos en ui - rodamiento posterior
        if self.mqtt_obj.temp_obj_pos:
            self.widgets.ui.lcd_temp_pos.display(self.mqtt_obj.temp_obj_pos)
        if self.mqtt_obj.acel_axial_pos:
            self.widgets.ui.lcd_axial_pos.display(self.mqtt_obj.acel_axial_pos)
        if self.mqtt_obj.acel_radial_pos:
            self.widgets.ui.lcd_radial_pos.display(self.mqtt_obj.acel_radial_pos)
        if self.mqtt_obj.pres_bpfo_pos:
            self.widgets.ui.led_bpfo_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_bpfi_pos:
            self.widgets.ui.led_bpfi_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_bsf_pos:
            self.widgets.ui.led_bsf_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.pres_ftf_pos:
            self.widgets.ui.led_ftf_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.fft_pos:
            # paso de str a una lista numpy
            self.fft_pos = np.fromstring(self.mqtt_obj.fft_pos, dtype=float, sep=',')  # Convertir la cadena en una lista de NumPy
            self.widgets.grafica2.ax.clear()
            self.widgets.grafica2.ax.set_title("Rodamiento posterior")
            self.widgets.grafica2.upgrade_fft(self.freq, self.fft_pos)

        # Si se registra alguna freq se guarda datos en base de datos
        self.upgrade_db()

        self.mqtt_obj.pres_bpfo_ant = False
        self.mqtt_obj.pres_bpfi_ant = False
        self.mqtt_obj.pres_bsf_ant = False
        self.mqtt_obj.pres_ftf_ant = False

        self.mqtt_obj.pres_bpfo_pos = False
        self.mqtt_obj.pres_bpfi_pos = False
        self.mqtt_obj.pres_bsf_pos = False
        self.mqtt_obj.pres_ftf_pos = False

        # Reseteo buffer para topic y msg
        self.mqtt_obj.topic = None
        self.mqtt_obj.msg = None        

    def upgrade_db(self):
        """
        Carga nuevo frame a base de datos
        """
        if self.mqtt_obj.pres_bpfo_ant or \
            self.mqtt_obj.pres_bpfi_ant or \
            self.mqtt_obj.pres_ftf_ant or \
            self.mqtt_obj.pres_bsf_ant:
                self.agregar_db_ant(
                    self.cont_ensayos, 
                    self.seconds_total, 
                    self.mqtt_obj.pres_bpfo_ant, 
                    self.mqtt_obj.pres_bpfi_ant, 
                    self.mqtt_obj.pres_ftf_ant, 
                    self.mqtt_obj.pres_bsf_ant, 
                    self.mqtt_obj.temp_obj_ant, 
                    self.mqtt_obj.acel_axial_ant, 
                    self.mqtt_obj.acel_radial_ant
                    )

        if self.mqtt_obj.pres_bpfo_pos or \
            self.mqtt_obj.pres_bpfi_pos or \
            self.mqtt_obj.pres_ftf_pos or \
            self.mqtt_obj.pres_bsf_pos:
                self.agregar_db_pos(
                    self.cont_ensayos, 
                    self.seconds_total, 
                    self.mqtt_obj.pres_bpfo_pos, 
                    self.mqtt_obj.pres_bpfi_pos, 
                    self.mqtt_obj.pres_ftf_pos, 
                    self.mqtt_obj.pres_bsf_pos, 
                    self.mqtt_obj.temp_obj_pos, 
                    self.mqtt_obj.acel_axial_pos, 
                    self.mqtt_obj.acel_radial_pos
                    )