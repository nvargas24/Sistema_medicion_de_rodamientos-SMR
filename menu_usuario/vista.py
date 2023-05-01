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
class Mainwindow(QMainWindow):
    def __init__(self, ):
        super().__init__() # Accedo constructor de QMainWindwow, por si se cambia de nombre es mejor utilizar super()
        self.ui = Ui_MainWindow() # Instancio la ventana main esta clase esta defnida en .py del .ui
        self.ui.setupUi(self) # Se pasa objeto de la clase MainWindow asi se
                              # se identifica el espacio de trabajo
                              # En el archivo window_main.py se puede ver el nombre que se lo 
                              # identifica al objeto, esto se puede modificar en QtDesigner
        # Ahora puedo acceder a los metodos de cada widget creado por medio del objeto self .ui
        self.ui.btn_aceptar.clicked.connect(self.url_op)

    # --- Metodos que se accede al hacer click ---#
    def url_op(self, ):
        print("Esta en ventana principal")
        self.selecct = self.ui.comboBox_seleccion.currentText() # Para obtener valor seleccionado en combobox

class WindowLogin():
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.parent = parent # Accedo a metodos de ventana principal por medio del objeto controlador
         # Ahora puedo acceder a los metodos de cada widget creado por medio del objeto self .ui       
        self.ui.btn_aceptar.clicked.connect(self.input_user)
        self.ui.btn_aceptar.clicked.connect(self.close)
    
    # --- Metodos que accede al hacer click --#
    def input_user(self, ):
        # Se debe tomar los datos y si coinciden con los de usuarios se puede acceder a MainWindow
        self.parent.window_main.show()



