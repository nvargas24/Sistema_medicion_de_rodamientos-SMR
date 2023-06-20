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

from menu_v2 import *
from modelo import *

class Canvas_grafica(FigureCanvas):
    def __init__(self, ):
        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)
 
        # Establecer límites del eje X e Y
        self.ax.set_xlim(-100, 19000)
        self.ax.set_ylim(-40, 60)

        # Creo grilla
        for i in range(0, 19000, 1000):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(-40, 60, 10):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Frecuencia[Hz]")
        self.ax.set_ylabel("Amplitud[dBV]")

    def upgrade_fft(self, freq, mag_decode):
        # Establecer límites del eje X e Y
        self.ax.set_xlim(-100, 19000)
        self.ax.set_ylim(-40, 60)
        
        # Creo grilla
        for i in range(0, 19000, 1000):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(-40, 60, 10):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)
            
        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Frecuencia[Hz]")
        self.ax.set_ylabel("Amplitud[dBV]")

        # Convierto en lista, la fft en str recibido
        mag = mag_decode.split(',')
        self.mag = [float(value) for value in mag]
        self.ax.plot(freq, self.mag)

        self.draw()

class Mainwindow(QMainWindow):
    def __init__(self, ):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.measure = Measure()

        # Formato a qtimer
        self.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        self.ui.lcd_temp_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_pos.display(f"{0:02d}.{0:02d}")

        # Asigno rango default a qprogressbar
        self.ui.progress_bar_ensayo.setValue(0)
        self.ui.progress_bar_ensayo.setRange(0, 100)  # Asignar rango de 0 a 100

        # Para crear y actualizar grafico fft
        self.grafica = Canvas_grafica()
        self.grafica2 = Canvas_grafica()

        self.ui.fft_ant.addWidget(self.grafica)
        self.ui.fft_pos.addWidget(self.grafica2)

        self.grafica.ax.set_title("Rodamiento anterior")
        self.grafica2.ax.set_title("Rodamiento posterior")

        # Deshabilito widgets hasta que finalice configuracion
        self.ui.btn_finish.setEnabled(False)
        self.ui.led_ant.setEnabled(False)
        self.ui.led_pos.setEnabled(False)
        self.ui.lcd_time_ensayo.setEnabled(False)
        self.ui.progress_bar_ensayo.setEnabled(False)
        self.ui.btn_forzar.setEnabled(False)
        self.ui.lcd_temp_ant.setEnabled(False)
        self.ui.lcd_axial_ant.setEnabled(False)
        self.ui.lcd_radial_ant.setEnabled(False)
        self.ui.lcd_temp_pos.setEnabled(False)
        self.ui.lcd_axial_pos.setEnabled(False)
        self.ui.lcd_radial_pos.setEnabled(False)

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
        self.ui.slider_bpfo.valueChanged.connect(self.on_slider_value_changed)
        self.ui.slider_bpfi.valueChanged.connect(self.on_slider_value_changed)
        self.ui.slider_ftf.valueChanged.connect(self.on_slider_value_changed)
        self.ui.slider_bsf.valueChanged.connect(self.on_slider_value_changed)

        # Creo contador asociado a un metodo que inicia el conteo
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        
        self.timer1.timeout.connect(self.measure.timer_ensayo)
        self.timer2.timeout.connect(self.measure.timer_standby)

    def on_slider_value_changed(self, value):
        rounded_value = round(value / 500) * 500
        sender = self.sender()
        if sender == self.ui.slider_bpfo:
            self.ui.label_slider_bpfo.setText(f"{rounded_value}Hz")
        elif sender == self.ui.slider_bpfi:
            self.ui.label_slider_bpfi.setText(f"{rounded_value}Hz")
        elif sender == self.ui.slider_ftf:
            self.ui.label_slider_ftf.setText(f"{rounded_value}Hz")
        elif sender == self.ui.slider_bsf:
            self.ui.label_slider_bsf.setText(f"{rounded_value}Hz")