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
import chainsawman_rc
# Hay que tener en cuenta la clase definida en el qtdesigner de cada ventana
# Para la ventana principal siempre es QMainWindow, esto se asigna cuando se crea la ventana en QtDesigner
class Mainwindow(QMainWindow):
    def __init__(self, windows):
        super().__init__() # Accedo constructor de QMainWindwow, por si se cambia de nombre es mejor utilizar super()
        self.ui = Ui_MainWindow() # Instancio la ventana main esta clase esta defnida en .py del .ui
        self.ui.setupUi(self) # Se pasa objeto de la clase MainWindow asi se
                              # se identifica el espacio de trabajo
                              # En el archivo window_main.py se puede ver el nombre que se lo 
                              # identifica al objeto, esto se puede modificar en QtDesigner
        self.windows = windows # Parametro para acceder a los metodos del modelo, en este caso de la clase Option
        self.ui.usuario.setText("Lab")  # se debe utilizar un observador para no tener problemas al cerrar la ventana login y quede registrado el nomnbre
        # Ahora puedo acceder a los metodos de cada widget

        self.ui.image.setPixmap(QPixmap(":/chainsawman.jpeg"))
        self.ui.image.setScaledContents(True)

        self.ui.btn_aceptar.clicked.connect(lambda: self.windows.option.url_op(self))
        self.ui.btn_menu.clicked.connect(self.exit)
    
    def exit(self, ):
        self.windows.window_login.show()
        # Limpio celdas 
        self.windows.window_login.ui.usuario.clear()
        self.windows.window_login.ui.contrasenia.clear()
        self.close()


# Se debe asignar la clase padre QWidget o QForm para ventanas secundarias, esto se configura en QtDesigner
class WindowLogin(QWidget):
    def __init__(self, windows):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.windows = windows # Accedo a metodos de ventana principal por medio del objeto controlador
         # Ahora puedo acceder a los metodos de cada widget creado por medio del objeto self .ui       
        self.ui.btn_aceptar.clicked.connect(lambda: self.windows.option.input_user(self)) # En este caso necesito acceder a self.ui y a self.parent, 
                                                                                                # para obtener datos de Qline y mostrar ventana principal, respectivamente
        self.ui.btn_salir.clicked.connect(self.close)


