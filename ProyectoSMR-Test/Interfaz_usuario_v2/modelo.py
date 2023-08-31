from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time
import numpy as np
import os

import math
import paho.mqtt.client as mqtt

import mysql.connector

NUM_ENSAYOS = 2

class BaseDatosMySQL():
    def connectDB(self, user, password, database):
        '''!
        Function to connect to SMR's database
        @return conection
        '''
        try:
            connection = mysql.connector.connect(host = "localhost", user = user, password = password, database = database)
            return connection
        
        except mysql.connector.Error as e:
            print(e)

    def readStageFromDB(self, connection, table, stageNum, rows):
        query = 'SELECT * FROM ' + table + ' WHERE stageNum = ' + str(stageNum) + ' ORDER BY id DESC LIMIT ' + str(rows)
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                return cursor.fetchall()
            
            except Exception as e:
                print(f'Hubu un error en la consulta a la base de datos {e}')

class Mqtt:
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

        self.time_stamp_ant = False
        self.temp_obj_ant = 0.0
        self.acel_axial_ant = 0.0
        self.acel_radial_ant = 0.0
        self.pres_bpfi_ant = False
        self.pres_bpfo_ant = False
        self.pres_bsf_ant = False
        self.pres_ftf_ant = False
        self.fft_ant = False
        self.snr_ant = False
        self.limit_value_ant = False

        self.time_stamp_pos = False       
        self.temp_obj_pos = 0.0
        self.acel_axial_pos = 0.0
        self.acel_radial_pos = 0.0
        self.pres_bpfi_pos = False
        self.pres_bpfo_pos = False
        self.pres_bsf_pos = False
        self.pres_ftf_pos = False
        self.fft_pos = False
        self.snr_pos = False
        self.limit_value_pos = False


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
        #print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
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
        if self.topic == "rodAnt/timeStamp":
            self.time_stamp_ant = self.msg
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
        if self.topic == "rodAnt/snr":
            self.snr_ant = self.msg
        if self.topic == "rodAnt/limitValue":
            self.limit_value_ant = self.msg

        if self.topic == "rodPos/timeStamp":
            self.time_stamp_pos = self.msg
        if self.topic == "rodPos/tempObj":
            self.temp_obj_pos = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelAxial":
            self.acel_axial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelRadial":
            self.acel_radial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/presBPFO":
            self.pres_bpfo_pos = int(self.msg)
        if self.topic == "rodPos/presBPFI":
            self.pres_bpfi_pos = int(self.msg)
        if self.topic == "rodPos/presBSF":
            self.pres_bsf_pos = int(self.msg)
        if self.topic == "rodPos/presFTF":
            self.pres_ftf_pos = int(self.msg)
        if self.topic == "rodPos/fft":
            self.fft_pos = self.msg
        if self.topic == "rodPos/snr":
            self.snr_pos = self.msg
        if self.topic == "rodPos/limitValue":
            self.limit_value_pos = self.msg


    def suscrip_topics(self):
        self.suscrip("rodAnt/timeStamp")
        self.suscrip("rodAnt/fft")
        self.suscrip("rodAnt/tempObj")
        self.suscrip("rodAnt/acelAxial")
        self.suscrip("rodAnt/acelRadial")
        self.suscrip("rodAnt/presBPFO")
        self.suscrip("rodAnt/presBPFI")
        self.suscrip("rodAnt/presBSF")
        self.suscrip("rodAnt/presFTF")
        self.suscrip("rodAnt/snr")
        self.suscrip("rodAnt/limitValue")

        self.suscrip("rodPos/timeStamp")
        self.suscrip("rodPos/fft")
        self.suscrip("rodPos/tempObj")
        self.suscrip("rodPos/acelAxial")
        self.suscrip("rodPos/acelRadial")
        self.suscrip("rodPos/presBPFO")
        self.suscrip("rodPos/presBPFI")
        self.suscrip("rodPos/presBSF")
        self.suscrip("rodPos/presFTF")
        self.suscrip("rodPos/snr")
        self.suscrip("rodPos/limitValue")


    def desuscrip_topics(self):
        self.desuscrip("rodAnt/timeStamp")
        self.desuscrip("rodAnt/fft")
        self.desuscrip("rodAnt/tempObj")
        self.desuscrip("rodAnt/acelAxial")
        self.desuscrip("rodAnt/acelRadial")
        self.desuscrip("rodAnt/presBPFO")
        self.desuscrip("rodAnt/presBPFI")
        self.desuscrip("rodAnt/presBSF")
        self.desuscrip("rodAnt/presFTF")
        self.desuscrip("rodAnt/snr")
        self.desuscrip("rodAnt/limitValue")

        self.desuscrip("rodPos/timeStamp")    
        self.desuscrip("rodPos/fft")
        self.desuscrip("rodPos/tempObj")
        self.desuscrip("rodPos/acelAxial")
        self.desuscrip("rodPos/acelRadial")
        self.desuscrip("rodPos/presBPFO")
        self.desuscrip("rodPos/presBPFI")
        self.desuscrip("rodPos/presBSF")
        self.desuscrip("rodPos/presFTF")
        self.desuscrip("rodPos/snr")
        self.desuscrip("rodPos/limitValue")

