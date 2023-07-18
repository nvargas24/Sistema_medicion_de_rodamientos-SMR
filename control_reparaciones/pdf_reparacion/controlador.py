import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
from vista import *

class Controlador():
    def __init__(self, ):
        self.window_main = MainWindow()
        self.window_main.setWindowTitle("Nota de servicio")
        self.window_main.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj_controlador = Controlador()