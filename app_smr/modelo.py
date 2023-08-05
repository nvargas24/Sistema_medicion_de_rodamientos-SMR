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
    
    def data_test(self):
        pass

class CfgFileManager():
    # CONFIG RODAMIENTOS
    def new_file_config_rod(self):
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
                file.write(f'[[{rodamiento}]]\n')
                for sentido, velocidades in sentidos.items():
                    file.write(f'    [{sentido}]\n')
                    for velocidad, freqs in velocidades.items():
                        file.write(f'        [{velocidad}]\n')
                        for freq, value in freqs.items():
                            file.write(f'            {freq}={value}\n')
                        file.write('\n') 

    def add_model_config(self, modelo, config_freq):
        self.config[modelo] = config_freq

    def update_config_value(self, rodamiento, sentido, velocidad, freq, new_value):
        self.config[rodamiento][sentido][velocidad][freq] = new_value 

    def read_list_rod(self):
        self.rodamientos = []

        with open('config_rod.cfg', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if  line.startswith('[[') and \
                line.endswith(']]'):
                rodamiento = line[2:-2]
                self.rodamientos.append(rodamiento)
        
        return self.rodamientos

    def read_file_config(self, rodamiento, sentido, velocidad): pass

    def delete_file_config(self):
        pass
    
    # CONFIG ENSAYO
    def new_file_config_ensayo(self):
        list_rod = self.read_list_rod()

        self.config_ensayo= {
            "EnsayoDefault": {
                "RodamientoAnterior": list_rod[0],
                "RodamientoPosterior": list_rod[0],
                "TemperaturaMax": 30,
                "TemperaturaMin": 12,
                "VibracionAxialMax": 0.05,
                "VibracionRadialMax": 0.1
            },
            "UltimoEnsayo": {
                "RodamientoAnterior": list_rod[1],
                "RodamientoPosterior": list_rod[1],
                "TemperaturaMax": 35,
                "TemperaturaMin": 10,
                "VibracionAxialMax": 0.55,
                "VibracionRadialMax": 0.4
            },
        }

        with open('config_ensayo.cfg', 'w') as file:
            for ensayo, parametros in self.config_ensayo.items():
                file.write(f"[{ensayo}]\n")
                for parametro, value in parametros.items():
                    file.write(f"{parametro} = {value}\n")
                file.write("\n")

    def read_file_config_ensayo(self, ensayo):
        config_data = {}
        ensayo_actual = None

        with open('config_ensayo.cfg', "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    ensayo_actual = line[1:-1]
                    config_data[ensayo_actual] = {}
                elif ensayo_actual and "=" in line:
                    clave, valor = line.split("=")
                    config_data[ensayo_actual][clave.strip()] = valor.strip()

        return config_data.get(ensayo, {})

    def update_config_ensayo(self, parametro, new_value):
        with open('config_ensayo.cfg', "r") as file:
            lines = file.readlines()

        with open('config_ensayo.cfg', "w") as file:
            modificar = False
            for i, line in enumerate(lines):
                if modificar and parametro in lines[i]:
                    lines[i] = f"{parametro} = {new_value}\n"
                    modificar = False
                file.write(lines[i])

                if "[UltimoEnsayo]" in line:
                    modificar = True