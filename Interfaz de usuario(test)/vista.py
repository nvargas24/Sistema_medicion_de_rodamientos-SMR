import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QDoubleValidator
from PySide2 import QtCore as core

import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

from menu import *
from modelo import *

class Canvas_grafica(FigureCanvas):
    def __init__(self, ):
        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none") 
        super().__init__(self.fig)

        # Establecer límites del eje X e Y
        self.ax.set_xlim(-100, 19000)
        self.ax.set_ylim(-40, 60)

        for i in range(0, 19000, 1000):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(-40, 60, 10):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)

        # Establecer estilo de fuente y tamaño
        matplotlib.rcParams['font.size'] = 12
        plt.title("Grafico FFT")
        plt.xlabel("Frecuencia[Hz]")
        plt.ylabel("Amplitud[dBV]")

    def upgrade_fft(self, freq, mag):
        self.ax.clear()  # Borrar el contenido del subplot

        # Establecer límites del eje X e Y
        self.ax.set_xlim(-100, 19000)
        self.ax.set_ylim(-40, 60)

        for i in range(0, 19000, 1000):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(-40, 60, 10):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)
            
        # Establecer estilo de fuente y tamaño
        matplotlib.rcParams['font.size'] = 12
        self.ax.set_title("Grafico FFT")
        self.ax.set_xlabel("Frecuencia[Hz]")
        self.ax.set_ylabel("Amplitud[dBV]")

        self.ax.plot(freq, mag)

        self.draw()  # Actualizar gráfico


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

        # Para crear y actualizar grafico fft
        self.grafica = Canvas_grafica()
        self.ui.grafico_fft.addWidget(self.grafica)

        # Deshabilito widgets que hasta que finalice configuracion
        #self.ui.groupBox_time.setEnabled(False)
        self.ui.groupBox_leds.setEnabled(False)
        self.ui.groupBox_meas.setEnabled(False)

        self.ui.notificacion.setText("Esperando configuracion")

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
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        
        self.timer1.timeout.connect(self.measure.timer_ensayo)
        self.timer2.timeout.connect(self.measure.timer_standby)

    def on_slider_bpfo_value_changed(self, value):
        self.ui.label_slider_bpfo.setText(f"{value}Hz")

    def on_slider_bpfi_value_changed(self, value):
        self.ui.label_slider_bpfi.setText(f"{value}Hz")

    def on_slider_ftf_value_changed(self, value):
        self.ui.label_slider_ftf.setText(f"{value}Hz")
    
    def on_slider_bsf_value_changed(self, value):
        self.ui.label_slider_bsf.setText(f"{value}Hz")