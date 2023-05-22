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
        self.sector_solicitante = qt_entry.sector_solicitante.text()
        self.ref_ot = qt_entry.ref_ot.text()
        
        # Datos de origen
        self.num_formacion = qt_entry.num_formacion.currentText()
        self.num_coche = qt_entry.num_coche.currentText()

        # Descripcion de componente
        self.nom_modulo = qt_entry.nom_modulo.currentText()
        self.nom_sistema = qt_entry.nom_sistema.currentText()
        self.num_serie = qt_entry.num_serie.text()

        self.check_primer_ingreso = qt_entry.check_primer_ingreso.isChecked()
        
        # Descripcion de reparacion

        # Verificacion

        # Datos de operacio/s
        print("---"*20)
        print(self.tipo_servicio)
        print(self.nom_sector)
        print(self.num_reparacion)
        print(self.num_formacion)
        print(self.num_coche)

# ---------------------Clases que contienen métodos para base de datos--------------------------------
try:
    db = SqliteDatabase(
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


class Componentes(BaseModel):
    """
    Clase asociada a la tabla de la base de datos, y donde defino sus atributos (campos).
    """

    nombre = CharField()
    cantidad = CharField()
    precio = CharField()
    descripcion = CharField()


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
        self.con.create_tables([Componentes])  # Creo la tabla Componentes.

    def agregar_db(self, nombre, cantidad, precio, descripcion):
        """
        Método para agregar una fila de datos (registro) a la tabla.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.
        """
        comp = Componentes()  # Creo un objeto (registro) de la clase Componentes.

        # Le asigno los valores ingresados a cada atributo(campo) del objeto.
        comp.nombre = nombre
        comp.cantidad = cantidad
        comp.precio = precio
        comp.descripcion = descripcion

        try:
            comp.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

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



