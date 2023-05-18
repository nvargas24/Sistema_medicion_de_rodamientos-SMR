import os
import sys
from peewee import *

class Crud():
    def __init__(self, ):
        pass

    def get(self, qt_entry):
        # Nota servicio
        self.tipo_servicio = qt_entry.tipo_servicio.currentText()
        self.nom_sector = qt_entry.nom_sector.currentText()
        self.num_reparacion = qt_entry.num_reparacion.text()

        # Datos solicitante
        self.nom_solicitante = qt_entry.nom_solicitante.text()
        self.nom_sector = qt_entry.nom_sector.text()
        self.ref_ot = qt_entry.ref_ot.text()
        
        # Datos de origen
        self.num_formacion = qt_entry.num_formacion.currentText()
        self.num_coche = qt_entry.num_coche.currentText()

        # Descripcion de componente
        self.nom_modulo = qt_entry.nom_modulo.currentText()
        self.nom_sistema = qt_entry.nom_sistema.currentText()
        self.num_serie = qt_entry.num_serie.text()

        # Descripcion de reparacion

        # Verificacion

        # Datos de operacio/s

        print(self.tipo_servicio)
        print(self.nom_sector)
        print(self.num_reparacion)
        print(self.num_formacion)
        print(self.num_coche)

# ---------------------Clases que contienen métodos para base de datos--------------------------------
try:
    db = MySQLDatabase(
        "control_laboratorio_de_electronica.db"
    )  # Creo el objeto que indica el tipo y nombre de bd a la cual me voy a conectar (si no existe la crea).
except:
    print("No se pudo crear la base de datos")


class BaseModel(Model):
    """
    Clase que establece a que base de datos me conecto y su tipo.
    """

    class Meta:
        database = db  # Indico a que base me conecto y su tipo.

class Fallas(BaseModel):
    falla = CharField()
    detalle = TextField()
    tipo = CharField()

class Dispositivos(BaseModel):
    num_serie = IntegerField()
    modulo = CharField()
    sistema = CharField()
    descripcion = TextField()

class Operarios(BaseModel):
    legajo = IntegerField()
    nombre = CharField()
    apellido = CharField()
    cargo = CharField()

class Reparacion(BaseModel):
    num_ref = IntegerField()
    detalle_rep = TextField()

class BaseDatos:
    """
    Clase que contiene métodos para conectarme a la base de datos, y para manejar los registros de la misma.
    """

    def __init__(self):
        """
        Constructor para crear, conectarme, y agregar una tabla a la base de datos.
        """
        self.con = db
        self.con.connect()  # Me conecto a la bd.
        self.con.create_tables([Dispositivo, Operarios])  # Creo la tabla

    def agregar_dispositivos(self, num_serie, nombre, descripcion, ubicacion, num_reparacion):

        dispo = Dispositivos()  # Creo un objeto (registro) de la clase Componentes.

        # Creo registro
        try:
            dispo.create(
                num_serie = num_serie,
                nombre = nombre,
                descripcion = descripcion,
                ubicacion = ubicacion,
                num_reparacion = num_reparacion
            ) 
        except:
            print("No se pudo crear el registro")

    def eliminar_db(self, nombre):
        """
        Método para eliminar una fila de datos (registro) de la tabla
        usando como referencia el campo **Nombre**.

        :param nombre: Nombre del componente.
        """
        reg_borrar = Componentes.get(Componentes.nombre == nombre)

        try:
            reg_borrar.delete_instance()  # Borro el registro de la tabla.
        except:
            print("No se pudo eliminar el registro")

    def leer_db(self, nombre):
        """
        Método para seleccionar una o varias filas de la tabla usando como referencia el campo **Nombre**.

        :param nombre: Nombre del componente.

        :returns: Fila/s encontrada/s de acuerdo a la referencia.
        """
        if nombre == None:
            rows = Componentes.select()
        else:
            rows = Componentes.select().where(Componentes.nombre == nombre)

        return rows

    def actualizar_db(self, nombre, cant, prec, descrip):
        """
        Método para actualizar uno o varios campos de una fila de la tabla.

        :param nombre: Nombre del componente.
        :param cant: Nuevo valor del campo cantidad(si existe un dato válido).
        :param cant: Nuevo valor del campo precio(si existe un dato válido).
        :param cant: Nuevo valor del campo descripción(si existe un dato válido).
        """

        if flag_c == 1:  # Si existe un dato "cantidad" válido
            reg_actualizar = Componentes.update(cantidad=cant).where(
                Componentes.nombre == nombre
            )

            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_p == 1:  # Si existe un dato "precio" válido
            reg_actualizar = Componentes.update(precio=prec).where(
                Componentes.nombre == nombre
            )

            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_d == 1:  # Si existe un dato "descripción" válido
            reg_actualizar = Componentes.update(descripcion=descrip).where(
                Componentes.nombre == nombre
            )

            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")



