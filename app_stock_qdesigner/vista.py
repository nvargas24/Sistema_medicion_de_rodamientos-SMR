import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from Qt.window_main import *
from Qt.window_agregar import *
from Qt.window_eliminar import *
from Qt.window_modificar import *
from Qt.window_consulta import *

from modelo import Crud

#-------- Clases para widgets --------#
#--- Clase para abrir ventanas secundarias ---#
class Opciones():
    def agregar_dat(self,):
        print("Agregar articulo nuevo")
        self.window_agregar.setWindowTitle("Agregar")
        self.window_agregar.show()

    def eliminar_dat(self,):
        print("Eliminar articulo")
        self.window_eliminar.setWindowTitle("Eliminar")
        self.window_eliminar.show()

    def modificar_dat(self,):
        print("Modificar articulo")
        self.window_modificar.setWindowTitle("Modificar")
        self.window_modificar.show()

    def consultar_dat(self,):
        print("Consultar articulo")
        self.window_consulta.setWindowTitle("Consulta")
        self.window_consulta.show()

# --- Clase para iteractuar con grafico ---#
class Canvas_grafica(FigureCanvas):
    def __init__(self, ):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5,5), sharey=True, facecolor='none')
        super().__init__(self.fig)

        nombres= ['Diodos', 'Resistencias', 'Tiristores', 'Capacitores']
        colores=['red', 'blue', 'yellow', 'fuchsia']
        tamanio=[20, 29, 25, 30]
        explotar=[0.05, 0.05, 0.05, 0.05]

        self.ax.pie(tamanio, explode=explotar, labels=nombres, colors=colores,
                    autopct='%1.0f%%', pctdistance=0.6, shadow=True, startangle=90, radius=0.8, labeldistance=1.1)
        self.ax.axis('equal')

#-------- Clases para ventanas -------#

class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent=None):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets

        self.obj_f = Crud()  # Creo un objeto de clase Crud.
        
        #-------------- Ventanas secundarias --------------#
        self.window_agregar = WindowAgregar(self.obj_f)
        self.window_eliminar = WindowEliminar(self.obj_f)
        self.window_modificar = WindowModificar(self.obj_f)
        self.window_consulta = WindowConsulta(self.obj_f) 

        #------------- Grafico de torta -------------------#
        self.grafica = Canvas_grafica()
        self.ui.grafica_torta.addWidget(self.grafica)

        #--------------- Acciones para botones ------------#
        self.ui.btn_agregar.clicked.connect(self.agregar_dat)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_dat)
        self.ui.btn_modificar.clicked.connect(self.modificar_dat)
        self.ui.btn_consultar.clicked.connect(self.consultar_dat)


class WindowAgregar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(lambda: self.new_load(obj_f))
        self.ui.btns_option.rejected.connect(self.exit)

    def exit(self, ):
        self.close()
        print("Regresa a menu principal")


#aca tengo que pasar las variables in_nombre, in_ ... al modelo.py  y desde ahi trabajar con Crud que se encarga 
# de cargar el treeview de QT
    def new_load(self, obj_f):
        mje = obj_f.agreg(
                    self.ui.in_nombre, 
                    self.ui.in_cant, 
                    self.ui.in_precio, 
                    self.ui.in_descrip)

        print("Mensaje de agregar:", mje)
        print("Se guarda nuevo articulo")

        #--- Limpia celdas una vez cargados datos ---#
        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()

        self.exit() # Borra ventana

    
class WindowEliminar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)

        self.ui.btns_option.accepted.connect(lambda: self.delete(obj_f))
        self.ui.btns_option.rejected.connect(self.exit)
    
    def exit(self, ):
        print("Regresa a menu principal")
        self.close()

    def delete(self, obj_f):
        mje = obj_f.elim(
            self.ui.in_nombre)

        print("Mensaje de eliminar:", mje)
        print("Se elimino articulo")

        self.ui.in_nombre.clear() # Limpia celda una vez cargado dato

        self.exit() # Borra ventana

class WindowModificar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)

        self.ui.btns_option.accepted.connect(lambda: self.modificated(obj_f))
        self.ui.btns_option.rejected.connect(self.exit)


    def exit(self, ):
        print("Regresa a menu principal")        
        self.close()

    def modificated(self, obj_f):
        mje = obj_f.modif(
                    self.ui.in_nombre, 
                    self.ui.in_cant, 
                    self.ui.in_precio, 
                    self.ui.in_descrip)

        print("Mensaje de modificar:", mje)
        print("Se guardo modificaciones")

        #--- Limpia celdas una vez cargados datos ---#
        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()

        self.exit() # Borra ventana

class WindowConsulta(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)

        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.exit)

        #--- Ajusto ancho de columnas de la tabla ---#
        self.ui.catalogo_list.setColumnWidth(0, 40)
        self.ui.catalogo_list.setColumnWidth(1, 120)
        self.ui.catalogo_list.setColumnWidth(2, 80)
        self.ui.catalogo_list.setColumnWidth(3, 80)
        self.ui.catalogo_list.setColumnWidth(4, 160)

        
    def insert(self, nom, cant, prec, descrip):
        self.datos = []
        self.datos.append(('1', nom, cant, prec, descrip))

        self.datos.append(('2','1N4548', '32', '32', 'Diodo'))
        self.datos.append(('3','MCP3008', '2', '434', 'Circuito integrado'))
        self.datos.append(('4','7805', '45', '120', 'Regulador de tension'))
    
        self.load_list_componentes(self.datos)

    def load_list_componentes(self, frame):
        print("frame: ", frame)
        fila=0        
        for registro in frame:
            print("registro: ", registro, "  frame:", frame)
            columna=0            
            self.ui.catalogo_list.insertRow(fila) # se debe crear filas cada vez que se cargan dato
            for elemento in registro:
                print("registro: ", registro, "  elemento:", elemento)
                celda = QTableWidgetItem(elemento)
                print("celda:  ", celda)
                self.ui.catalogo_list.setItem(fila, columna, celda)
                columna+=1
            fila+=1

    def exit(self, ):
        print("Regresa a menu principal")
        self.close()

    def search(self, ):
        mje = self.obj_f.consulta(
                    self.ui.in_nombre)

        print("Mensaje de consulta:", mje)
        print("Busca articulo por nombre")

        #--- Limpia celdas una vez cargados datos ---#
        self.ui.in_nombre.clear()
        self.ui.in_descrip.clear()
    
    def full_cat(self, ):
        print("Muestra catalogo completo")
