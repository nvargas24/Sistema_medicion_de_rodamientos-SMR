"""
 IMPORTANTE: 
    NO SE DEBEN MODIFICAR LOS ARCHIVOS DE LA CARPETA QT, YA QUE ESTO UNICAMENTE SE
 MODIFICAN DESDE LA APP QTDESIGNER, SINO AL REALIZAR UN MINIMO CAMBIO EN QTDESIGNER,
 EL CODIGO ESCRITO SE BORRARA. SI SE QUIERE HACER ALGUN CAMBIO POR CODIGO, SE REALIZAN 
 ACA QUE INTERACTURA CON LAS CLASES Y METODOS DE OBTENIDOS CON PYSIDE2 DE LOS .UI
"""
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

# Se importa libreria de archivos .py creados con pyside2 de un .ui
# Necesario para acceder a las clases y metodos de cada widget en .ui
from Qt.window_main import *
from Qt.window_login import *

# Hay que tener en cuenta la clase definida en el qtdesigner de cada ventana
# Esto se puede editar en QtDesigner
class Mainwindwow(QMainWindow):
    def __init__(self, ):
        super().__init__() # Accedo constructor de QMainWindwow, por si se cambia de nombre es mejor utilizar super()
        self.ui = Ui_MainWindow() # Instancio la ventana main esta clase esta defnida en .py del .ui
        self.ui.setupUi(self) # Se pasa objeto de la clase MainWindow asi se
                              # se identifica el espacio de trabajo
                              # En el archivo window_main.py se puede ver el nombre que se lo 
                              # identifica al objeto, esto se puede modificar en QtDesigner
        # Ahora puedo acceder a los metodos de cada widget creado por medio del objeto self .ui

class UsuarioWindow():
    def __init__(self, ):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
         # Ahora puedo acceder a los metodos de cada widget creado por medio del objeto self .ui       




