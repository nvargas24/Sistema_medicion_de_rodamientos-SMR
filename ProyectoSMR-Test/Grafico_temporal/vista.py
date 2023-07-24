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
        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        # ver en programa de sensor, num de muestrar para realizar grafico y num de data 
        self.samples_initial = np.arange(0, 1024, 1)
        self.volt_initial = np.zeros(1024) # ver resolucion de adc 

        self.set_graph_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.samples_initial, self.volt_initial, picker=5)

    def upgrade_graph(self, samples, volt):
        """
        Metodo para actualizar listas de puntos para grafico
        """
        self.set_graph_style()

        self.line, = self.ax.plot(samples, volt, picker=5)
        self.draw()

    def set_graph_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Establecer límites del eje X e Y
        self.ax.set_xlim(-1, 1025)
        self.ax.set_ylim(-.1, 1)

        # Creo grilla
        for i in range(0, 1024, 64):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(-1, 10, 1):   
            self.ax.axhline(j*0.1, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Samples[#]")
        self.ax.set_ylabel("Volt[V]")


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
        self.grafica2 = Grafica_samples()

        self.measure = Measure(self)

        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica.fig.canvas.mpl_connect('pick_event', self.onpick)
        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica2.fig.canvas.mpl_connect('pick_event', self.onpick)

        # Asigno rango default a qprogressbar
        self.ui.progress_bar_ensayo.setValue(0)
        self.ui.progress_bar_ensayo.setRange(0, 100)  # Asignar rango de 0 a 100

        self.ui.samples_ant.addWidget(self.grafica)
        self.ui.samples_pos.addWidget(self.grafica2)

        self.grafica.ax.set_title("Rodamiento anterior")
        self.grafica2.ax.set_title("Rodamiento posterior")

        self.ui.notificacion.setText("Esperando configuracion")

        # Asigno metodos a cada boton
        ## Uso lambda para poder a acceder a ui desde el modelo
        self.ui.btn_finish.clicked.connect(self.measure.finish_test)
        self.ui.btn_init.clicked.connect(self.measure.init_ensayo)
        self.ui.btn_forzar.clicked.connect(self.measure.forzar_finish_ensayo)
        self.ui.capture.clicked.connect(self.measure.save_image)

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
            msj = "  Volt:{:.5f} V\n  Sample:{:.0f}".format(volt, sample)
            self.ui.value_sample_ant.setText(msj)

        elif self.grafica2.line == event.artist:
            # Lógica para grafico2
            xdata = self.grafica2.line.get_xdata()
            ydata = self.grafica2.line.get_ydata()
            index = event.ind[0]

            sample = xdata[index]
            volt = ydata[index]
            msj = "  Volt:{:.5f} V\n  Sample:{:.0f}".format(volt, sample)
            self.ui.value_sample_pos.setText(msj)