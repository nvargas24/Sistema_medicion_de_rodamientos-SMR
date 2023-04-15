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
        self.ui.btns_option.accepted.connect(self.new_load)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def new_load(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()    

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guarda nuevo articulo")
    
class WindowEliminar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.delete)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def delete(self,):
        nombre=str(self.ui.in_nombre.text())
        self.ui.in_nombre.clear()

        print(nombre)
        self.exit()
        print("Se elimino articulo")

class WindowModificar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.modificated)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def modificated(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()    

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guardo modificaciones")

class WindowConsulta(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)
        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.exit)

    def exit(self, ):
        self.close()
        print("Regresa a menu principal")
    
    def search(self, ):
        print("Busca articulo")
    
    def full_cat(self, ):
        print("Muestra catalogo completo")
