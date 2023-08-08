# No es el metodo mas apropiado, deberia usarse un observador para los cambios realizados
from PySide2.QtGui import *
import numpy as np
import os

import paho.mqtt.client as mqtt

SAMPLES_FFT = 512

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

class Mqtt():
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

        self.keepalive_ant = False
        self.temp_obj_ant = 0.0
        self.acel_axial_ant = 0.0
        self.acel_radial_ant = 0.0
        self.pres_bpfi_ant = False
        self.pres_bpfo_ant = False
        self.pres_bsf_ant = False
        self.pres_ftf_ant = False
        self.fft_ant = False
        self.temp_obj_pos = 0.0
        self.acel_axial_pos = 0.0
        self.acel_radial_pos = 0.0
        self.pres_bpfi_pos = False
        self.pres_bpfo_pos = False
        self.pres_bsf_pos = False
        self.pres_ftf_pos = False
        self.fft_pos = False

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conexión exitosa al broker")
        else:
            print(f"No se pudo conectar al broker. Código de retorno: {rc}")

    def start(self):
        try:
            self.client.on_connect = self.on_connect
            self.client.connect(self.broker_host, self.broker_port)
            self.client.loop_start()
        except ConnectionError as err:
            print(f"No se pudo conectar. ERROR: {str(err)}")
    
    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

    def send(self, topic, message):
        self.client.publish(topic, message)

    def on_message(self, client, userdata, msg):
        print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
        self.topic = msg.topic
        self.msg = msg.payload.decode()
        self.qualify_data_bytopic()

    def suscrip(self, topic):
        self.client.subscribe(topic)
        self.client.on_message = self.on_message 

    def desuscrip(self, topic):
        self.client.unsubscribe(topic)

    def qualify_data_bytopic(self):
        # Verifico si hay datos recibidos por broker y doy formato
        if self.topic == "rodAnt/keepalive":
            self.keepalive_ant = True
        if self.topic == "rodAnt/tempObj":
            self.temp_obj_ant = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelAxial":
            self.acel_axial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelRadial":
            self.acel_radial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/presBPFO":
            self.pres_bpfo_ant = int(self.msg)
        if self.topic == "rodAnt/presBPFI":
            self.pres_bpfi_ant = int(self.msg)
        if self.topic == "rodAnt/presBSF":
            self.pres_bsf_ant = int(self.msg)
        if self.topic == "rodAnt/presFTF":
            self.pres_ftf_ant = int(self.msg)
        if self.topic == "rodAnt/fft":
            self.fft_ant = self.msg

        if self.topic == "rodPos/tempObj":
            self.temp_obj_pos = "{:.2f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelAxial":
            self.acel_axial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelRadial":
            self.acel_radial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/presBPFO":
            self.pres_bpfo_pos = self.msg
        if self.topic == "rodPos/presBPFI":
            self.pres_bpfi_pos = self.msg
        if self.topic == "rodPos/presBSF":
            self.pres_bsf_pos = self.msg
        if self.topic == "rodPos/presFTF":
            self.pres_ftf_pos = self.msg
        if self.topic == "rodPos/fft":
            self.fft_pos = self.msg

    def suscrip_topics(self):
        self.suscrip("rodAnt/fft")
        self.suscrip("rodAnt/tempObj")
        self.suscrip("rodAnt/acelAxial")
        self.suscrip("rodAnt/acelRadial")
        self.suscrip("rodAnt/presBPFO")
        self.suscrip("rodAnt/presBPFI")
        self.suscrip("rodAnt/presBSF")
        self.suscrip("rodAnt/presFTF")

        self.suscrip("rodPos/fft")
        self.suscrip("rodPos/tempObj")
        self.suscrip("rodPos/acelAxial")
        self.suscrip("rodPos/acelRadial")
        self.suscrip("rodPos/presBPFO")
        self.suscrip("rodPos/presBPFI")
        self.suscrip("rodPos/presBSF")
        self.suscrip("rodPos/presFTF")

    def desuscrip_topics(self):
        self.desuscrip("rodAnt/fft")
        self.desuscrip("rodAnt/tempObj")
        self.desuscrip("rodAnt/acelAxial")
        self.desuscrip("rodAnt/acelRadial")
        self.desuscrip("rodAnt/presBPFO")
        self.desuscrip("rodAnt/presBPFI")
        self.desuscrip("rodAnt/presBSF")
        self.desuscrip("rodAnt/presFTF")

        self.desuscrip("rodPos/fft")
        self.desuscrip("rodPos/tempObj")
        self.desuscrip("rodPos/acelAxial")
        self.desuscrip("rodPos/acelRadial")
        self.desuscrip("rodPos/presBPFO")
        self.desuscrip("rodPos/presBPFI")
        self.desuscrip("rodPos/presBSF")
        self.desuscrip("rodPos/presFTF")

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

