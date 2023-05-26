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
    def __init__(self, ):
        super().__init__()

    def new_emp(self, regist_emp):
        print(regist_emp)

    def delete_emp(self, id): pass
    def update_emp(self, id, conf, new_data): pass
    def read_emp(self, tipo_busqueda): pass

class Empleado:
    def __init__(self, ):
        self.obj_crud = Crud()
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
            # Menu de ingreso de usuario
            self.id = int(input("Ingrese id: "))
            self.nombre = str(input("Ingrese nombre: "))
            self.salario = int(input("Ingrese salario: "))
            self.rol = str(input("Ingrese rol: "))            
            self.fecha_ingreso = str(input("Ingrese fecha de ingreso: "))

            self.registro = [self.id, self.nombre, self.salario, self.rol, self.fecha_ingreso]
            # testear estado de campos y regex

            state_registro = self.obj_crud.new_emp(self.registro)

        elif self.option == 2:
            print("del")
            self.id = int(input("Ingrese id: "))
            state_registro = self.obj_crud.delete_emp(self.id)

        elif self.option == 3:
            print("up")
            self.id = int(input("Ingrese id: "))
            # Se busca en base de datos al empleado
            registro_emp=self.obj_crud.update_emp(self.id)
            # Si existe se solicitan modificaciones a realizar
            if registro_emp:
                print("En base de datos: ", registro_emp)
                # Menu pora cambiar parametro
                print("(1) Nombre:", registro_emp[1])
                print("(2) Salario: ", registro_emp[2])
                print("(3) Rol: ", registro_emp[3])
                print("(4) Fecha de ingreso: ", registro_emp[4])

                param_registro = int(input("Indique parametro a modificar: "))
                conf_registro = input("Ingrese nuevo valor: ")

                registro_emp=self.obj_crud.update_emp(self.id, param_registro, conf_registro)
                print("Actualizado: ", registro_emp)

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
        if select == 5:
            break


