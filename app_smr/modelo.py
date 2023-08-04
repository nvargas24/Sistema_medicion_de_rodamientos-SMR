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
    
class CfgFileManager():
    def new_file_config(self):
        self.config={
            'SKF1':{
                'horario':{
                    'v300':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1500':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1800':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                },
                'antihorario':{
                    'v1500':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1800':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                },               
            },
            'SKF2':{
                'horario':{
                    'v300':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1500':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1800':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                },
                'antihorario':{
                    'v1500':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                    'v1800':{'bpfo': 12000, 'bpfi': 15000, 'ftf': 600, 'bsf': 800},
                },               
            }
        }

        with open('config_rod.cfg', 'w') as file:
            for rodamiento, sentidos in self.config.items():
                file.write(f'[{rodamiento}]\n')
                for sentido, velocidades in sentidos.items():
                    file.write(f'   [{sentido}]\n')
                    for velocidad, freqs in velocidades.items():
                        file.write(f'       [{velocidad}]\n')
                        for freq, value in freqs.items():
                            file.write(f'               {freq}={value}\n')
                        file.write('\n') 


    def upgrade_file_config(self, modelo, config_freq):
        self.config[modelo] = config_freq

    def read_file_config(self):
        pass

    def delete_file_config(self):
        pass