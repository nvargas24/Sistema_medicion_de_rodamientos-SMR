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
from OpenGL.GL import *

import numpy as np
from main import *
from modelo import *

class GraficaPieza3D(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.new_angle_x = 0
        self.new_angle_y = 0
        self.new_angle_z = 0

    def initializeGL(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)

        self.vertices = np.array([
            (-0.1, -3.0, -2.0),  # Vértice 0 (trasero, izquierda, abajo)
            (0.1, -3.0, -2.0),   # Vértice 1 (trasero, derecha, abajo)
            (0.1, 3.0, -2.0),    # Vértice 2 (trasero, derecha, arriba)
            (-0.1, 3.0, -2.0),   # Vértice 3 (trasero, izquierda, arriba)
            (-0.1, -3.0, 2.0),   # Vértice 4 (delantero, izquierda, abajo)
            (0.1, -3.0, 2.0),    # Vértice 5 (delantero, derecha, abajo)
            (0.1, 3.0, 2.0),     # Vértice 6 (delantero, derecha, arriba)
            (-0.1, 3.0, 2.0)     # Vértice 7 (delantero, izquierda, arriba)
        ], dtype=np.float32)

        self.faces = np.array([
            (0, 1, 5, 4),  # Cara trasera
            (1, 2, 6, 5),  # Cara derecha
            (2, 3, 7, 6),  # Cara frontal
            (3, 0, 4, 7),  # Cara izquierda
            (4, 5, 6, 7),   # Cara superior
            (3, 2, 1, 0)   # Cara inferior
        ], dtype=np.uint32)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-8, 8, -8, 8, -20, 20)  # Ajusta los valores para obtener la vista deseada
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(80, 0, 1, -1)  # Rotación para la vista de caballera
        glTranslatef(0.0, 0.0, 0.0)  # Ajusta la posición de la cámara para ver el cubo completo

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar el prisma rectangular (cubo)
        glPushMatrix()
        glRotatef(self.new_angle_x, 1, 0, 0)  # Rotación sobre el eje XY
        glRotatef(self.new_angle_y, 0, 1, 0)  # Rotación sobre el eje XY
        glRotatef(self.new_angle_z, 0, 0, 1)  # Rotación sobre el eje XY

        # Dibuja las caras del cubo
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        
        # Configura el color del cuerpo del cubo (gris claro)
        glColor3f(0.7, 0.7, 0.7)
        glDrawElements(GL_QUADS, len(self.faces) * 4, GL_UNSIGNED_INT, self.faces)
        
        # Configura el color de las aristas (negro)
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(1.0)  # Grosor de las líneas
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # Modo de dibujo de aristas
        glEnable(GL_POLYGON_OFFSET_LINE)
        glPolygonOffset(-1, -1)  # Ajusta la separación entre las aristas y las caras
        glDrawElements(GL_QUADS, len(self.faces) * 4, GL_UNSIGNED_INT, self.faces)
        glDisable(GL_POLYGON_OFFSET_LINE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Vuelve al modo de dibujo de caras llenas
        
        glDisableClientState(GL_VERTEX_ARRAY)

        glPopMatrix()

        #self.swapBuffers()


class GraficaFFT(FigureCanvas):
    """
    Clase para dibujar grafico de fft - plots
    """
    def __init__(self, ):
        """
        Constructor de grafica fft - parametros iniciales
        """
        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.freq_initial = np.arange(0, 512*37, 37)
        self.mag_initial = np.zeros(512)

        self.set_graph_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.freq_initial, self.mag_initial, picker=5)

    def upgrade_fft(self, freq, mag):
        """
        Metodo para actualizar listas de puntos para grafico fft
        """
        self.set_graph_style()

        self.line, = self.ax.plot(freq, mag, picker=5)
        self.draw()

    def set_graph_style(self):
        """
        Metodo que asigna estilo al grafico
        """
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
        self.grafica = GraficaFFT()
        self.grafica2 = GraficaPieza3D()

        self.measure = Measure(self)

        # Registrar el manejador de eventos de click del ratón sobre grafico
        self.grafica.fig.canvas.mpl_connect('pick_event', self.onpick)

        self.ui.graph.addWidget(self.grafica)
        self.ui.graph2.addWidget(self.grafica2)

        self.grafica.ax.set_title("FFT de acelerometro")
        self.ui.label_notificacion.setText("Esperando configuracion")

        # Asigno metodos a cada boton
        ## Uso lambda para poder a acceder a ui desde el modelo
        self.ui.btn_finish.clicked.connect(self.measure.finish_test)
        self.ui.btn_init.clicked.connect(self.measure.init_ensayo)

        # Creo contador asociado a un metodo que inicia el conteo
        self.timer1 = QTimer(self)
     
        self.timer1.timeout.connect(self.measure.timer_ensayo)
 
        self.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}:{0:02d}")

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