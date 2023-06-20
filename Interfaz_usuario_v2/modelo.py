from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time

import paho.mqtt.client as mqtt

class Mqtt:
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

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
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker_host, self.broker_port)
        self.client.loop_start()

    def send(self, topic, message):
        self.client.publish(topic, message)

    def on_message(self, client, userdata, msg):
        #print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
        self.topic = msg.topic
        self.msg = msg.payload.decode()

        # Verifico si hay datos recibidos por broker y doy formato
        if self.topic == "rodAnt/tempObj":
            self.temp_obj_ant = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelAxial":
            self.acel_axial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelRadial":
            self.acel_radial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/presBPFO":
            self.pres_bpfo_ant = self.msg
        if self.topic == "rodAnt/presBPFI":
            self.pres_bpfi_ant = self.msg
        if self.topic == "rodAnt/presBSF":
            self.pres_bsf_ant = self.msg
        if self.topic == "rodAnt/presFTF":
            self.pres_ftf_ant = self.msg
        if self.topic == "rodAnt/fft":
            self.fft_ant = self.msg

        if self.topic == "rodPos/tempObj":
            self.temp_obj_ant = "{:.2f}".format(float(self.msg)) 
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

    def suscrip(self, topic):
        self.client.subscribe(topic)
        self.client.on_message = self.on_message

    def desuscrip(self, topic):
        self.client.unsubscribe(topic)

