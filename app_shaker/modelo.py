from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
import time
import numpy as np
import os

import paho.mqtt.client as mqtt
from peewee import *

NUM_ENSAYOS = 2

# ---------------------Clases que contienen métodos para base de datos--------------------------------
try:
    db = SqliteDatabase(
        "registro_eventos.db"
    )  # Creo el objeto que indica el tipo y nombre de bd a la cual me voy a conectar (si no existe la crea).
except:
    print("No se pudo crear la base de datos")

class BaseModel(Model):
    """
    Clase que establece a que base de datos me conecto y su tipo.
    """

    class Meta:
        database = db  # Indico a que base me conecto y su tipo.

class RodAnterior(BaseModel):
    Tiempo_de_ensayo = TimeField()
    Acel_x = FloatField()
    Acel_y = FloatField()
    Acel_z = FloatField()

class RodPosterior(BaseModel):
    Tiempo_de_ensayo = TimeField()
    Acel_x = FloatField()
    Acel_y = FloatField()
    Acel_z = FloatField()

class BaseDatos:
    """
    Clase que contiene métodos para conectarme a la base de datos, y para manejar los registros de la misma.
    """

    def __init__(self):
        """
        Constructor para crear, conectarme, y agregar una tabla a la base de datos.
        """
        self.con = db
        self.con.connect()
        self.con.create_tables([RodAnterior()])
        self.con.create_tables([RodPosterior()])

    def agregar_db_ant(self, time_ensayo, acel_x, acel_y, acel_z):

        reg = RodAnterior()
        reg.Tiempo_de_ensayo = time_ensayo
        reg.Acel_x = acel_x
        reg.Acel_y = acel_y
        reg.Acel_z = acel_z      

        try:
            reg.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

    def agregar_db_pos(self, time_ensayo, acel_x, acel_y, acel_z):

        reg = RodPosterior()
        reg.Tiempo_de_ensayo = time_ensayo
        reg.Acel_x = acel_x
        reg.Acel_y = acel_y
        reg.Acel_z = acel_z      

        try:
            reg.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

    def upgrade_db(self):
        """
        Carga nuevo frame a base de datos
        """
        
        self.agregar_db_ant(
            self.mqtt_obj.time_stamp,
            self.mqtt_obj.acel_x_ant,            
            self.mqtt_obj.acel_y_ant, 
            self.mqtt_obj.acel_z_ant
            )

        self.agregar_db_pos(
            self.mqtt_obj.time_stamp,
            self.mqtt_obj.acel_x_ant,            
            self.mqtt_obj.acel_y_ant, 
            self.mqtt_obj.acel_z_ant
            )

class Mqtt:
    def __init__(self, broker_host, broker_port):
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port

        self.acel_axial_ant = 0.0
        self.acel_radial_ant = 0.0

        self.acel_axial_pos = 0.0
        self.acel_radial_pos = 0.0


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
        if self.topic == "rodAnt/acelAxial":
            self.acel_axial_ant = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodAnt/acelRadial":
            self.acel_radial_ant = "{:.3f}".format(float(self.msg)) 


        if self.topic == "rodPos/acelAxial":
            self.acel_axial_pos = "{:.3f}".format(float(self.msg)) 
        if self.topic == "rodPos/acelRadial":
            self.acel_radial_pos = "{:.3f}".format(float(self.msg)) 

    def suscrip_topics(self):
        self.suscrip("rodAnt/acelAxial")
        self.suscrip("rodAnt/acelRadial")

        self.suscrip("rodPos/acelAxial")
        self.suscrip("rodPos/acelRadial")

    def desuscrip_topics(self):
        self.desuscrip("rodAnt/acelAxial")
        self.desuscrip("rodAnt/acelRadial")

        self.desuscrip("rodPos/acelAxial")
        self.desuscrip("rodPos/acelRadial")

