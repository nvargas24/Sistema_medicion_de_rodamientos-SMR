# No es el metodo mas apropiado, deberia usarse un observador para los cambios realizados
from PySide2.QtGui import *

class InputData():
    # Se puede implementar una lista de usuario para validar su rol, o desde una base de datos
    def user_type(self, name, pswd):
        if name=="admin" and pswd=="admin":
            print("Ingresa como administrador")
            return "admin"
        elif name=="user" and pswd=="user":
            print("Ingresa como usuario")
            return "user"
        else:
            print("Usuario no valido")
            return "no existe" 
    
    
