import sys
from PySide2 import QtWidgets, QtGui, QtCore
from OpenGL.GL import *
import numpy as np

class OpenGLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800, 600)  # Ajusta el tamaño mínimo
        self.angle = 0
        self.rotating = False
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.rotate)
        self.timer.start(1000)  # Intervalo de tiempo para la rotación

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
        glRotatef(self.angle, 1, 0, 0)  # Rotación sobre el eje XY

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

    def rotate(self):
        if self.rotating:
            print(self.angle)
            self.angle += 10
            self.angle %= 360  # Asegurarse de que el ángulo no exceda 360 grados
            self.update()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.opengl_widget = OpenGLWidget(self.central_widget)
        layout.addWidget(self.opengl_widget)

        self.rotating_button = QtWidgets.QPushButton("Rotar", self.central_widget)
        layout.addWidget(self.rotating_button)

        self.rotating_button.clicked.connect(self.toggle_rotation)

    def toggle_rotation(self):
        self.opengl_widget.rotating = not self.opengl_widget.rotating

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
