"""
Registro de empleados: Diseña una clase Empleado que represente a un empleado en 
una empresa. Utiliza SQL para almacenar y recuperar información sobre los empleados, 
como nombre, salario y fecha de contratación. Implementa métodos para crear, leer, 
actualizar y eliminar registros de empleados en la base de datos. Utiliza 
decoradores para controlar el acceso a los métodos según los permisos del usuario.
"""
import os
import sys
from peewee import *

class BaseDatos:
    def __init__(self, ): pass
    def load_db(self, ): pass
    def delete_db(self, ): pass
    def update_db(self, ): pass

class Crud(BaseDatos):
    def __init__():
        super().__init__()

    def new_emp(self, id, nombre, salario, fecha_cont, rol): pass
    def delete_emp(self, id): pass
    def update_emp(self, id, conf, new_data): pass
    def read_emp(self, tipo_busqueda): pass

class Empleado:
    def __init__(self, ):
        #self.obj_crud = Crud()
        print("----"*4, "Bienvenido", "----"*4)

    def menu(self, ):
        print("---"*15)
        print("Seleccione una opcion:")
        print("(1) Agregar nuevo empleado")
        print("(2) Eliminar empleado")
        print("(3) Actualizar datos de empleado")
        print("(4) Ver listado de empleados")
        print("(5) Salir")

        try:
            return int(input())
        except:
            ## se debe utilizar regex
            print("error de dato")

    def operacion(self, option):
        self.option = option

        if self.option == 1:
            print("new")
        elif self.option == 2:
            print("del")
        elif self.option == 3:
            print("up")
        elif self.option == 4:
            print("view")
        elif self.option == 5:
            print("salir")
        else:
            print("opcion no valida, vuelva a intentar")

obj_empleado = Empleado()
while True:
        select = obj_empleado.menu()
        obj_empleado.operacion(select)


