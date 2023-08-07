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
            'SKF6311Default':{
                'Horario':{
                    'v300':{'bpfo': 920, 'bpfi': 1480, 'ftf': 115, 'bsf': 615},
                    'v1500':{'bpfo': 4620, 'bpfi': 7420, 'ftf': 570, 'bsf': 3070},
                    'v1800':{'bpfo': 5520, 'bpfi': 8870, 'ftf': 685, 'bsf': 3670},
                },
                'Antihorario':{
                    'v1500':{'bpfo': 4620, 'bpfi': 7420, 'ftf': 570, 'bsf': 3070},
                    'v1800':{'bpfo': 5520, 'bpfi': 8875, 'ftf': 685, 'bsf': 3670},
                },               
            },
            'SKF214Default':{
                'Horario':{
                    'v300':{'bpfo': 2211, 'bpfi': 2890, 'ftf': 130, 'bsf': 1110},
                    'v1500':{'bpfo': 11090, 'bpfi': 14500, 'ftf': 650, 'bsf': 5550},
                    'v1800':{'bpfo': 13260, 'bpfi': 17325, 'ftf': 775, 'bsf': 6640},
                },
                'Antihorario':{
                    'v1500':{'bpfo': 11090, 'bpfi': 14495, 'ftf': 650, 'bsf': 5550},
                    'v1800':{'bpfo': 13260, 'bpfi': 17335, 'ftf': 775, 'bsf': 6645},
                },               
            },
            'SKF6311':{
                'Horario':{
                    'v300':{'bpfo': 920, 'bpfi': 1480, 'ftf': 115, 'bsf': 615},
                    'v1500':{'bpfo': 4620, 'bpfi': 7420, 'ftf': 570, 'bsf': 3070},
                    'v1800':{'bpfo': 5520, 'bpfi': 8870, 'ftf': 685, 'bsf': 3670},
                },
                'Antihorario':{
                    'v1500':{'bpfo': 4620, 'bpfi': 7420, 'ftf': 570, 'bsf': 3070},
                    'v1800':{'bpfo': 5520, 'bpfi': 8875, 'ftf': 685, 'bsf': 3670},
                },               
            },
            'SKF214':{
                'Horario':{
                    'v300':{'bpfo': 2211, 'bpfi': 2890, 'ftf': 130, 'bsf': 1110},
                    'v1500':{'bpfo': 11090, 'bpfi': 14500, 'ftf': 650, 'bsf': 5550},
                    'v1800':{'bpfo': 13260, 'bpfi': 17325, 'ftf': 775, 'bsf': 6640},
                },
                'Antihorario':{
                    'v1500':{'bpfo': 11090, 'bpfi': 14495, 'ftf': 650, 'bsf': 5550},
                    'v1800':{'bpfo': 13260, 'bpfi': 17335, 'ftf': 775, 'bsf': 6645},
                },               
            }
        }

        with open('config_rod.cfg', 'w') as file:
            for rodamiento, sentidos in self.config.items():
                file.write(f'[[[{rodamiento}]]]\n')
                for sentido, velocidades in sentidos.items():
                    file.write(f'    [[{sentido}]]\n')
                    for velocidad, freqs in velocidades.items():
                        file.write(f'        [{velocidad}]\n')
                        for freq, value in freqs.items():
                            file.write(f'            {freq}={value}\n')
                        file.write('\n') 

    def add_model_config(self, modelo, config_freq):
        self.config[modelo] = config_freq

    def update_config_rod(self, rodamiento, sentido, velocidad, freq, new_value):
        with open('config_rod.cfg', "r") as file:
            lines = file.readlines()

        with open('config_rod.cfg', "w") as file:
            modificar = False
            found_rod = False
            found_sentido = False

            for i, line in enumerate(lines):
                line = line.strip()
                if modificar and freq in lines[i]:
                    lines[i] = f"            {freq}={new_value}\n"
                    modificar = False
                    found_rod = False
                    found_sentido = False
                file.write(lines[i])

                if line.startswith("[[[") and line.endswith("]]]"):
                    if line[3:-3] == rodamiento:
                        found_rod = True
                elif found_rod and line.startswith("[[") and line.endswith("]]"):
                    if line[2:-2] == sentido:
                        found_sentido = True
                elif found_sentido and  line.startswith("[") and line.endswith("]"):
                    if line[1:-1] == velocidad:
                        modificar = True

    def read_list_rod(self):
        self.rodamientos = []

        with open('config_rod.cfg', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if  line.startswith('[[[') and line.endswith(']]]'):
                rodamiento = line[3:-3]
                if rodamiento.find("Default") == -1:
                    self.rodamientos.append(rodamiento)
        
        return self.rodamientos

    def read_file_config(self, rodamiento, sentido, velocidad):
        """
        Metodo para obtener diccionario de config_rod.cfg
        """
        config_data = {}
        
        categoria = None
        subcategoria = None
        subsubcategoria = None
        
        with open("config_rod.cfg", 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("[[[") and line.endswith("]]]"):
                    categoria = line[3:-3]
                    config_data[categoria] = {} # creo diccionario vacio solo con categoria
                elif categoria and line.startswith("[[") and line.endswith("]]"):
                    subcategoria = line[2:-2]
                    config_data[categoria][subcategoria] = {}
                elif subcategoria and line.startswith("[") and line.endswith("]"):
                    subsubcategoria = line[1:-1]
                    config_data[categoria][subcategoria][subsubcategoria] = {}
                elif subsubcategoria and "=" in line:
                    clave, valor = line.split("=")
                    config_data[categoria][subcategoria][subsubcategoria][clave.strip()] = valor.strip()
        # se accede a hasta diccionario de velocidad por clave
        # para acceder a la frecuencia indicar clave en parametro
        return config_data.get(rodamiento, {}).get(sentido, {}).get(velocidad,{})

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
        # con get se especifica el diccionario a acceder
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