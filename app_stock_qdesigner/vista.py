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

#--- Clase para interaturar con tabla de catalogo ---#
class Catalogo():
    def agregar():
        pass
    def eliminar():
        pass
    def modificar():
        pass

#-------- Clases para ventanas -------#

class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent=None):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets

        self.obj_f = Crud()  # Creo un objeto de clase Crud.
        
        #-------------- Ventanas secundarias --------------#
        self.window_agregar = WindowAgregar()
        self.window_eliminar = WindowEliminar()
        self.window_modificar = WindowModificar()
        self.window_consulta = WindowConsulta() 

        # ------------------- Variables -------------------#
        self.var_nombre = StringVar()
        self.var_cantidad = StringVar()  # Luego lo convierto a int.
        self.var_precio = StringVar()  # Luego lo convierto a float.
        self.var_descrip = StringVar()

        mje = self.obj_f.agreg(
            self.var_nombre,
            self.var_cantidad,
            self.var_precio,
            self.var_descrip,
        )

        #------------- Grafico de torta -------------------#
        self.grafica = Canvas_grafica()
        self.ui.grafica_torta.addWidget(self.grafica)

        #--------------- Acciones para botones ------------#
        self.ui.btn_agregar.clicked.connect(self.agregar_dat)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_dat)
        self.ui.btn_modificar.clicked.connect(self.modificar_dat)
        self.ui.btn_consultar.clicked.connect(self.consultar_dat)


class WindowAgregar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.new_load)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def new_load(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        #--- Limpia celdas una vez cargados datos ---#
        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guarda nuevo articulo")
    
class WindowEliminar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.delete)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def delete(self,):
        nombre=str(self.ui.in_nombre.text())
        self.ui.in_nombre.clear()

        print(nombre)
        self.exit()
        print("Se elimino articulo")

class WindowModificar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.modificated)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def modificated(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()    

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guardo modificaciones")

class WindowConsulta(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)
        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.exit)

        self.ui.catalogo_list.setColumnWidth(0, 40)
        self.ui.catalogo_list.setColumnWidth(1, 120)
        self.ui.catalogo_list.setColumnWidth(2, 80)
        self.ui.catalogo_list.setColumnWidth(3, 80)
        self.ui.catalogo_list.setColumnWidth(4, 160)

        self.list_componentes_test()
        self.load_list_componentes()
    
    def list_componentes_test(self, ):
        self.datos = []

        self.datos.append(('2','1N4548', '32', '32', 'Diodo'))
        self.datos.append(('3','MCP3008', '2', '434', 'Circuito integrado'))
        self.datos.append(('4','7805', '45', '120', 'Regulador de tension'))

    def load_list_componentes(self, ):
        fila=0        
        for registro in self.datos:
            columna=0            
            self.ui.catalogo_list.insertRow(fila) # se debe crear filas cada vez que se cargan dato
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.catalogo_list.setItem(fila, columna, celda)
                columna+=1
            fila+=1


    def exit(self, ):
        self.close()
        print("Regresa a menu principal")
    
    def search(self, ):
        nombre=str(self.ui.in_nombre.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_descrip.clear()

        print(nombre)
        print(descrip)        
        print("Busca articulo")
    
    def full_cat(self, ):
        print("Muestra catalogo completo")
