import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

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