class Measure(BaseDatos):
    
    def __init__(self, widgets):
        super().__init__()
        # Atributo para acceder a los widgets
        self.widgets = widgets
        
        self.mqtt_obj = Mqtt("192.168.149.203", 1883)
        self.cont_ensayos = 1
        self.freq = np.arange(0, 512*37, 37)
        #self.reset_widgets()
        self.widgets_config()

    def init_conf(self):
        """
        Modo configuracion - Usuario debe ingresar parametros de configuracion
        """
        self.widgets_config()
        #self.reset_widgets()    
        self.notificacion("Esperando configuracion")

    def init_ensayo(self):
        """
        Callback de boton 'Iniciar' - Obtiene parametros del ui y los envia por mqtt
        """
        # Inicio conexion mqtt
        self.mqtt_obj.start()
        # Enviar por mqtt los datos de configuracion
        self.mqtt_obj.send("smr/start", True)
        # Des/habilito widget para modo ensayo
        self.widgets_ensayo()
        self.mqtt_obj.suscrip_topics()
        # Temporizador de 1 segundo, cuando finaliza accede a metodo asociado
        self.widgets.timer1.start(1000)
    
    def finish_test(self):
        print("Finalizo test")
        # Finalizo contadores
        self.widgets.timer1.stop()
        self.reset_widgets()
        self.cont_ensayos = 1
        self.mqtt_obj.send("smr/stop", True)
        # Se vuelve a modo configuracion
        self.mqtt_obj.stop()
        self.init_conf()

    def widgets_config(self):
        """
        Des/habilita widgets en modo configuracion
        """
        self.widgets.ui.btn_finish.setEnabled(False)
        self.widgets.ui.btn_init.setEnabled(True)

        self.widgets.ui.lcd_time_ensayo.setEnabled(False)

        ### FALTA DE TABLA

    def widgets_ensayo(self):
        """
        Des/habilita widgets en modo ensayo
        """
        self.widgets.ui.btn_finish.setEnabled(True)
        self.widgets.ui.btn_init.setEnabled(False)

        self.widgets.ui.lcd_time_ensayo.setEnabled(True)

        self.widgets.ui.lcd_axial_ant.setEnabled(True)
        self.widgets.ui.lcd_radial_ant.setEnabled(True)

    def timer_ensayo(self, ):
        """
        Timer de Modo ensayo - tiempo de contador asignado por usuario
        """
        self.notificacion("Ensayo "+ str(self.cont_ensayos) + " en proceso")
        # Se obtiene minutos y segundos a mostrar en lcd
        # Cada vez que se cumpla un 1 seg resto un valor del total de segundos
        self.seconds_total +=1
        # Se verifica si el dispositivo publico algo en un topic
        self.data_recive()
        # Se detiene contador para que no siga con parte negativa
        if self.seconds_total<0 : 
            self.widgets.timer1.stop()
            # Cargo valor a progressbar cada vez que finaliza un ensayo
            self.widgets.ui.progress_bar_programa.setValue(int(self.cont_ensayos))
            self.reset_widgets()
            self.mqtt_obj.desuscrip_topics()

    def notificacion(self, msj):
        """
        Informa eventos
        """        
        self.widgets.ui.label_notificacion.setText(str(msj))
    
    def reset_widgets(self):
        """
        Reseteo estado de widgets
        """
        self.widgets.ui.lcd_time_ensayo.display(f"{0:02d}:{0:02d}:{0:02d}")

        self.widgets.grafica.ax.clear()
        self.widgets.grafica.ax.set_title("Rodamiento anterior")
        self.widgets.grafica.upgrade_fft(self.freq, np.zeros(512))

    def data_recive(self):
        """
        Muestra lecturas obtenidas de sensores en display
        """
        # Muestro datos recibidos en ui - rodamiento anterior
        ## CARGAR TABLA

        # Si se registra alguna freq se guarda datos en base de datos
        self.upgrade_db()

        # Reseteo buffer para topic y msg
        self.mqtt_obj.topic = None
        self.mqtt_obj.msg = None        