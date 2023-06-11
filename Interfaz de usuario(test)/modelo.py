from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time

class Mqtt():
    """
    Inicializa comunicacion mqtt
    """
    def start(self, ): pass

    """
    Envia mensaje por mqtt
    """
    def send(self, topic, msj): pass

    """
    Se suscribe a un topico y devuelve valor obtenido
    """
    def suscrip(self, ): pass
    
    """
    Se desuscribirse de un topico
    """
    def unsuscrip(self, ): pass

class Measure():
    
    def __init__(self):
        self.mqtt = Mqtt()
        self.cont_ensayos = 1

    def init_conf(self, ):
        self.menu.ui.groupBox_time.setEnabled(False)
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

        # Cambaio color de 'led'
        self.menu.ui.led_bpfo.setStyleSheet("background-color: green; border-radius: 10px; border: 2px solid darkgreen;")
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

        print("Configuracion realizada \nDeshabilito widgets")

        ###### Enviar por mqtt los datos de configuracion

        self.init_ensayos()

    def init_ensayos(self, ):
        self.mode = "Modo ensayo"
        # Bloquear acceso a todos los widget hasta que termine el sistema, excepto btn_finish
        self.menu.ui.time_ensayo.setEnabled(False)

        self.menu.ui.groupBox_freq.setEnabled(False)
        self.menu.ui.slider_bpfo.setEnabled(False)
        self.menu.ui.slider_bpfi.setEnabled(False)
        self.menu.ui.slider_ftf.setEnabled(False)
        self.menu.ui.slider_bsf.setEnabled(False)

        self.menu.ui.btn_init.setEnabled(False)

        # Habilito widgets para ver datos
        self.menu.ui.groupBox_time.setEnabled(True)
        self.menu.ui.groupBox_leds.setEnabled(True)
        self.menu.ui.groupBox_meas.setEnabled(True)

        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.menu.timer1.start(1000)

    # Cuando timer finalice entra a este metodo
    def timer_ensayo(self, ):
        self.notificacion("Ensayo "+ str(self.cont_ensayos) + " en proceso")
        
        self.minutes = self.seconds_total//60
        self.seconds = self.seconds_total%60
        self.menu.ui.lcd_time_ensayo.display(f"{self.minutes:02d}:{self.seconds:02d}")
        # Cargo valor a progressbar, segun avance el contador
        self.menu.ui.progress_bar_ensayo.setValue(int(self.seconds_total_aux)-int(self.seconds_total))

        self.seconds_total = self.seconds_total-1
        # Se detiene contador para que no siga con parte negativa
        if self.seconds_total<0 : 
            self.menu.timer1.stop()
            print("Finalizo contador")
            # Cargo valor a progressbar, segun avance el contador            
            self.menu.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
            
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
    def lecturas(self, ): pass

    """
    Modifica 'leds' en caso de detectar alguna frecuencia solicitada
    """
    def fallas_detectadas(self, ): pass

