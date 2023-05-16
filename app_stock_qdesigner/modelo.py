"""
modelo.py:
    Módulo encargado de la lógica de la app, lo cual implica el manejo de base de datos, CRUD, y eventos. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.2"

from peewee import *
from validar import Validacion
from observador import Sujeto
import datetime
import pandas as pd

# --------------------Variables---------------------------------
# Flag utilizado para informar si hubo un error en la validación de los datos de un campo a actualizar.
flag_e = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo cantidad.
flag_c = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo precio.
flag_p = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo descripción.
flag_d = 0


# ---------------------Decoradores-------------------------------
def decorador_add(metodo):
    """
    Función decoradora que captura el método ``agregar_db()``

    :param metodo: Método ``agregar_db()`` que captura.

    :returns: La función ``envoltura()``.
    """

    def envoltura(*args):
        """
        Función que ejecuta el método capturado e informa en un archivo de log la acción realizada.

        :param args: Párametros que fueron enviados previamente a la función capturada.
        """
        # Abro y escribo en un archivo de log para informar que se ingresó un nuevo registro.
        archivo = open("registro_log_app.txt", "a", encoding="utf-8")
        archivo.write(
            "Se ingresó un nuevo registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )

        # Ejecuto método capturado.
        metodo(*args)

    return envoltura


def decorador_del(metodo):
    """
    Función decoradora que captura el método ``eliminar_db()``

    :param metodo: Método ``eliminar_db()`` que captura.

    :returns: La función ``envoltura()``.
    """

    def envoltura(*args):
        """
        Función que ejecuta el método capturado e informa en un archivo de log la acción realizada.

        :param args: Párametros que fueron enviados previamente a la función capturada.
        """
        # Abro y escribo en un archivo de log para informar que se eliminó un registro.
        archivo = open("registro_log_app.txt", "a", encoding="utf-8")
        archivo.write(
            "Se eliminó un registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )

        # Ejecuto método capturado.
        metodo(*args)

    return envoltura


def decorador_mod(metodo):
    """
    Función decoradora que captura el método ``actualizar_db()``

    :param metodo: Método ``actualizar_db()`` que captura.

    :returns: La función ``envoltura()``.
    """

    def envoltura(*args):
        """
        Función que ejecuta el método capturado e informa en un archivo de log la acción realizada.

        :param args: Párametros que fueron enviados previamente a la función capturada.
        """
        # Abro y escribo en un archivo de log para informar que se modificó un registro.
        archivo = open("registro_log_app.txt", "a", encoding="utf-8")
        archivo.write(
            "Se modificó un registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )

        # Ejecuto método capturado.
        metodo(*args)

    return envoltura


def decorador_mostrar(metodo):
    """
    Función decoradora que captura el método ``mostrar_cat()``

    :param metodo: Método ``mostrar_cat()`` que captura.

    :returns: La función ``envoltura()``.
    """

    def envoltura(*args):
        """
        Función que ejecuta el método capturado, e informa en consola mediante una
        tabla la lista de componentes ingresados.
        A partir de dicha información también realiza un gráfico de torta que se
        actualiza cada vez que se consulta el stock de componentes o al iniciar la app.

        :param args: Párametros que fueron enviados previamente a la función capturada.
        """

        window_main = args[2]

        list_componente, list_cantidad = metodo(*args)

        # Se calcula y se muestra en consola una tabla de componentes cargados con sus respectivas cantidades.
        print("---" * 23)
        print("Lista de stock")
        dataset = {"Componente": list_componente, "Cantidad": list_cantidad}
        df = pd.DataFrame(dataset)
        print(df)
        print("---" * 23)

        # Se realiza un gráfico de torta del total de componentes cargados con sus respectivas cantidades.
        window_main.grafica.upgrade_graph(list_componente, list_cantidad)

    return envoltura


# ---------------------Clases que contienen métodos para base de datos--------------------------------
try:
    db = SqliteDatabase(
        "base_stock.db"
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

    @decorador_add
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

    @decorador_del
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

    def leer_db(self, nombre=None, descrip=None):
        """
        Método para seleccionar una o varias filas de la tabla usando como referencia
        el campo **Nombre** y/o el campo **Descripción**.

        :param nombre: Nombre del componente.
        :param descrip: Descripcion del componente.

        :returns: Fila/s encontrada/s de acuerdo a la referencia.
        """

        if nombre == None and descrip == None:
            rows = Componentes.select()
        elif nombre != None and descrip == None:
            rows = Componentes.select().where(Componentes.nombre == nombre)
        elif nombre == None and descrip != None:
            rows = Componentes.select().where(Componentes.descripcion == descrip)
        elif nombre != None and descrip != None:
            rows = Componentes.select().where(
                (Componentes.nombre == nombre) & (Componentes.descripcion == descrip)
            )

        return rows

    @decorador_mod
    def actualizar_db(self, nombre, cant, prec, descrip):
        """
        Método para actualizar uno o varios campos de una fila de la tabla.

        :param nombre: Nombre del componente.
        :param cant: Nuevo valor del campo cantidad (si existe un dato válido).
        :param prec: Nuevo valor del campo precio (si existe un dato válido).
        :param descrip: Nuevo valor del campo descripción (si existe un dato válido).
        """

        if flag_c == 1:  # Si existe un dato cantidad válido.
            reg_actualizar = Componentes.update(cantidad=cant).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_p == 1:  # Si existe un dato precio válido.
            reg_actualizar = Componentes.update(precio=prec).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_d == 1:  # Si existe un dato descripción válido.
            reg_actualizar = Componentes.update(descripcion=descrip).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")


# ---------------------Clase que contienen métodos para manejo de datos ingresados--------------------------------
class Crud(BaseDatos, Sujeto):
    """
    Clase que contiene métodos para el manejo de los datos ingresados.
    """

    def __init__(self):
        """
        Constructor que hereda el correspondiente a la clase ``BaseDatos()``,
        y que además crea un objeto ``Validacion()`` para comprobar los campos de entrada.
        También hereda de la clase ``Sujeto()`` para el manejo de observadores.
        """
        super().__init__()
        self.obj_val = Validacion()

    def agreg(self, nombre, cantidad, precio, descripcion):
        """
        Método para agregar un nuevo componente.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.

        :returns: ``"Campos vacios"`` si no se completaron todos los campos.
        :returns: ``"Ya existe el articulo"`` si el componente que se quiere ingresar ya se encontraba cargado.
        :returns: ``"Nuevo articulo cargado"`` si el componente fue ingresado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        nom = nombre.text()
        cant = cantidad.text()
        prec = precio.text()
        descrip = descripcion.text()

        # Chequeo que el campo nombre, cantidad, precio y descripcion no esten vacíos.
        if not (
            self.obj_val.empty_entry(nom, "nom")
            and self.obj_val.empty_entry(cant, "cant")
            and self.obj_val.empty_entry(prec, "prec")
            and self.obj_val.empty_entry(descrip, "descrip")
        ):
            return "Campos vacios"

        # Si se ingresó un dato inválido genero una excepción.
        if not (
            self.obj_val.val_entry(nom, "nom")
            and self.obj_val.val_entry(cant, "cant")
            and self.obj_val.val_entry(prec, "prec")
            and self.obj_val.val_entry(descrip, "descrip")
        ):
            raise ValueError("Campos incorrectos")

        # Cargo en la base de datos y notifico al observador
        if not self.leer_db(nom):
            self.agregar_db(nom, cant, prec, descrip)
            self.notificar(nom, cant, prec, descrip)
            return "Nuevo articulo cargado"

        return "Ya existe el articulo"

    def elim(self, nombre):
        """
        Método para eliminar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.

        :returns: ``"Campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"Articulo no encontrado"`` si el componente a eliminar no se encuentra ingresado.
        :returns: ``"Articulo eliminado"`` si el componente fue eliminado exitosamente.
        """
        nom = nombre.text()

        # Chequeo que el campo nombre no esté vacío.
        if not self.obj_val.empty_entry(nom, "nom"):
            return "Campo vacio"

        # Chequeo si el artículo a eliminar existe.
        if not self.leer_db(nom):
            return "Articulo no encontrado"

        # Elimino de la base de datos y notifico al observador.
        self.eliminar_db(nom)
        self.notificar(nom)
        return "Articulo eliminado"

    def modif(self, nombre, cantidad, precio, descripcion):
        """
        Método para modificar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.

        :returns: ``"Campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"Articulo no existe"`` si el componente a modificar no se encuentra ingresado.
        :returns: ``"Articulo sin modificar"`` si no se ingresó ningún parámetro a modificar del componente.
        :returns: ``"Articulo modificado"`` si el componente fue modificado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        global flag_e
        global flag_c
        global flag_p
        global flag_d

        nom = nombre.text()
        cant = cantidad.text()
        prec = precio.text()
        descrip = descripcion.text()

        # Chequeo que el campo nombre no esté vacío.
        if not self.obj_val.empty_entry(nom, "nom"):
            return "Campo vacio"

        # Chequeo si el artículo a modificar existe.
        if not self.leer_db(nom):
            return "Articulo no existe"

        # Si el campo cantidad no está vacío y cumple con el patrón de regex
        # se pondrá en '1' el flag_c (dato válido para actualizar).
        if self.obj_val.empty_entry(cant, "cant"):
            if self.obj_val.val_entry(cant, "cant"):
                flag_c = 1
            else:
                flag_e = 1

        # Si el campo precio no está vacío y cumple con el patrón de regex
        # se pondrá en '1' el flag_p (dato válido para actualizar).
        if self.obj_val.empty_entry(prec, "prec"):
            if self.obj_val.val_entry(prec, "prec"):
                flag_p = 1
            else:
                flag_e = 1

        # Si el campo descripción no está vacío y cumple con el patrón de regex
        # se pondrá en '1' el flag_p (dato válido para actualizar).
        if self.obj_val.empty_entry(descrip, "descrip"):
            if self.obj_val.val_entry(descrip, "descrip"):
                flag_d = 1
            else:
                flag_e = 1

        # Si no hubo error en la validación de datos (flag_e == 0) se actualizarán
        # los datos que hayan sido ingresados en los campos correspondientes.
        if not flag_e:
            # Si no se ingresó ningún dato a modificar.
            if not (flag_c or flag_p or flag_d):
                return "Articulo sin modificar"

            # Si se ingresó un dato modifico el componente y notifico al observador.
            self.actualizar_db(nom, cant, prec, descrip)
            self.notificar(nom, flag_c, cant, flag_p, prec, flag_d, descrip)

            flag_c = 0
            flag_p = 0
            flag_d = 0

            return "Articulo modificado"

        # Si hubo error en la validación de datos (flag == 1)
        # no se actualizará ningun campo y se informará del error al usuario.
        flag_e = 0  # Como ya se detecto un error se lo vuelve a setear para la siguiente operación.

        raise ValueError(
            "Campos incorrectos"
        )  # Si se ingresó un dato inválido genero una excepción.

    def consulta(self, nombre, descrip, window_consulta):
        """
        Método para consultar los datos de un componente en particular (lo busco por el nombre y/o descripción).

        :param nombre: Nombre del componente.
        :param descrip: Descripción del componente.
        :param window_consulta: Objeto de clase ``WindowConsulta()``.

        :returns: ``"Campo vacios"`` si no se ingresó ningún nombre y/o descripción.
        :returns: ``"Articulo no encontrado por nombre"`` si el componente consultado por nombre no se encuentra ingresado.
        :returns: ``"Articulo no encontrado por descripcion"`` si el componente consultado por descripción no se encuentra ingresado.
        :returns: ``"Articulo no encontrado"`` si el componente consultado por nombre y descripción no se encuentra ingresado.
        """
        nom = nombre.text()
        descrip = descrip.text()

        # Búsqueda por nombre.
        if self.obj_val.empty_entry(nom, "nom") and not self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            data_from_db = self.leer_db(nom, None)
            if not data_from_db:
                return "Articulo no encontrado por nombre"

        # Búsqueda por descripción.
        elif not self.obj_val.empty_entry(nom, "nom") and self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            data_from_db = self.leer_db(None, descrip)
            if not data_from_db:
                return "Articulo no encontrado por descripcion"

        # Búsqueda por nombre y descripción.
        elif self.obj_val.empty_entry(nom, "nom") and self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            data_from_db = self.leer_db(nom, descrip)
            if not data_from_db:
                return "Articulo no encontrado"

        else:
            return "Campos vacios"

        # Borro las filas de la tabla que contiene la ventana de Consulta.
        window_consulta.delete()

        # Cargo la tabla con la/s fila/s encontradas de acuerdo a la búsqueda.
        for row in data_from_db:
            window_consulta.insert(
                str(row.id),
                row.nombre,
                row.cantidad,
                row.precio,
                row.descripcion,
            )

    @decorador_mostrar
    def mostrar_cat(self, window_consulta, window_main):
        """
        Método que muestra el catálogo completo de componentes cargados hasta el momento.

        :param window_consulta: Objeto de clase ``WindowConsulta()``.
        :param window_main: Objeto de clase ``MainWindow()``, utilizado por el decorador vinculado al método.

        :returns: **x_nom**, lista que almacena los nombres de cada componente registrado.
        :returns: **y_cant**, lista que almacena las cantidades de cada componente registrado.
        """

        x_nom = []  # Lista que almacena los nombres de cada componente cargado.
        y_cant = []  # Lista que almacena las cantidades de cada componente cargado.

        data_from_db = self.leer_db()

        # Cargo la tabla de la ventana Consulta con todos los registros almacenados en la bd.
        for row in data_from_db:
            window_consulta.insert(
                str(row.id),
                row.nombre,
                row.cantidad,
                row.precio,
                row.descripcion,
            )

            x_nom.append(row.nombre)
            y_cant.append(row.cantidad)

        return x_nom, y_cant
