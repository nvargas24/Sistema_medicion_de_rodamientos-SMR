import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from app_stock import *
from ventanas import *

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

class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent=None):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets

        self.ui.btn_agregar.clicked.connect(self.agregar_dat)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_dat)
        self.ui.btn_modificar.clicked.connect(self.modificar_dat)
        self.ui.btn_consultar.clicked.connect(self.consultar_dat)

        self.window_agregar = WindowAgregar()
        self.window_eliminar = WindowEliminar()
        self.window_modificar = WindowModificar()
        self.window_consulta = WindowConsulta() 
        
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
