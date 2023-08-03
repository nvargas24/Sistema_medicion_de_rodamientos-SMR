import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from vista import *
from modelo import *

class Controlador():
    def __init__(self, ):
        # se deben crear las clases que interactuan con los .ui en vista.py
        #self.option = Option()
        # Creo ventanas

        self.window_login = WindowLogin(self) # Esta ventana es secundaria por lo tanto se debe decir cuando se muestra
        # Una tiene que ser mostrada apenas se abre la app, las demas al realizar alguna accion como hace un click en un boton
        # Paso el objeto controlador para poder acceder a los metodos de MainWindow --> mostrar ventana        
        self.window_main = Mainwindow(self) # Esta ventana ya se define como principala pero se debe asignar cuando se muestra
        self.window_login.show() # Muestra la ventana de login
        try:
            print("Abro menu de app_stock")            
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro menu de app_stock")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Creao objeto controlador 
    obj_controlador = Controlador()

