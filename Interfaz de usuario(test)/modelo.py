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
        self.topic = None
        self.msg = None

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
        print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
        self.topic = msg.topic
        self.msg = msg.payload.decode()

    def suscrip(self, topic):
        self.client.subscribe(topic)
        self.client.on_message = self.on_message

    def desuscrip(self, topic):
        self.client.unsubscribe(topic)

class Measure():
    
    def __init__(self):
        super().__init__()
        #self.mqtt_obj = Mqtt("192.168.68.168", 1883)
        self.mqtt_obj = Mqtt("192.168.1.108", 1883)
        self.cont_ensayos = 1

        self.freq = []
        for i in range(512): # Cantidad de muestras fft
            self.freq.append(37*i)

    def init_conf(self, ):
        #self.menu.ui.groupBox_time.setEnabled(False)
        self.menu.ui.groupBox_leds.setEnabled(False)
        self.menu.ui.groupBox_meas.setEnabled(False)

        self.menu.ui.time_ensayo.setEnabled(True)

        self.menu.ui.groupBox_freq.setEnabled(True)
        self.menu.ui.slider_bpfo.setEnabled(True)
        self.menu.ui.slider_bpfi.setEnabled(True)
        self.menu.ui.slider_ftf.setEnabled(True)
        self.menu.ui.slider_bsf.setEnabled(True)

        self.menu.ui.btn_init.setEnabled(True)

        self.notificacion("Esperando configuracion")
        self.menu.ui.progress_bar_programa.setValue(0)
        self.menu.ui.progress_bar_ensayo.setValue(0)

    """
    Obtiene parametros del ui y los envia por mqtt
    """
    def finish_conf(self, menu):
        self.menu = menu
        self.mqtt_obj.start()

        # Obtener valor de tiempo de cada ensayo
        self.selected_time = self.menu.ui.time_ensayo.time() # va a cambiar por addSecs()
        # Se debe obtener los segundos totales para determinar el rango de la progressbar(valores fijos)
        self.minutes = self.selected_time.minute()
        self.seconds = self.selected_time.second()
        self.seconds_total = (self.minutes * 60 + self.seconds)
        self.seconds_total_aux = self.seconds_total

        self.seconds_standby = 10  # Valor ramdom de standby
        self.seconds_standby_aux = self.seconds_standby  # Valor ramdom de standby
        # Asigno rango dinamico a progressbar
        self.menu.ui.progress_bar_ensayo.setRange(0, int(self.seconds_total))
        self.menu.ui.progress_bar_programa.setRange(0, 5)

        # Obtener configuracion de frecuencias a buscar
        self.freq_bpfo = str(self.menu.ui.slider_bpfo.value())
        self.freq_bpfi = str(self.menu.ui.slider_bpfi.value())
        self.freq_ftf = str(self.menu.ui.slider_ftf.value())
        self.freq_bsf = str(self.menu.ui.slider_bsf.value())
        
        print("Tiempo seleccionado:"+ str(self.seconds_total)+ "seg")
        
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

        self.init_ensayos()

    def init_ensayos(self, ):
        # Bloquear acceso a ciertos widgets hasta que termine el sistema
        self.menu.ui.time_ensayo.setEnabled(False)

        self.menu.ui.groupBox_freq.setEnabled(False)
        self.menu.ui.slider_bpfo.setEnabled(False)
        self.menu.ui.slider_bpfi.setEnabled(False)
        self.menu.ui.slider_ftf.setEnabled(False)
        self.menu.ui.slider_bsf.setEnabled(False)

        self.menu.ui.btn_init.setEnabled(False)

        # Habilito widgets para ver datos
        #self.menu.ui.groupBox_time.setEnabled(True)
        self.menu.ui.groupBox_leds.setEnabled(True)
        self.menu.ui.groupBox_meas.setEnabled(True)

        # Habilito suscripciones
        self.mqtt_obj.suscrip("rodAnt/fft")
        self.mqtt_obj.suscrip("rodAnt/tempObj")
        self.mqtt_obj.suscrip("rodAnt/acelAxial")
        self.mqtt_obj.suscrip("rodAnt/acelRadial")
        self.mqtt_obj.suscrip("rodAnt/presBPFO")
        self.mqtt_obj.suscrip("rodAnt/presBPFI")
        self.mqtt_obj.suscrip("rodAnt/presBSF")
        self.mqtt_obj.suscrip("rodAnt/presFTF")

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
            print("Finalizo contador")
            # Cargo valor a progressbar cada vez que finaliza un ensayo
            self.menu.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
            # Reseteo 'leds'
            self.menu.ui.led_bpfo.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bpfi.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_bsf.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
            self.menu.ui.led_ftf.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")

            # Desuscricpion cada vez que termine programa
            self.mqtt_obj.desuscrip("rodAnt/fft")
            self.mqtt_obj.desuscrip("rodAnt/tempObj")
            self.mqtt_obj.desuscrip("rodAnt/acelAxial")
            self.mqtt_obj.desuscrip("rodAnt/acelRadial")
            self.mqtt_obj.desuscrip("rodAnt/presBPFO")
            self.mqtt_obj.desuscrip("rodAnt/presBPFI")
            self.mqtt_obj.desuscrip("rodAnt/presBSF")
            self.mqtt_obj.desuscrip("rodAnt/presFTF")
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
            print("Finalizo contador 2")
            # Habilito suscripciones
            self.mqtt_obj.suscrip("rodAnt/fft")
            self.mqtt_obj.suscrip("rodAnt/tempObj")
            self.mqtt_obj.suscrip("rodAnt/acelAxial")
            self.mqtt_obj.suscrip("rodAnt/acelRadial")
            self.mqtt_obj.suscrip("rodAnt/presBPFO")
            self.mqtt_obj.suscrip("rodAnt/presBPFI")
            self.mqtt_obj.suscrip("rodAnt/presBSF")
            self.mqtt_obj.suscrip("rodAnt/presFTF")

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
        # Reseteo 'leds'
        self.menu.ui.led_bpfo.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.menu.ui.led_bpfi.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.menu.ui.led_bsf.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        self.menu.ui.led_ftf.setStyleSheet("background-color: red; border-radius: 10px; border: 2px solid darkred;")
        
        # Verifico si hay datos recibidos por broker
        if self.mqtt_obj.topic == "rodAnt/tempObj":
            print("Temperatura obj: ", self.mqtt_obj.msg, "°C")
            self.menu.ui.lcd_temperatura.display(float(self.mqtt_obj.msg))
        if self.mqtt_obj.topic == "rodAnt/acelAxial":
            print("Accel axial: ", self.mqtt_obj.msg)
            self.menu.ui.lcd_vibra_axial.display(float(self.mqtt_obj.msg))
        if self.mqtt_obj.topic == "rodAnt/acelRadial":
            print("Accel radial: ", self.mqtt_obj.msg)
            self.menu.ui.lcd_vibra_radial.display(float(self.mqtt_obj.msg))
        if self.mqtt_obj.topic == "rodAnt/presBPFO":
            print("Recibo BPFO")
            self.menu.ui.led_bpfo.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.topic == "rodAnt/presBPFI":
            print("Recibo BPFI")
            self.menu.ui.led_bpfi.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.topic == "rodAnt/presBSF":
            print("Recibo BSF")
            self.menu.ui.led_bsf.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.topic == "rodAnt/presFTF":
            print("Recibo FTF")
            self.menu.ui.led_ftf.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
        if self.mqtt_obj.topic == "rodAnt/fft":
            self.menu.grafica.upgrade_fft(self.freq, self.mqtt_obj.msg)

        # Reseteo buffer para topic y msg
        self.mqtt_obj.topic = None
        self.mqtt_obj.msg = None        