class Measure():
    
    def __init__(self):
        super().__init__()
        #self.mqtt_obj = Mqtt("192.168.68.168", 1883)
        self.mqtt_obj = Mqtt("192.168.1.107", 1883)
        #self.mqtt_obj = Mqtt("192.168.68.203", 1883)       
        self.cont_ensayos = 1

        self.freq = []
        for i in range(512): # Cantidad de muestras fft
            self.freq.append(37*i)

    def init_conf(self, ):
        self.menu.ui.time_ensayo.setEnabled(True)
        self.menu.ui.time_standby.setEnabled(True)
        self.menu.ui.btn_finish.setEnabled(False)
        self.menu.ui.btn_init.setEnabled(True)
        
        self.menu.ui.groupBox_freq.setEnabled(True)
        self.menu.ui.slider_bpfo.setEnabled(True)
        self.menu.ui.slider_bpfi.setEnabled(True)
        self.menu.ui.slider_ftf.setEnabled(True)
        self.menu.ui.slider_bsf.setEnabled(True)

        self.menu.ui.led_ant.setEnabled(False)
        self.menu.ui.led_pos.setEnabled(False)
        self.menu.ui.lcd_time_ensayo.setEnabled(False)
        self.menu.ui.progress_bar_ensayo.setEnabled(False)
        self.menu.ui.btn_forzar.setEnabled(False)

        self.menu.ui.lcd_temp_ant.setEnabled(False)
        self.menu.ui.lcd_axial_ant.setEnabled(False)
        self.menu.ui.lcd_radial_ant.setEnabled(False)
        self.menu.ui.lcd_temp_pos.setEnabled(False)
        self.menu.ui.lcd_axial_pos.setEnabled(False)
        self.menu.ui.lcd_radial_pos.setEnabled(False)

        self.notificacion("Esperando configuracion")
        self.menu.ui.progress_bar_programa.setValue(0)
        self.menu.ui.progress_bar_ensayo.setValue(0)

    """
    Obtiene parametros del ui y los envia por mqtt
    """
    def finish_conf(self, menu):
        self.menu = menu
        self.mqtt_obj.start()

        # Obtengo tiempo de cada ensayo
        self.selected_time = self.menu.ui.time_ensayo.time()
        self.minutes = self.selected_time.minute()
        self.seconds = self.selected_time.second()
        self.seconds_total = (self.minutes * 60 + self.seconds)
        self.seconds_total_aux = self.seconds_total

        # Obtengo tiempo de intervalo entre ensayo
        self.seconds_standby = self.menu.ui.time_standby.time().second()
        self.seconds_standby_aux = self.seconds_standby
        
        # Asigno rango dinamico a progressbar
        self.menu.ui.progress_bar_ensayo.setRange(0, int(self.seconds_total))
        self.menu.ui.progress_bar_programa.setRange(0, 5)

        # Obtengo de frecuencias a buscar
        self.freq_bpfo = str(round(self.menu.ui.slider_bpfo.value() / 500) * 500)
        self.freq_bpfi = str(round(self.menu.ui.slider_bpfi.value() / 500) * 500)
        self.freq_ftf = str(round(self.menu.ui.slider_ftf.value() / 500) * 500)
        self.freq_bsf = str(round(self.menu.ui.slider_bsf.value() / 500) * 500)
        
        print("Tiempo de ensayo:"+ str(self.seconds_total)+ "seg")
        print("Tiempo de intervalo:"+ str(self.seconds_standby)+ "seg")
        print("Frecuencia BPFO: "+ self.freq_bpfo+ "Hz")
        print("Frecuencia BPFI: "+ self.freq_bpfi+ "Hz")
        print("Frecuencia FTF: "+ self.freq_ftf+ "Hz")
        print("Frecuencia BSF: "+ self.freq_bsf+ "Hz")

        print("Configuracion realizada")

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

        self.init_ensayos()

    def init_ensayos(self, ):
        # Bloquear acceso a ciertos widgets hasta que termine el sistema
        self.menu.ui.time_ensayo.setEnabled(False)
        self.menu.ui.time_standby.setEnabled(False)

        self.menu.ui.groupBox_freq.setEnabled(False)
        self.menu.ui.slider_bpfo.setEnabled(False)
        self.menu.ui.slider_bpfi.setEnabled(False)
        self.menu.ui.slider_ftf.setEnabled(False)
        self.menu.ui.slider_bsf.setEnabled(False)

        self.menu.ui.btn_init.setEnabled(False)
        self.menu.ui.btn_finish.setEnabled(True)

        # Habilito widgets para ver datos
        self.menu.ui.led_ant.setEnabled(True)
        self.menu.ui.led_pos.setEnabled(True)
        self.menu.ui.lcd_time_ensayo.setEnabled(True)
        self.menu.ui.progress_bar_ensayo.setEnabled(True)
        self.menu.ui.btn_forzar.setEnabled(True)
        self.menu.ui.lcd_temp_ant.setEnabled(True)
        self.menu.ui.lcd_axial_ant.setEnabled(True)
        self.menu.ui.lcd_radial_ant.setEnabled(True)
        self.menu.ui.lcd_temp_pos.setEnabled(True)
        self.menu.ui.lcd_axial_pos.setEnabled(True)
        self.menu.ui.lcd_radial_pos.setEnabled(True)

        # Habilito suscripciones
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

        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.menu.timer1.start(1000)

    # Cuando timer finalice entra a este metodo
    def timer_ensayo(self, ):
        self.notificacion("Ensayo "+ str(self.cont_ensayos) + " en proceso")

        # Se obtiene minutos y segundos a mostrar en lcd
        self.minutes = self.seconds_total//60
        self.seconds = self.seconds_total%60
        self.menu.ui.lcd_time_ensayo.display(f"{self.minutes:02d}:{self.seconds:02d}")
        # Cargo valor a progressbar, segun avance el contador
        self.menu.ui.progress_bar_ensayo.setValue(int(self.seconds_total_aux)-int(self.seconds_total))
        # Cada vez que se cumpla un 1 seg resto un valor del total de segundos
        self.seconds_total = self.seconds_total-1
        # Se verifica si el dispositivo publico algo en un topic
        self.data_recive()

        # Se detiene contador para que no siga con parte negativa
        if self.seconds_total<0 : 
            self.menu.timer1.stop()
            # Cargo valor a progressbar cada vez que finaliza un ensayo
            self.menu.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
            # Reseteo 'leds'
            self.menu.ui.led_bpfo_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bpfi_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bsf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_ftf_ant.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bpfo_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bpfi_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bsf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_ftf_pos.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

            # Desuscricpion cada vez que termine programa
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
            # Se vertfica si ya se cumplio el total de ensayos o no
            if self.cont_ensayos == 5:            
                print("Ya se realizaron 5 ensayos")
                self.cont_ensayos = 1
                self.init_conf()
            else:
                self.menu.timer2.start(1000)
                self.seconds_total = self.seconds_total_aux

    def timer_standby(self, ):
        self.notificacion("Nuevo ensayo en "+ str(self.seconds_standby))
        self.seconds_standby = self.seconds_standby-1

        # Se detiene contador para que no siga con parte negativa
        if self.seconds_standby<0 : 
            self.menu.timer2.stop()
            # Habilito suscripciones
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
            self.menu.timer1.start(1000)
            self.seconds_standby = self.seconds_standby_aux
            self.cont_ensayos = self.cont_ensayos +1

    """
    Fuerza finalizacion de ensayo actual y arranca el siguiente (si es que lo hay)
    """
    def finish_ensayo(self, ):
        print("Finaliza ensayo "+ str(self.cont_ensayos) +" - Forzado")
        self.menu.timer1.stop()

        # Seteo widget como si hubiese terminado ensayo
        self.menu.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        self.menu.ui.progress_bar_ensayo.setValue(int(self.seconds_total_aux))
        self.menu.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
        
        # En el caso de que se cumplan los 5 ensayos pase a modo config
        if self.cont_ensayos == 5:            
            self.cont_ensayos = 1
            self.init_conf()
        else:
            self.menu.timer2.start(1000)
            self.seconds_total = self.seconds_total_aux
    """
    Informa eventos
    """
    def notificacion(self, msj):
        self.menu.ui.notificacion.setText(str(msj))
    
    """
    Muestra lecturas obtenidas de sensores en display
    """
    def data_recive(self, ):

        # Muestro datos recibidos por qlcd
        if self.mqtt_obj.temp_obj_ant:
            self.menu.ui.lcd_temp_ant.display(self.mqtt_obj.temp_obj_ant)
        if self.mqtt_obj.acel_axial_ant:
            self.menu.ui.lcd_axial_ant.display(self.mqtt_obj.acel_axial_ant)
        if self.mqtt_obj.acel_radial_ant:
            self.menu.ui.lcd_radial_ant.display(self.mqtt_obj.acel_radial_ant)
        if self.mqtt_obj.pres_bpfo_ant:
            self.menu.ui.led_bpfo_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bpfo_ant = False
        if self.mqtt_obj.pres_bpfi_ant:
            self.menu.ui.led_bpfi_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bpfi_ant = False
        if self.mqtt_obj.pres_bsf_ant:
            self.menu.ui.led_bsf_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bsf_ant = False
        if self.mqtt_obj.pres_ftf_ant:
            self.menu.ui.led_ftf_ant.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_ftf_ant = False
        if self.mqtt_obj.fft_ant:
            self.menu.grafica.ax.clear()  # Borrar el contenido del subplot
            self.menu.grafica.ax.set_title("Rodamiento anterior")
            self.menu.grafica.upgrade_fft(self.freq, self.mqtt_obj.fft_ant)

        if self.mqtt_obj.temp_obj_pos:
            self.menu.ui.lcd_temp_pos.display(self.mqtt_obj.temp_obj_pos)
        if self.mqtt_obj.acel_axial_pos:
            self.menu.ui.lcd_axial_pos.display(self.mqtt_obj.acel_axial_pos)
        if self.mqtt_obj.acel_radial_pos:
            self.menu.ui.lcd_radial_pos.display(self.mqtt_obj.acel_radial_pos)
        if self.mqtt_obj.pres_bpfo_pos:
            self.menu.ui.led_bpfo_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bpfo_pos = False
        if self.mqtt_obj.pres_bpfi_pos:
            self.menu.ui.led_bpfi_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bpfi_pos = False
        if self.mqtt_obj.pres_bsf_pos:
            self.menu.ui.led_bsf_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_bsf_pos = False
        if self.mqtt_obj.pres_ftf_pos:
            self.menu.ui.led_ftf_pos.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
            self.mqtt_obj.pres_ftf_pos = False
        if self.mqtt_obj.fft_pos:
            self.menu.grafica2.ax.clear()  # Borrar el contenido del subplot
            self.menu.grafica2.ax.set_title("Rodamiento Posterior")
            self.menu.grafica2.upgrade_fft(self.freq, self.mqtt_obj.fft_pos)

        # Reseteo buffer para topic y msg
        self.mqtt_obj.topic = None
        self.mqtt_obj.msg = None        