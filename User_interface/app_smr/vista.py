import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from matplotlib.animation import FuncAnimation

import numpy as np

from modelo import *

from Qt.win_login import *
from Qt.win_admin import *
from Qt.win_admin_rod import *
from Qt.win_user import *
from Qt.win_user_form import *
from Qt.popup_agregar_rod import *
from Qt.popup_meas_corrientes import *
from Qt.popup_time_ensayos import *
from Qt.popup_advertencia import *
from Qt.popup_error import *

SAMPLES_FFT = 512

class Grafica_fft(FigureCanvas):
    """
    Clase para dibujar grafico de fft - plots
    """
    def __init__(self, ):
        """
        Constructor de grafica fft - parametros iniciales
        """
        self.xlim_freq_initial = -1
        self.xlim_freq_finish = 19000
        self.ylim_amp_initial = -100
        self.ylim_amp_finish = 10

        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.freq_initial = np.arange(0, SAMPLES_FFT*37, 37)
        self.mag_initial = np.zeros(SAMPLES_FFT)
        
        self.set_graph_fft_style()
        # Crear la línea inicial
        self.line, = self.ax.plot(self.freq_initial, self.mag_initial, picker=5)

    def update_graph_fft(self, freq, mag):
        """
        Metodo para actualizar listas de puntos para grafico fft
        """
        self.set_graph_fft_style()

        self.line, = self.ax.plot(freq, mag, picker=5)
        self.draw()

    def set_graph_fft_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_freq_initial, self.xlim_freq_finish)
        self.ax.set_ylim(self.ylim_amp_initial, self.ylim_amp_finish)

        # Creo grilla
        step_value_fft_x = round((self.xlim_freq_finish-self.xlim_freq_initial)/20)
        step_value_fft_y = round((self.ylim_amp_finish-self.ylim_amp_initial)/10)
        for i in range(self.xlim_freq_initial, self.xlim_freq_finish, step_value_fft_x):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(self.ylim_amp_initial, self.ylim_amp_finish, step_value_fft_y):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 9
        self.ax.set_xlabel("Frecuencia[Hz]")
        self.ax.set_ylabel("Amplitud[dBV]")

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

        self.ui.input_usuario.returnPressed.connect(self.read_data)
        self.ui.input_contrasenia.returnPressed.connect(self.read_data)

        #self.file_cfg.new_file_config_ensayo() #####
        self.file_cfg.new_file_config_rod()
    def exit(self):
        self.ui.input_usuario.clear()
        self.ui.input_contrasenia.clear()
        self.close()
    
    def read_data(self):
        name = self.ui.input_usuario.text()
        pswd = self.ui.input_contrasenia.text()
        
        type_user = self.data_input.user_type(name, pswd)
        self.ui.input_usuario.clear()
        self.ui.input_contrasenia.clear()

        print(type_user)
        if type_user == "admin":
            self.windows.win_admin.show()
            self.close()
        elif type_user == "user":
            self.windows.win_user_form.show()
            self.close()
        elif type_user=="no existe":
            self.windows.popup_error.set_msj("Usuario incorrecto")
            self.windows.popup_error.exec_()
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

        self.ui.cbox_modelo_rod.currentIndexChanged.connect(self.set_parama_win_admin_rod)
        self.ui.rbtn_horario.clicked.connect(self.set_parama_win_admin_rod)
        self.ui.rbtn_antihorario.clicked.connect(self.set_parama_win_admin_rod)
        self.ui.rbtn_v300.clicked.connect(self.set_parama_win_admin_rod)
        self.ui.rbtn_v1500.clicked.connect(self.set_parama_win_admin_rod)
        self.ui.rbtn_v1800.clicked.connect(self.set_parama_win_admin_rod)

        self.ui.btn_guardar.clicked.connect(self.save_config_rod)
        self.ui.btn_reset.clicked.connect(self.reset_config)
        self.ui.btn_new_rod.clicked.connect(self.save_new_rod)

        # lee y cargo rodamientos disponibles en combobox
        self.ui.cbox_modelo_rod.addItems(self.file_cfg.read_list_rod())
        self.set_parama_win_admin_rod()

    def obtener_param_win_admin_rod(self):
        self.model_rod = self.ui.cbox_modelo_rod.currentText()
        
        if self.ui.rbtn_horario.isChecked():
            self.ui.rbtn_v300.setEnabled(True)
            self.sentido_giro = self.ui.rbtn_horario.text()
        elif self.ui.rbtn_antihorario.isChecked():
            self.ui.rbtn_v300.setEnabled(False)
            self.sentido_giro = self.ui.rbtn_antihorario.text()
            if self.ui.rbtn_v300.isChecked():
                self.ui.rbtn_v1500.setChecked(True)

        if self.ui.rbtn_v300.isChecked():
            self.velocidad = "v300"
        elif self.ui.rbtn_v1500.isChecked():
            self.velocidad = "v1500"
        elif self.ui.rbtn_v1800.isChecked():
            self.velocidad = "v1800"        

    def set_parama_win_admin_rod(self):
        self.obtener_param_win_admin_rod()

        data_rod = self.file_cfg.read_file_config(self.model_rod, self.sentido_giro, self.velocidad)

        self.ui.sbox_bpfo.setValue(int(data_rod["bpfo"]))
        self.ui.sbox_bpfi.setValue(int(data_rod["bpfi"]))
        self.ui.sbox_ftf.setValue(int(data_rod["ftf"]))
        self.ui.sbox_bsf.setValue(int(data_rod["bsf"]))

    def save_config_rod(self):
        self.obtener_param_win_admin_rod()

        new_freq_bpfo = self.ui.sbox_bpfo.value()
        new_freq_bpfi = self.ui.sbox_bpfi.value()
        new_freq_ftf = self.ui.sbox_ftf.value()
        new_freq_bsf = self.ui.sbox_bsf.value()

        self.file_cfg.update_config_rod(self.model_rod, self.sentido_giro, self.velocidad, "bpfo", new_freq_bpfo)
        self.file_cfg.update_config_rod(self.model_rod, self.sentido_giro, self.velocidad, "bpfi", new_freq_bpfi)
        self.file_cfg.update_config_rod(self.model_rod, self.sentido_giro, self.velocidad, "ftf", new_freq_ftf)
        self.file_cfg.update_config_rod(self.model_rod, self.sentido_giro, self.velocidad, "bsf", new_freq_bsf)
    
    def reset_config(self): pass
    
    def save_new_rod(self):
        self.windows.popup_agregar_rod.exec_()
        

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        self.windows.win_admin.show()

