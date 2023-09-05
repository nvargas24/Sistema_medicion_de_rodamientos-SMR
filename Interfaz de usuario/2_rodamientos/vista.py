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
import math

SAMPLES_FFT = 512

class Grafica_fft(FigureCanvas):
    """
    Clase para dibujar grafico de fft - plots
    """
    def __init__(self, ):
        """
        Constructor de grafica fft - parametros iniciales
        """
        self.xlim_freq_initial = -1
        self.xlim_freq_finish = 19000
        self.ylim_amp_initial = -100
        self.ylim_amp_finish = 10

        self.annotate = None

        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.freq_initial = np.arange(0, SAMPLES_FFT*37, 37)
        self.mag_initial = np.zeros(SAMPLES_FFT)
        
        self.set_graph_fft_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.freq_initial, self.mag_initial, picker=5)

    def update_graph_fft(self, freq, mag, snr, limit_value):
        """
        Metodo para actualizar listas de puntos para grafico fft
        """
        self.set_graph_fft_style()
        self.ax.axhline(float(snr), color='green', linestyle='dashdot', linewidth=2, zorder=2)  
        self.ax.axhline(float(limit_value), color='red', linestyle='dashdot', linewidth=2, zorder=3)
        self.ax.fill_between(freq, -100, float(limit_value), color='red', alpha=0.3)  
        
        self.line, = self.ax.plot(freq, mag, picker=5, zorder=1)

        self.ax.figure.canvas.draw()
        self.show()
        self.annotate = None

    def set_graph_fft_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_freq_initial, self.xlim_freq_finish)
        self.ax.set_ylim(self.ylim_amp_initial, self.ylim_amp_finish)

        # Creo grilla
        step_value_fft_x = round((self.xlim_freq_finish-self.xlim_freq_initial)/20)
        step_value_fft_y = round((self.ylim_amp_finish-self.ylim_amp_initial)/10)
        for i in range(self.xlim_freq_initial, self.xlim_freq_finish, step_value_fft_x):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(self.ylim_amp_initial, self.ylim_amp_finish, step_value_fft_y):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Frecuencia[Hz]")
        self.ax.set_ylabel("Amplitud[dBV]")

    # Debo actualizar annotation antes de grafico
    def update_annotation(self, freq_annot, mag_annot):
        """
        Metodo para actualizar anotacion en grafico
        """
        #if self.annotate:
        #    self.annotate.remove()
        
        freq_annot = round(freq_annot, 0)

        self.annotate = self.ax.annotate(
            f"freq:{freq_annot}Hz\nmag:{mag_annot}dBV",
            xy=(freq_annot, mag_annot),
            xytext=(0, 50),        # Desplazamiento del texto en relación al punto
            textcoords='offset points',  # Coordenadas relativas al punto de la anotación=
            arrowprops=dict(
                facecolor='black',
                arrowstyle='wedge',
                connectionstyle='arc3,rad=0.5',  # Estilo de conexión de la flecha
            ),
            bbox=dict(
                boxstyle='round4',
                edgecolor='red',
                facecolor='white',
                alpha=0.7
            )
        )

class Mainwindow(QMainWindow):
    """
    Clase que interactua con .py de de qt
    """
    def __init__(self, ):
        """
        Constructor para crear objetos, asignar callback y eventos asociados a widgets
        """
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Para crear y actualizar grafico fft
        self.grafica = Grafica_fft()
        self.grafica2 = Grafica_fft()

        self.measure = Measure(self)

        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica.fig.canvas.mpl_connect('pick_event', self.onpick)
        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica2.fig.canvas.mpl_connect('pick_event', self.onpick)

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
        self.ui.captureFFT.clicked.connect(self.measure.save_image)

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

        self.ui.lcd_time_ensayo.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_pos.display(f"{0:02d}.{0:02d}")

    def on_slider_value_changed(self, value):
        """
        Metodo para redondear valores tomados de slider en qt
        """
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

    def onpick(self, event):
        """
        Metodo asociado a evento de click sobre grafico
        """
        if self.grafica.line == event.artist:
            # Lógica para grafico
            xdata = self.grafica.line.get_xdata()
            ydata = self.grafica.line.get_ydata()
            index = event.ind[0]

            freq = xdata[index]
            mag = ydata[index]
            msj = "  Freq={:.2f}Hz\n  Mag={:.2f}dBV".format(freq, mag)
            self.ui.value_fft_ant.setText(msj)

        elif self.grafica2.line == event.artist:
            # Lógica para grafico2
            xdata = self.grafica2.line.get_xdata()
            ydata = self.grafica2.line.get_ydata()
            index = event.ind[0]

            freq = xdata[index]
            mag = ydata[index]
            msj = "  Freq={:.2f}Hz\n  Mag={:.2f}dBV".format(freq, mag)
            self.ui.value_fft_pos.setText(msj)