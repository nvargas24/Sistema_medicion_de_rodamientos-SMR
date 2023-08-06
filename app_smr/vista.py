import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from modelo import *

from Qt.win_login import *
from Qt.win_admin import *
from Qt.win_admin_rod import *
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
        self.file_cfg = CfgFileManager() # VER SI SE BORRA

        self.ui.btn_aceptar.clicked.connect(self.read_data)
        self.ui.btn_salir.clicked.connect(self.exit)

        #self.file_cfg.new_file_config_ensayo() #####

    def exit(self):
        self.ui.input_usuario.clear()
        self.ui.input_contrasenia.clear()
        self.close()
    
    def read_data(self):
        name = self.ui.input_usuario.text()
        pswd = self.ui.input_contrasenia.text()
        
        type = self.data_input.user_type(name, pswd)
        self.ui.input_usuario.clear()
        self.ui.input_contrasenia.clear()

        if type == "admin":
            self.windows.win_admin.show()
            self.close()
        elif type == "user":
            self.windows.win_user_form.show()
            self.close()
        else:
            print("No existe el usuario")
            # MOstrar anuncio de usuario no valido, capaz como popup


class WindowAdmin(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.file_cfg = CfgFileManager()

        # lee y cargo rodamientos disponibles en combobox
        self.ui.cbox_modelo_rod_ant.addItems(self.file_cfg.read_list_rod())
        self.ui.cbox_modelo_rod_pos.addItems(self.file_cfg.read_list_rod())

        self.ui.btn_guardar.clicked.connect(self.save_config)
        self.ui.btn_reset.clicked.connect(self.reset_config)
        self.ui.btn_edit_rod.clicked.connect(self.edit_rod)

        self.set_param_win_admin("UltimoEnsayo")

    def set_param_win_admin(self, ensayo):
        """
        Metodo para setear valores de formulario
        """
        self.data_ensayo=self.file_cfg.read_file_config_ensayo(ensayo)

        self.ui.cbox_modelo_rod_ant.setCurrentText(self.data_ensayo["RodamientoAnterior"])
        self.ui.cbox_modelo_rod_pos.setCurrentText(self.data_ensayo["RodamientoPosterior"])
        self.ui.sbox_temp_max.setValue(int(self.data_ensayo["TemperaturaMax"]))
        self.ui.sbox_temp_min.setValue(int(self.data_ensayo["TemperaturaMin"]))
        self.ui.sbox_axial_max.setValue(float(self.data_ensayo["VibracionAxialMax"]))
        self.ui.sbox_radial_max.setValue(float(self.data_ensayo["VibracionRadialMax"]))


    def save_config(self):
        rod_ant = self.ui.cbox_modelo_rod_ant.currentText()
        rod_pos = self.ui.cbox_modelo_rod_pos.currentText()
        temp_max = self.ui.sbox_temp_max.value()
        temp_min = self.ui.sbox_temp_min.value()
        axial_max = self.ui.sbox_axial_max.value()
        radial_max = self.ui.sbox_radial_max.value()
        
        self.file_cfg.update_config_ensayo("RodamientoAnterior", rod_ant)
        self.file_cfg.update_config_ensayo("RodamientoPosterior", rod_pos)
        self.file_cfg.update_config_ensayo("TemperaturaMax", temp_max)
        self.file_cfg.update_config_ensayo("TemperaturaMin", temp_min)
        self.file_cfg.update_config_ensayo("VibracionAxialMax", axial_max)
        self.file_cfg.update_config_ensayo("VibracionRadialMax", radial_max)
        print("Se modifica configuracion de ensayo")

    def reset_config(self):
        self.set_param_win_admin("EnsayoDefault")

    def edit_rod(self):
        self.file_cfg.read_list_rod()
        self.windows.win_rod.show()
        self.hide()

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        self.windows.win_login.show()

class WindowRod(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_RodWindow()
        self.ui.setupUi(self)
        self.windows = windows
        self.file_cfg = CfgFileManager()

        self.ui.cbox_modelo_rod.currentIndexChanged.connect(self.obtener_parametros)
        self.ui.rbtn_horario.clicked.connect(self.obtener_parametros)
        self.ui.rbtn_antihorario.clicked.connect(self.obtener_parametros)
        self.ui.rbtn_v300.clicked.connect(self.obtener_parametros)
        self.ui.rbtn_v1500.clicked.connect(self.obtener_parametros)
        self.ui.rbtn_v1800.clicked.connect(self.obtener_parametros)

        self.ui.btn_guardar.clicked.connect(self.save_config_rod)
        self.ui.btn_reset.clicked.connect(self.reset_config)
        self.ui.btn_new_rod.clicked.connect(self.save_new_rod)

        # lee y cargo rodamientos disponibles en combobox
        self.ui.cbox_modelo_rod.addItems(self.file_cfg.read_list_rod())
        self.obtener_parametros()

    def obtener_parametros(self):
        model_rod = self.ui.cbox_modelo_rod.currentText()
        
        if self.ui.rbtn_horario.isChecked():
            self.ui.rbtn_v300.setEnabled(True)
            sentido_giro = self.ui.rbtn_horario.text()
        elif self.ui.rbtn_antihorario.isChecked():
            self.ui.rbtn_v300.setEnabled(False)
            sentido_giro = self.ui.rbtn_antihorario.text()
            if self.ui.rbtn_v300.isChecked():
                self.ui.rbtn_v1500.setChecked(True)

        if self.ui.rbtn_v300.isChecked():
            velocidad = self.ui.rbtn_v300.text()
        elif self.ui.rbtn_v1500.isChecked():
            velocidad = self.ui.rbtn_v1500.text()
        elif self.ui.rbtn_v1800.isChecked():
            velocidad = self.ui.rbtn_v1800.text()


        print(model_rod)
        print(sentido_giro)        
        print(velocidad)


    def save_config_rod(self):
        self.obtener_parametros()
    def reset_config(self): pass
    def save_new_rod(self): pass

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        self.windows.win_admin.show()


class WindowUserForm(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_FormUserWindow()
        self.ui.setupUi(self)
        self.windows = windows
    
        self.data_input = InputData()

        self.ui.btn_reset.clicked.connect(self.clear_data)
        self.ui.btn_ingresar.clicked.connect(self.ingresar)

    def clear_data(self): pass
    def ingresar(self):
    # se deberia crear archivo temporal para guardar datos de operario y motor
        self.windows.win_user.show()
        self.hide()

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        if not self.windows.win_user.isVisible():
            self.windows.win_login.show()

class WindowUser(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_iniciar.clicked.connect(self.init_ensayo)
        self.ui.btn_finalizar.clicked.connect(self.stop_ensayo)
        self.ui.btn_config_data.clicked.connect(self.config_data)

    def init_ensayo(self): pass
    def stop_ensayo(self): pass
    def config_data(self):
        self.windows.win_user_form.show()

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        self.windows.win_login.show()

class PopupAgregarRod(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_NewRodWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_aceptar.clicked.connect(self.new_model_rod)
    
    def new_model_rod(self): pass


