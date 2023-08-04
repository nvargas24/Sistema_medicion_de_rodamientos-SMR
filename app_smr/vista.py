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
            self.windows.win_user_form.show()
            self.close()
        else:
            self.ui.input_usuario.clear()
            self.ui.input_contrasenia.clear()
            # MOstrar anuncio de usuario no valido, capaz como popup

class WindowAdmin(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.cbox_modelo_rod_ant.activated.connect(self.select_rod)
        self.ui.cbox_modelo_rod_pos.activated.connect(self.select_rod)

        self.ui.btn_guardar_ant.clicked.connect(self.save_config_rod)
        self.ui.btn_guardar_pos.clicked.connect(self.save_config_rod)

        self.ui.btn_reset_ant.clicked.connect(self.reset_config)
        self.ui.btn_reset_pos.clicked.connect(self.reset_config)

        self.ui.btn_new_rod_ant.clicked.connect(self.save_new_rod)
        self.ui.btn_new_rod_pos.clicked.connect(self.save_new_rod)

    def save_config_rod(self): pass
    def reset_config(self): pass
    def save_new_rod(self): pass
    def select_rod(self): pass

class WindowUserForm(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_FormUserWindow()
        self.ui.setupUi(self)
        self.windows = windows
    
        self.data_input = InputData()

        self.ui.btn_volver.clicked.connect(self.volver_login)
        self.ui.btn_reset.clicked.connect(self.clear_data)
        self.ui.btn_ingresar.clicked.connect(self.show_win_user)

    def volver_login(self): pass
    def clear_data(self): pass
    def show_win_user(self): pass
    # se deberia crear archivo temporal para guardar datos de operario y motor

class WindowUser(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_iniciar.clicked.connect(self.init_ensayo)
        self.ui.btn_finalizar.clicked.connect(self.stop_ensayo)

    def init_ensayo(self): pass
    def stop_ensayo(self): pass

class PopupAgregarRod(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_NewRodWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_aceptar.clicked.connect(self.new_model_rod)
    
    def new_model_rod(self): pass


