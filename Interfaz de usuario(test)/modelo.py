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
        self.mode = "Modo configuracion"
        self.cont = 1
        self.flag_forzar = 0
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
        # Asigno rango dinamico a progressbar
        self.menu.ui.progress_bar_ensayo.setRange(0, int(self.seconds_total))

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
        self.menu.timer.start(1000)

    # Cuando timer finalice entra a este metodo
    def update_clock(self, ):
        print("Tiempo restante", self.seconds_total)

        self.minutes = self.seconds_total//60
        self.seconds = self.seconds_total%60
        self.menu.ui.lcd_time_ensayo.display(f"{self.minutes:02d}:{self.seconds:02d}")

        self.seconds_total = self.seconds_total-1
        # Se detiene contador para que no siga con parte negativa
        if self.seconds_total<0 : 
            self.menu.timer.stop()
            print("Finalizo contador") 


        """
        if self.selected_time <= QTime(0, 0, 0): #hh, mm, ss
            self.reset_cronometro()

        else:
            self.notificacion("Ensayo " +str(self.cont) +" - en proceso")
            self.cronometro()
        """
    def reset_cronometro(self, ):            
        self.menu.timer_standby()
        self.menu.timer.stop()
        # Se inicia nuevo ensayo
        self.menu.timer.start(1000)
        self.selected_time = self.menu.ui.time_ensayo.time()
        self.cont = self.cont+1

    def cronometro_stanby(self, ):
        self.notificacion("Ajuste velocidad de motor")
        # Standby Mode, para ajustar frecuencia de motor
        self.cont_stanby = 10
        while not self.cont_stanby < 0 and self.flag_forzar == 1:
            print("Nuevo ensayo en " +str(self.cont_stanby))
            self.notificacion("Nuevo ensayo en " +str(self.cont_stanby))
            self.cont_stanby = self.cont_stanby - 1
            time.sleep(1)            
            if self.cont_stanby == 10: self.flag_forzar = 0


    def cronometro(self, ):
        # Restar un segundo al tiempo actual
        self.selected_time = self.selected_time.addSecs(-1)
        
        # Obtener tiempo actual de timer
        self.minutes_now = self.selected_time.minute()
        self.seconds_now = self.selected_time.second()
        self.seconds_total_now = self.minutes_now*60 + self.seconds_now

        # Formatear el tiempo en estilo "mm:ss" y mostrarlo en el QLCDNumber
        self.menu.ui.lcd_time_ensayo.display(f"{self.minutes_now:02d}:{self.seconds_now:02d}")
        # Cargo valor a progressbar, segun avance el contador
        self.menu.ui.progress_bar_ensayo.setValue(int(self.seconds_total)-int(self.seconds_total_now))

    """
    Fuerza finalizacion de ensayo actual y arranca el siguiente (si es que lo hay)
    """
    def finish_ensayo(self, ):
        self.flag_forzar = 1
        print("Finaliza "+ str(self.cont) +" - Forzado")
        self.reset_cronometro()

    """
    Informa eventos
    """
    def notificacion(self, msj):
        self.menu.ui.notificacion.setText(str(msj))
    
    """
    Contador de tiempo para ensayos, tanto el transcurrido como tiempo faltante para el prox
    """
    def time_progress(self): pass

    """
    Muestra lecturas obtenidas de sensores en display
    """
    def lecturas(self, ): pass

    """
    Modifica 'leds' en caso de detectar alguna frecuencia solicitada
    """
    def fallas_detectadas(self, ): pass

