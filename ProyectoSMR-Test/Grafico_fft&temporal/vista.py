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

class Grafica_samples(FigureCanvas):
    """
    Clase para dibujar grafico - plots
    """
    def __init__(self, ):
        """
        Constructor de grafica - parametros iniciales
        """
        self.xlim_sample_initial = 1
        self.xlim_sample_finish = 1024
        self.ylim_volt_initial = 0
        self.ylim_volt_finish = 1024

        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        # ver en programa de sensor, num de muestrar para realizar grafico y num de data 
        self.samples_initial = np.arange(0, SAMPLES_ADC, 1)
        self.volt_initial = np.zeros(SAMPLES_ADC) # ver resolucion de adc 

        self.set_graph_temp_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.samples_initial, self.volt_initial, picker=5)

    def upgrade_graph_temp(self, samples, volt):
        """
        Metodo para actualizar listas de puntos para grafico
        """
        self.set_graph_temp_style()

        self.line, = self.ax.plot(samples, volt, picker=5)
        self.draw()

    def set_graph_temp_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_sample_initial, self.xlim_sample_finish)
        self.ax.set_ylim(self.ylim_volt_initial*0.005, self.ylim_volt_finish*0.005)

        # Creo grilla
        step_value_temp_x = round((self.xlim_sample_finish-self.xlim_sample_initial)/20)
        step_value_temp_y = round((self.ylim_volt_finish-self.ylim_volt_initial)/10)
        for i in range(self.xlim_sample_initial, self.xlim_sample_finish, step_value_temp_x):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(self.ylim_volt_initial, self.ylim_volt_finish, step_value_temp_y):   
            self.ax.axhline(j*0.005, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Samples[#]")
        self.ax.set_ylabel("Volt[V]")

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

        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.freq_initial = np.arange(0, SAMPLES_FFT*37, 37)
        self.mag_initial = np.zeros(SAMPLES_FFT)
        
        self.set_graph_fft_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.freq_initial, self.mag_initial, picker=5)

    def upgrade_graph_fft(self, freq, mag):
        """
        Metodo para actualizar listas de puntos para grafico fft
        """
        self.set_graph_fft_style()

        self.line, = self.ax.plot(freq, mag, picker=5)
        self.draw()

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


class Mainwindow(QMainWindow):
    """
    Clase que interactua con .py de qt
    """
    def __init__(self, ):
        """
        Constructor para crear objetos, asignar callback y eventos asociados a widgets
        """
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Para crear y actualizar grafico
        self.grafica = Grafica_samples()
        self.grafica2 = Grafica_fft()

        self.measure = Measure(self)

        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica.fig.canvas.mpl_connect('pick_event', self.onpick)
        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica2.fig.canvas.mpl_connect('pick_event', self.onpick)

        # Asigno rango default a qprogressbar
        self.ui.progress_bar_ensayo.setValue(0)
        self.ui.progress_bar_ensayo.setRange(0, 100)  # Asignar rango de 0 a 100

        self.ui.samples_ant.addWidget(self.grafica)
        self.ui.fft_ant.addWidget(self.grafica2)

        self.grafica.ax.set_title("Grafico temporal")
        self.grafica2.ax.set_title("Grafico FFT")

        self.ui.notificacion.setText("Esperando configuracion")

        # Asigno metodos a cada boton
        self.ui.btn_finish.clicked.connect(self.measure.finish_test)
        self.ui.btn_init.clicked.connect(self.measure.init_ensayo)
        self.ui.btn_forzar.clicked.connect(self.measure.forzar_finish_ensayo)
        self.ui.capture.clicked.connect(self.measure.save_image)

        # Asigno metodos a cada dial
        self.ui.dial_volt_init_temp.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_volt_fin_temp.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_sample_temp.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_freq_init_fft.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_freq_fin_fft.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_amp_init_fft.valueChanged.connect(self.on_dial_value_changed)
        self.ui.dial_amp_fin_fft.valueChanged.connect(self.on_dial_value_changed)       

        # Creo contador asociado a un metodo que inicia el conteo
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        
        self.timer1.timeout.connect(self.measure.timer_ensayo)
        self.timer2.timeout.connect(self.measure.timer_standby)

        self.ui.lcd_time_ensayo.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_ant.display(f"{0:02d}.{0:02d}")

    def onpick(self, event):
        """
        Metodo asociado a evento de click sobre grafico
        """
        if self.grafica.line == event.artist:
            # Lógica para grafico
            xdata = self.grafica.line.get_xdata()
            ydata = self.grafica.line.get_ydata()
            index = event.ind[0]

            sample = xdata[index]
            volt = ydata[index]

            # Convertir la lista de cadenas a un arreglo de NumPy de floats
            data = np.array(volt, dtype=float)
            data = data * (SAMPLES_ADC / 5)

            msj = "  Volt:{:.3f}V / Data: {:.2f}\n  Sample:{:.0f}".format(volt, data, sample)
            self.ui.value_sample_ant.setText(msj)

        elif self.grafica2.line == event.artist:
            # Lógica para grafico2
            xdata = self.grafica2.line.get_xdata()
            ydata = self.grafica2.line.get_ydata()
            index = event.ind[0]

            freq = xdata[index]
            mag = ydata[index]
            msj = "  Freq={:.2f}Hz\n  Mag={:.2f}dBV".format(freq, mag)
            self.ui.value_fft_ant.setText(msj)

    def on_dial_value_changed(self, value):
        """
        Metodo para obtener valores de dials
        """
        sender = self.sender()
        if sender == self.ui.dial_sample_temp:
            self.ui.value_sample_temp.setText(f"{value}")
            self.grafica.xlim_sample_finish = round(value)
        elif sender == self.ui.dial_volt_init_temp:
            self.ui.value_volt_init_temp.setText("{:.3f}".format(value*0.005))
            self.grafica.ylim_volt_initial = value
        elif sender == self.ui.dial_volt_fin_temp:
            self.ui.value_volt_fin_temp.setText("{:.3f}".format(value*0.005))
            self.grafica.ylim_volt_finish = value
        """
        self.grafica.ax.clear()
        self.grafica.set_graph_temp_style()
        self.grafica.draw()
        """

        if sender == self.ui.dial_freq_init_fft:
            value = value *37
            self.ui.value_freq_init_fft.setText("{:.1f}".format(value))
            self.grafica2.xlim_freq_initial = round(value)
        elif sender == self.ui.dial_freq_fin_fft:
            value = value *37
            self.ui.value_freq_fin_fft.setText("{:.1f}".format(value))
            self.grafica2.xlim_freq_finish = round(value)
        elif sender == self.ui.dial_amp_init_fft:
            self.ui.value_amp_init_fft.setText("{:.1f}".format(value))
            self.grafica2.ylim_amp_initial = round(value)
        elif sender == self.ui.dial_amp_fin_fft:
            self.ui.value_amp_fin_fft.setText("{:.1f}".format(value))
            self.grafica2.ylim_amp_finish = round(value)
        """
        self.grafica2.ax.clear()
        self.grafica2.set_graph_fft_style()
        self.grafica2.draw()
        """