class PopupAgregarRod(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_NewRodWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_aceptar.clicked.connect(self.new_model_rod)
    
    def new_model_rod(self):
        return "Aceptar"

class WindowUserForm(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_FormUserWindow()
        self.ui.setupUi(self)
        self.windows = windows
    
        self.data_input = InputData()
        self.file_cfg = CfgFileManager()

        self.ui.btn_reset.clicked.connect(self.clear_data)
        self.ui.btn_ingresar.clicked.connect(self.ingresar)

    def clear_data(self):
        self.ui.input_operario.clear()
        self.ui.input_legajo.clear()
        self.ui.input_formacion.clear()
        self.ui.input_coche.clear()
        self.ui.input_boguie.clear()
        self.ui.input_motor.clear()  
        self.ui.cbox_fase_tierra.setCurrentIndex(-1)
        self.ui.cbox_rod_tierra.setCurrentIndex(-1)

    def ingresar(self):
        state_entries = self.obtener_param_form()
        self.update_data_form()

        if state_entries == "Todo completo":
            self.windows.win_user.show()
            self.hide()
        elif state_entries == "No completo algunos campos":
            self.windows.popup_advertencia.set_msj("No completo todos los campos, \n¿Desea continuar?")
            self.windows.popup_advertencia.exec_()
        elif state_entries == "No completo campos operario, ni legajo":
            self.windows.popup_error.set_msj("Los siguientes campos son obligatorios:\nOperario y Legajo")
            self.windows.popup_error.exec_()

    def obtener_param_form(self):
        # SUGERENCIA: se deberia crear archivo temporal para guardar datos de operario y motor
        self.data_ensayo = self.file_cfg.read_file_config_ensayo("UltimoEnsayo")        
        self.operario = self.ui.input_operario.text()
        self.legajo = self.ui.input_legajo.text()
        self.formacion = self.ui.input_formacion.text()
        self.coche = self.ui.input_coche.text()
        self.boguie = self.ui.input_boguie.text()
        self.motor = self.ui.input_motor.text()
        self.rod_ant = self.data_ensayo["RodamientoAnterior"]
        self.rod_pos = self.data_ensayo["RodamientoPosterior"]
        self.fase_tierra = self.ui.cbox_fase_tierra.currentText()
        self.rod_tierra = self.ui.cbox_rod_tierra.currentText()

        if  self.check_entry_empty(self.operario) or \
            self.check_entry_empty(self.legajo):
            return "No completo campos operario, ni legajo"
        
        elif self.check_entry_empty(self.formacion) or \
            self.check_entry_empty(self.coche) or \
            self.check_entry_empty(self.boguie) or \
            self.check_entry_empty(self.motor) or \
            self.check_entry_empty(self.fase_tierra) or \
            self.check_entry_empty(self.rod_tierra):
            return "No completo algunos campos"
        
        else:
            return "Todo completo"

    def check_entry_empty(self, entry):
        if entry == "":
            return 1
        else:
            return 0
    
    def update_data_form(self):
        self.windows.win_user.ui.label_operario.setText(self.operario)
        self.windows.win_user.ui.label_legajo.setText(self.legajo)
        self.windows.win_user.ui.label_formacion.setText(self.formacion)
        self.windows.win_user.ui.label_coche.setText(self.coche)
        self.windows.win_user.ui.label_boguie.setText(self.boguie)
        self.windows.win_user.ui.label_motor.setText(self.motor)
        self.windows.win_user.ui.label_modelo_rod_ant.setText(self.rod_ant)
        self.windows.win_user.ui.label_modelo_rod_pos.setText(self.rod_pos)       
        self.windows.win_user.ui.label_fase_tierra.setText(self.fase_tierra)
        self.windows.win_user.ui.label_rod_tierra.setText(self.rod_tierra)


    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        if not self.windows.win_user.isVisible():
            self.windows.win_login.show()
        else:
            event.ignore()

class WindowUser(QMainWindow):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.grafica = Grafica_fft()
        self.grafica2 = Grafica_fft()

        self.measure = Measure(self)

        self.ui.fft_ant.addWidget(self.grafica)
        self.ui.fft_pos.addWidget(self.grafica2)

        self.grafica.ax.set_title("Grafico Rodamiento Anterior")
        self.grafica2.ax.set_title("Grafico Rodamiento Posterior")

        self.ui.btn_iniciar.clicked.connect(self.measure.init_ensayo)
        self.ui.btn_finalizar.clicked.connect(self.measure.stop_ensayo)
        self.ui.btn_config_data.clicked.connect(self.config_data)
        self.ui.btn_ver_ensayos.clicked.connect(self.ver_ensayos)

        self.ui.btn_finalizar.setEnabled(False)
        self.ui.btn_ver_ensayos.setEnabled(False)

        # Creo contador asociado a un metodo que inicia el conteo
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.measure.timer_ensayo)

        self.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        self.ui.lcd_temp_amb.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_ant.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_temp_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_axial_pos.display(f"{0:02d}.{0:02d}")
        self.ui.lcd_radial_pos.display(f"{0:02d}.{0:02d}")

    def config_data(self):
        self.windows.win_user_form.exec_()

    def ver_ensayos(self):
        self.windows.popup_time_ensayos.exec_()

    def closeEvent(self, event):
        """
        Evento cierre window de barra default qt
        """
        self.windows.win_login.show()

class PopupMeasCorrientes(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_MeasCorrientesWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_aceptar.clicked.connect(self.finish_data_ensayo)

    def finish_data_ensayo(self):
        self.fase_u = self.ui.input_fase_u.text()
        self.fase_v = self.ui.input_fase_v.text()
        self.fase_w = self.ui.input_fase_w.text()

        if self.check_entry_empty(self.fase_u) or \
            self.check_entry_empty(self.fase_v) or \
            self.check_entry_empty(self.fase_w):
            print("DEBE COMPLETAR LOS CAMPOS")
        else:
            print("FINALIZO ENSAYO")
            self.hide()
        
        self.windows.win_user.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}")
        self.windows.win_user.measure.seconds = 0
        self.windows.win_user.measure.minutes = 0
        

    def check_entry_empty(self, entry):
        if entry == "":
            return 1
        else:
            return 0

    def closeEvent(self, event):
        event.ignore()

class PopupTimeEnsayos(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_TimeEnsayosWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.btn_ok.clicked.connect(self.close)

    def set_time(self, num_ensayo, minutes, seconds):

        if num_ensayo == "1":
            self.ui.time_ensayo1.setText(f"{minutes:02d}:{seconds:02d}")
        elif num_ensayo == "2":
            self.ui.time_ensayo2.setText(f"{minutes:02d}:{seconds:02d}")
        elif num_ensayo == "3":
            self.ui.time_ensayo3.setText(f"{minutes:02d}:{seconds:02d}")
        elif num_ensayo == "4":
            self.ui.time_ensayo4.setText(f"{minutes:02d}:{seconds:02d}")
        elif num_ensayo == "5":
            self.ui.time_ensayo5.setText(f"{minutes:02d}:{seconds:02d}")
        elif num_ensayo == "reset":
            self.ui.time_ensayo1.setText("en proceso")
            self.ui.time_ensayo2.setText("en proceso")   
            self.ui.time_ensayo3.setText("en proceso")
            self.ui.time_ensayo4.setText("en proceso")   
            self.ui.time_ensayo5.setText("en proceso")

class PopupAdvertencia(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_AdvertenciaWindow()
        self.ui.setupUi(self)
        self.windows = windows
    
        self.ui.icon.setPixmap(QPixmap("iconos/advertencia.png"))

        self.ui.btn_aceptar.clicked.connect(self.continuar)
        self.ui.btn_cancelar.clicked.connect(self.return_form_user)

    def set_msj(self, msj):
        self.ui.label.setText(msj) 

    def continuar(self):
        self.windows.win_user.show()
        self.windows.win_user_form.hide()
        self.close()

    def return_form_user(self):
        self.close()

class PopupError(QDialog):
    def __init__(self, windows):
        super().__init__() 
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)
        self.windows = windows

        self.ui.icon.setPixmap(QPixmap("iconos/incorrecto.png"))

        self.ui.btn_ok.clicked.connect(self.return_form_user)

    def set_msj(self,msj):
        self.ui.label.setText(msj)        

    def return_form_user(self):
        #self.windows.win_user_form.show()
        self.close()