class Measure():
    
    def __init__(self, widgets):
        super().__init__()
        # Atributo para acceder a los widgets
        self.widgets = widgets        
        self.mqtt_obj = Mqtt("192.168.197.29", 1883)
        self.mysql = BaseDatosMySQL()

        self.num_fft = 1
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
        # Inicio conexion a MySQL
        try:
            self.mysql.connectDB(user = "root", password = "raspi", database = "smr" )
        except Exception as e:
            print(e)

        # Inicio conexion mqtt
        try:
            self.mqtt_obj.start()
        except Exception as e:
            print(e)

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
        self.freq_bpfo = str(self.widgets.ui.slider_bpfo.value())
        self.freq_bpfi = str(self.widgets.ui.slider_bpfi.value())
        self.freq_ftf = str(self.widgets.ui.slider_ftf.value())
        self.freq_bsf = str(self.widgets.ui.slider_bsf.value())
        
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
        self.mqtt_obj.suscrip_topics()
        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.widgets.timer1.start(1000)

    def forzar_finish_ensayo(self):
        """
        Fuerza finalizacion de ensayo actual y arranca el siguiente (si es que lo hay)
        """
        # Deshabilito transmision de datos de esp32
        self.mqtt_obj.send("smr/stop", True)
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
        # Deshabilito transmision de datos de esp32
        self.mqtt_obj.send("smr/stop", True)
        # Se vuelve a modo configuracion
        self.mqtt_obj.stop()
        self.init_conf()

    def save_image(self):
        """
        Metodo para capturar grafico fft en tiempo real
        """
        name_fft_ant = os.path.join("capture", f"FFT_ant_{self.num_fft}.tiff")
        name_fft_pos = os.path.join("capture", f"FFT_pos_{self.num_fft}.tiff")

        self.widgets.grafica.fig.savefig(name_fft_ant)
        self.widgets.grafica2.fig.savefig(name_fft_pos)

        self.num_fft += self.num_fft

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
            # Deshabilito transmision de datos de esp32
            self.mqtt_obj.send("smr/stop", True)            
            self.mqtt_obj.desuscrip_topics()
            # Se verifica si ya se cumplio el total de ensayos o no
            if self.cont_ensayos == NUM_ENSAYOS:            
                print("Ya se realizaron %d ensayos" %NUM_ENSAYOS)
                self.cont_ensayos = 1
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
            # Habilito transmision de datos de esp32
            self.mqtt_obj.send("smr/start", True)
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
        self.widgets.grafica.update_graph_fft(self.freq, np.zeros(512), 0, 0)

        self.widgets.grafica2.ax.clear()
        self.widgets.grafica2.ax.set_title("Rodamiento posterior")
        self.widgets.grafica2.update_graph_fft(self.freq, np.zeros(512), 0, 0)

    def data_recive(self):
        """
        Muestra lecturas obtenidas de sensores en display
        """
        self.widgets.ui.led_bpfo_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bpfi_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bsf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_ftf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

        self.widgets.ui.led_bpfo_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bpfi_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_bsf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.widgets.ui.led_ftf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

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
            self.mag_bpfo = self.fft_ant[int(float(self.freq_bpfo)/37)]
            self.mag_bpfi = self.fft_ant[int(float(self.freq_bpfi)/37)]
            self.mag_ftf = self.fft_ant[int(float(self.freq_ftf)/37)]
            self.mag_bsf = self.fft_ant[int(float(self.freq_bsf)/37)]
            self.widgets.grafica.ax.clear()
            self.widgets.grafica.ax.set_title("Rodamiento anterior")
            self.widgets.grafica.update_annotation(float(self.freq_bpfo), self.mag_bpfo)
            self.widgets.grafica.update_annotation(float(self.freq_bpfi), self.mag_bpfi)
            self.widgets.grafica.update_annotation(float(self.freq_ftf), self.mag_ftf)
            self.widgets.grafica.update_annotation(float(self.freq_bsf), self.mag_bsf)
            self.widgets.grafica.update_graph_fft(self.freq, self.fft_ant, self.mqtt_obj.snr_ant, self.mqtt_obj.limit_value_ant)
        if self.mqtt_obj.snr_ant:
            self.widgets.ui.label_snr_ant.setText(self.mqtt_obj.snr_ant+"dBV")
            self.widgets.ui.label_snr_lim_ant.setText(self.mqtt_obj.limit_value_ant+"dBV")
        if self.mqtt_obj.time_stamp_ant:
            self.widgets.ui.label_time_stamp_ant.setText(self.mqtt_obj.time_stamp_ant)

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
            self.widgets.grafica2.update_annotation(float(self.freq_bpfo), self.mag_bpfo)
            self.widgets.grafica2.update_annotation(float(self.freq_bpfi), self.mag_bpfi)
            self.widgets.grafica2.update_annotation(float(self.freq_ftf), self.mag_ftf)
            self.widgets.grafica2.update_annotation(float(self.freq_bsf), self.mag_bsf)
            self.widgets.grafica2.update_graph_fft(self.freq, self.fft_pos, self.mqtt_obj.snr_pos, self.mqtt_obj.limit_value_pos)
        if self.mqtt_obj.snr_pos:
            self.widgets.ui.label_snr_pos.setText(self.mqtt_obj.snr_pos+"dBV")
            self.widgets.ui.label_snr_lim_pos.setText(self.mqtt_obj.limit_value_pos+"dBV")
        if self.mqtt_obj.time_stamp_pos:
            self.widgets.ui.label_time_stamp_pos.setText(self.mqtt_obj.time_stamp_pos)

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