class Measure():
    def __init__(self, widgets):
        super().__init__()
        # Atributo para acceder a los widgets
        self.widgets = widgets
        self.file_cfg = CfgFileManager()
        self.mqtt_obj = Mqtt("192.168.5.203", 1883)

        self.num_fft = 1
        self.cont_ensayos = 0
        self.freq = np.arange(0, SAMPLES_FFT*37, 37)
        self.seconds = 0
        self.minutes = 0        

    def init_ensayo(self):
        # Cierro conexiones previas
        self.mqtt_obj.stop()
        # Inicio conexion mqtt
        self.mqtt_obj.start()
        self.cont_ensayos += 1

        self.widgets.ui.btn_iniciar.setEnabled(False)       
        self.widgets.ui.btn_finalizar.setEnabled(True)
        self.widgets.ui.btn_config_data.setEnabled(False)

        if not self.cont_ensayos == 0:
            self.widgets.ui.btn_ver_ensayos.setEnabled(True)
        else:
            self.widgets.ui.btn_ver_ensayos.setEnabled(False)            

        self.param_ensayo(str(self.cont_ensayos))
        # Enviar por mqtt los datos de configuracion
        self.mqtt_obj.send("smr/start", True)
        self.param_ensayo_send_mqtt()

        self.mqtt_obj.suscrip_topics()
        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.widgets.timer1.start(1000)
        self.notificacion("Ensayo "+ str(self.cont_ensayos) + " en proceso")

    def param_ensayo_send_mqtt(self):
        self.mqtt_obj.send("rodAnt/frecBPFO", int(self.freq_bpfo_ant))
        self.mqtt_obj.send("rodAnt/frecBPFI", int(self.freq_bpfi_ant))
        self.mqtt_obj.send("rodAnt/frecFTF", int(self.freq_ftf_ant))
        self.mqtt_obj.send("rodAnt/frecBSF", int(self.freq_bsf_ant))

        self.mqtt_obj.send("rodPos/frecBPFO", int(self.freq_bpfo_pos))
        self.mqtt_obj.send("rodPos/frecBPFI", int(self.freq_bpfi_pos))
        self.mqtt_obj.send("rodPos/frecFTF", int(self.freq_ftf_pos))
        self.mqtt_obj.send("rodPos/frecBSF", int(self.freq_bsf_pos))

    def param_ensayo(self, ensayo):
        # el ensayo depende del sentido y la velocidad

        self.data_ensayo = self.file_cfg.read_file_config_ensayo("UltimoEnsayo")
        self.rod_ant = self.data_ensayo["RodamientoAnterior"]
        self.rod_pos = self.data_ensayo["RodamientoPosterior"]
        self.temp_max = self.data_ensayo["TemperaturaMax"]
        self.temp_min = self.data_ensayo["TemperaturaMin"]
        self.axial_max = self.data_ensayo["VibracionAxialMax"]
        self.radial_max = self.data_ensayo["VibracionRadialMax"]

        ## LER DE ARCHIVO .CFG PARAMETRO SEGUN RODAMIENTOS
        if ensayo=="1":
            self.data_rod_ant = self.file_cfg.read_file_config(self.rod_ant, "Horario", "v300")
            self.data_rod_pos = self.file_cfg.read_file_config(self.rod_pos, "Horario", "v300")
        elif ensayo=="2":
            self.data_rod_ant = self.file_cfg.read_file_config(self.rod_ant, "Horario", "v1500")
            self.data_rod_pos = self.file_cfg.read_file_config(self.rod_pos, "Horario", "v1500")
        elif ensayo=="3":
            self.data_rod_ant = self.file_cfg.read_file_config(self.rod_ant, "Horario", "v1800")
            self.data_rod_pos = self.file_cfg.read_file_config(self.rod_pos, "Horario", "v1800")
        elif ensayo=="4":
            self.data_rod_ant = self.file_cfg.read_file_config(self.rod_ant, "Antihorario", "v1500")
            self.data_rod_pos = self.file_cfg.read_file_config(self.rod_pos, "Antihorario", "v1500")
        elif ensayo=="5":
            self.data_rod_ant = self.file_cfg.read_file_config(self.rod_ant, "Antihorario", "v1800")
            self.data_rod_pos = self.file_cfg.read_file_config(self.rod_pos, "Antihorario", "v1800")
        
        ### YA SE PUEDE ACCEDER A LAS FRECUENCIAS
        self.freq_bpfo_ant = self.data_rod_ant["bpfo"]
        self.freq_bpfi_ant = self.data_rod_ant["bpfi"]
        self.freq_ftf_ant = self.data_rod_ant["ftf"]
        self.freq_bsf_ant = self.data_rod_ant["bsf"]

        self.freq_bpfo_pos = self.data_rod_pos["bpfo"]
        self.freq_bpfi_pos = self.data_rod_pos["bpfi"]
        self.freq_ftf_pos = self.data_rod_pos["ftf"]
        self.freq_bsf_pos = self.data_rod_pos["bsf"]

    def stop_ensayo(self):
        self.widgets.ui.btn_iniciar.setEnabled(True)       
        self.widgets.ui.btn_finalizar.setEnabled(False)

        if not self.cont_ensayos == 0:
            self.widgets.ui.btn_ver_ensayos.setEnabled(True)
        else:
            self.widgets.ui.btn_config_data.setEnabled(True)
            self.widgets.ui.btn_ver_ensayos.setEnabled(False)            


        self.mqtt_obj.desuscrip_topics()
        self.mqtt_obj.stop()
        self.widgets.windows.win_user.timer1.stop()

        self.notificacion("Finalizo ensayo "+ str(self.cont_ensayos) + 
                          " a los "+ str(self.minutes) + " minutos y "+ 
                          str(self.seconds) + " segundos")
        
        if self.cont_ensayos == 1:
            self.widgets.windows.popup_time_ensayos.set_time(str(self.cont_ensayos), self.minutes, self.seconds)
        elif self.cont_ensayos == 2:
            self.widgets.windows.popup_time_ensayos.set_time(str(self.cont_ensayos), self.minutes, self.seconds)
        elif self.cont_ensayos == 3:
            self.widgets.windows.popup_time_ensayos.set_time(str(self.cont_ensayos), self.minutes, self.seconds)
        elif self.cont_ensayos == 4:
            self.widgets.windows.popup_time_ensayos.set_time(str(self.cont_ensayos), self.minutes, self.seconds)
        elif self.cont_ensayos == 5:
            self.widgets.windows.popup_time_ensayos.set_time(str(self.cont_ensayos), self.minutes, self.seconds)
        else:
            self.widgets.windows.popup_time_ensayos.set_time("reset", None, None)

        self.widgets.windows.popup_meas_corrientes.exec_()

    def timer_ensayo(self, ):
        """
        Timer de Modo ensayo - tiempo de contador asignado por usuario
        """
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60 and self.seconds == 60:
            self.notificacion("Tiempo máximo permitido superado")
            self.seconds = 0
            self.minutes = 0

        self.widgets.ui.lcd_time_ensayo.display(f"{self.minutes:02d}:{self.seconds:02d}")

    def notificacion(self, msj):
        """
        Informa eventos
        """        
        self.widgets.ui.label_notificacion.setText(str(msj))
