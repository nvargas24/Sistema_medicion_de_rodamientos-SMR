import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from menu import *
from modelo import *

class Mainwindow(QMainWindow):
    def __init__(self, ):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.measure = Measure()

        # Formato a qtimer
        self.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        # Asigno rango default a qprogressbar
        self.ui.progress_bar_ensayo.setValue(0)
        self.ui.progress_bar_ensayo.setRange(0, 100)  # Asignar rango de 0 a 100

        # Deshabilito widgets que hasta que finalice configuracion
        self.ui.groupBox_time.setEnabled(False)
        self.ui.groupBox_leds.setEnabled(False)
        self.ui.groupBox_meas.setEnabled(False)

        # Asigno metodos a cada boton
        ## Uso lambda para poder a acceder a ui desde el modelo
        self.ui.btn_finish.clicked.connect(self.close)
        self.ui.btn_init.clicked.connect(lambda: self.measure.finish_conf(self))
        self.ui.btn_forzar.clicked.connect(self.measure.finish_ensayo)
        
        # Se obtiene valor default de slider para label
        self.ui.label_slider_bpfo.setText(f"{self.ui.slider_bpfo.value()}Hz")
        self.ui.label_slider_bpfi.setText(f"{self.ui.slider_bpfi.value()}Hz")
        self.ui.label_slider_ftf.setText(f"{self.ui.slider_ftf.value()}Hz")
        self.ui.label_slider_bsf.setText(f"{self.ui.slider_bsf.value()}Hz")

        # Obtiene valor de slider al realizar un cambio y mostrar en label
        self.ui.slider_bpfo.valueChanged.connect(self.on_slider_bpfo_value_changed)
        self.ui.slider_bpfi.valueChanged.connect(self.on_slider_bpfi_value_changed)
        self.ui.slider_ftf.valueChanged.connect(self.on_slider_ftf_value_changed)
        self.ui.slider_bsf.valueChanged.connect(self.on_slider_bsf_value_changed)

        # Creo contador asociado a un metodo que inicia el conteo
        self.timer = QTimer(self)
        self.timer_standby = QTimer(self)
        
        self.timer.timeout.connect(self.measure.update_clock)
        self.timer_standby.timeout.connect(self.measure.cronometro_stanby)

    def on_slider_bpfo_value_changed(self, value):
        self.ui.label_slider_bpfo.setText(f"{value}Hz")

    def on_slider_bpfi_value_changed(self, value):
        self.ui.label_slider_bpfi.setText(f"{value}Hz")

    def on_slider_ftf_value_changed(self, value):
        self.ui.label_slider_ftf.setText(f"{value}Hz")
    
    def on_slider_bsf_value_changed(self, value):
        self.ui.label_slider_bsf.setText(f"{value}Hz")
