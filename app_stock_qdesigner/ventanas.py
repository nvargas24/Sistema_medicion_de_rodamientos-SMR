import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from agregar import *
from eliminar import *
from modificar import *
from consulta import *

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
