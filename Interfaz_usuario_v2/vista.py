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
from matplotlib.animation import FuncAnimation

import numpy as np
from menu_v2 import *
from modelo import *

class Canvas_grafica(FigureCanvas):
    def __init__(self, ):
        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.freq_initial = np.arange(0, 512*37, 37)
        self.mag_initial = np.zeros(512)

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

        # Crear la línea inicial
        self.line, = self.ax.plot(self.freq_initial, self.mag_initial)


    def upgrade_fft(self, freq, mag):
        mag_initial = self.mag_initial
        mag_final = mag

        # Establecer límites del eje X e Y
        #self.ax.set_xlim(-100, 19000)
        #self.ax.set_ylim(-40, 60)
        
        # Creo grilla
        #for i in range(0, 19000, 1000):
        #    self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        #for j in range(-40, 60, 10):   
        #    self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)
            
        # Establece nombres de ejes y tamanio
        #matplotlib.rcParams['font.size'] = 9
        #self.ax.set_xlabel("Frecuencia[Hz]")
        #self.ax.set_ylabel("Amplitud[dBV]")

        # Asigno nuevos valores de punto para grafico
        #self.ax.plot(freq, mag)
        animation = FuncAnimation(self.fig, self.update_frame, frames=100, fargs=(mag_initial, mag_final),interval=1, blit=True, repeat=False)

        self.draw()
        self.mag_initial = mag_final

    # Metodo para agregar frames al cambiar de valor
    def update_frame(self, frame, mag_initial, mag_final):
        mag_interp = np.linspace(mag_initial, mag_final, 100)
        self.line.set_ydata(mag_interp[frame])
        return self.line,


class Mainwindow(QMainWindow):
    def __init__(self, ):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Para crear y actualizar grafico fft
        self.grafica = Canvas_grafica()
        self.grafica2 = Canvas_grafica()

        self.measure = Measure(self)

        # Registrar el manejador de eventos de movimiento del ratón sonbre grafico
        self.grafica.fig.canvas.mpl_connect('motion_notify_event', self.onmove)
        # Registrar el manejador de eventos de movimiento del ratón sonbre grafico
        self.grafica2.fig.canvas.mpl_connect('motion_notify_event', self.onmove)

        # Asigno rango default a qprogressbar
        self.ui.progress_bar_ensayo.setValue(0)
        self.ui.progress_bar_ensayo.setRange(0, 100)  # Asignar rango de 0 a 100

        self.ui.fft_ant.addWidget(self.grafica)
        self.ui.fft_pos.addWidget(self.grafica2)

        self.grafica.ax.set_title("Rodamiento anterior")
        self.grafica2.ax.set_title("Rodamiento posterior")

        self.ui.notificacion.setText("Esperando configuracion")

        # Asigno metodos a cada boton
        ## Uso lambda para poder a acceder a ui desde el modelo
        self.ui.btn_finish.clicked.connect(self.measure.finish_test)
        self.ui.btn_init.clicked.connect(self.measure.init_ensayo)
        self.ui.btn_forzar.clicked.connect(self.measure.forzar_finish_ensayo)

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

    # Función para manejar los eventos de movimiento del ratón sobre grafico
    def onmove(self, event):
        if event.inaxes == self.grafica.ax:
            freq, mag = event.xdata, event.ydata 
            msj = "  Freq={:.2f}Hz\n  Mag={:.2f}dBV".format(freq, mag)
            self.ui.value_fft_ant.setText(msj)

        if event.inaxes == self.grafica2.ax:
            freq, mag = event.xdata, event.ydata 
            msj = "  Freq={:.2f}Hz\n  Mag={:.2f}dBV".format(freq, mag)
            self.ui.value_fft_pos.setText(msj)