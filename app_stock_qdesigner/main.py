import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

# ===========================================================
from app_stock import *

from agregar import *
from eliminar import *
from modificar import *
from consulta import *

class Opciones():
    def agregar_dat(self,):
        print("agregar articulo nuevo")
        self.window_agregar.setWindowTitle("Agregar")
        self.window_agregar.show()

    def eliminar_dat(self,):
        print("eliminar articulo")
        self.window_eliminar.setWindowTitle("Eliminar")
        self.window_eliminar.show()

    def modificar_dat(self,):
        print("modificar articulo")
        self.window_modificar.setWindowTitle("Modificar")
        self.window_modificar.show()

    def consultar_dat(self,):
        print("consultar articulo")
        self.window_consulta.setWindowTitle("Consulta")
        self.window_consulta.show()

class WindowAgregar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self,)

class WindowEliminar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)

class WindowModificar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)

class WindowConsulta(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)

class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent=None):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets

        self.ui.agregar.clicked.connect(self.agregar_dat)
        self.ui.eliminar.clicked.connect(self.eliminar_dat)
        self.ui.modificar.clicked.connect(self.modificar_dat)
        self.ui.consultar.clicked.connect(self.consultar_dat)

        self.window_agregar = WindowAgregar()
        self.window_eliminar = WindowEliminar()
        self.window_modificar = WindowModificar()
        self.window_consulta = WindowConsulta() 

        """ Se debe crear el objeto en la ventana principal, sino da la impresion que se cierra al crearlo en un metodo
        esto debido a que el boton al hacer click, instaneamente se deselecciona, dando a mal entender que se realizo
        otro click ocultando la primera. Para evitar depender de los click sea crea el objeto fuera del metodo y con self
        se lo llama. """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
    window = MainWindow() # Creo objeto de la clase MainWindow

    # Los metodos utilizados son los heredados de la clase QMainWindow
    window.setWindowTitle("App Stock")
    window.show()

    try:
        sys.exit(app.exec_())    # Mantiene abierta la app
    except SystemExit:
        print("Cierro menu de app_stock")
