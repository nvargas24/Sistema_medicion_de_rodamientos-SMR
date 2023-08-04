import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from modelo import *

from Qt.win_login import *
from Qt.win_admin import *
from Qt.win_user import *
from Qt.win_user_form import *
from Qt.popup_agregar_rod import *

class WindowLogin(QWidget):
    def __init__(self, windows):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.windows = windows
    
        self.data_input = InputData()

        self.ui.btn_aceptar.clicked.connect(self.read_data)
        self.ui.btn_salir.clicked.connect(self.exit)

    def exit(self):
        self.ui.input_usuario.clear()
        self.ui.input_contrasenia.clear()
        self.close()
    
    def read_data(self):
        name = self.ui.input_usuario.text()
        pswd = self.ui.input_contrasenia.text()
        
        type = self.data_input.user_type(name, pswd)

        if type == "admin":
            self.windows.win_admin.show()
            self.close()
        elif type == "user":
            self.windows.win_user.show()
            self.close()
        else:
            self.ui.input_usuario.clear()
            self.ui.input_contrasenia.clear()
            # MOstrar anuncio de ususario no valido, capaz como popup

class WindowAdmin(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.windows = windows

class WindowUser(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)
        self.windows = windows

class WindowUserForm(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_FormUserWindow()
        self.ui.setupUi(self)
        self.windows = windows

class PopupAgregarRod(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_NewRodWindow()
        self.ui.setupUi(self)
        self.windows = windows



