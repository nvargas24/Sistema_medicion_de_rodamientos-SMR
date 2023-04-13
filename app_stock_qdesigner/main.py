import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

# ===========================================================
from app_stock import *
from consulta import *



class Opciones():
    def agregar_dat(self,):
        print("agregar articulo nuevo")
    def eliminar_dat(self,):
        print("eliminar articulo")
    def modificar_dat(self,):
        print("modificar articulo")
    def consultar_dat(self,):
        print("consultar articulo")
        window_consulta = ConsultaWindow(self,)        
        #window_consulta.exec_()
        window_consulta.setWindowTitle("Consulta")
        window_consulta.show()

class ConsultaWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self,)
        print("estoy aca")

class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent=None):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets

        self.ui.agregar.clicked.connect(self.agregar_dat)
        self.ui.eliminar.clicked.connect(self.eliminar_dat)
        self.ui.modificar.clicked.connect(self.modificar_dat)
        self.ui.consultar.clicked.connect(self.consultar_dat)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
    window = MainWindow() # Creo objeto de la clase MainWindow

    # Los metodos utilizados son los heredados de la clase QMainWindow
    window.setWindowTitle("App Stock")
    #window.setFixedWidth(750) # Opcional, ya esta definido al ajustar la ventana en el QtDesigner
    #window.setFixedHeight(400) # Opcional, ya esta definido al ajustar la ventana en el QtDesigner
    window.show()

    try:
        sys.exit(app.exec_())    # Mantiene abierta la app
    except SystemExit:
        print("Closing Window...")
