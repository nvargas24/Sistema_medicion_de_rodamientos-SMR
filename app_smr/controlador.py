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
        # Creo ventanas
        self.win_login = WindowLogin(self)
        self.win_admin = WindowAdmin(self)
        self.win_user = WindowUser(self)
        self.win_user_form = WindowUserForm(self)
        self.popup_agregar_rod = PopupAgregarRod(self)
        
        self.win_login.show()
        try:
            print("Abro menu de app_stock")            
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro menu de app_stock")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Creao objeto controlador 
    obj_controlador = Controlador()

