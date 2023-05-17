import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from Qt.App_nota_de_servicio import *
from modelo import *

class MainWindow(QMainWindow):
    def __init__ (self, ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        obj_solicitud = DatosSolicitud(self.ui)

class DatosSolicitud():
    def __init__(self, ui):
        self.ui = ui
        self.obj_crud = Crud()
        self.set()

    def set(self, ):
        # Inicializacion
        self.ui.guardar_pdf.clicked.connect(lambda: self.obj_crud.get(self.ui))
        # Seteo por indice valor inicial
        self.ui.tipo_servicio.setCurrentIndex(1) # Se selecciona item por indice
        self.ui.nom_sector.setCurrentIndex(4)
        self.ui.num_formacion.setCurrentIndex(0)
        self.ui.num_coche.setCurrentIndex(0)

class DescripcionOperacion():
    def set(self, ): pass

class Verificacion():
    def set(self, ): pass

class DatosOperador():
    def set(self, ): pass

class CierreSolicitud():
    def guardar(self, ): pass
    def imprimir(self, ): pass

