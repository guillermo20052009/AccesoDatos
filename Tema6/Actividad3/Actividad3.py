import logging
from peewee import Model, CharField, ForeignKeyField, MySQLDatabase

# Configuración de logging para registrar todas las operaciones en un archivo y en la consola
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager_orm.log"),  # Archivo donde se registran los logs
        logging.StreamHandler()  # Consola para monitorear las operaciones
    ]
)

# Configuración de la base de datos MySQL
db = MySQLDatabase(
    "1dam",  # Nombre de la base de datos
    user="usuario",  # Usuario de MySQL
    password="usuario",  # Contraseña de MySQL
    host="localhost",  # Host (generalmente localhost)
    port=3306  # Puerto por defecto de MySQL
)

# Modelo para la tabla Proveedor
class Proveedor(Model):
    nombre = CharField()  # Nombre del proveedor
    direccion = CharField()  # Dirección o contacto del proveedor

    class Meta:
        database = db  # Asocia este modelo con la base de datos configurada

# Modelo para la tabla Herramienta
class Herramienta(Model):
    nombre = CharField()  # Nombre de la herramienta
    tipo = CharField()  # Tipo de herramienta (manual, eléctrico, etc.)
    marca = CharField()  # Marca de la herramienta
    uso = CharField()  # Uso principal de la herramienta
    material = CharField()  # Material principal de la herramienta
    proveedor = ForeignKeyField(Proveedor, backref='herramientas')  # Relación con Proveedor

    class Meta:
        database = db  # Asocia este modelo con la base de datos configurada

# Clase para manejar la base de datos con Peewee
class DatabaseManagerORM:
    def __init__(self):
        self.db = db

    def conectar(self):
        """Conecta la base de datos y crea las tablas."""
        self.db.connect()  # Conecta a la base de datos
        self.db.create_tables([Proveedor, Herramienta])  # Crea las tablas necesarias
        logging.info("Conexión establecida y tablas creadas.")

    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        if not self.db.is_closed():
            self.db.close()
            logging.info("Conexión cerrada.")

    def iniciar_transaccion(self):
        """Inicia una transacción."""
        self.db.begin()
        logging.info("Transacción iniciada.")

    def confirmar_transaccion(self):
        """Confirma (commit) una transacción."""
        self.db.commit()
        logging.info("Transacción confirmada.")

    def revertir_transaccion(self):
        """Revierte (rollback) una transacción."""
        self.db.rollback()
        logging.info("Transacción revertida.")

    def crear_proveedor(self, nombre, direccion):
        """Inserta un nuevo proveedor."""
        proveedor = Proveedor.create(nombre=nombre, direccion=direccion)
        logging.info(f"Proveedor creado: {proveedor.nombre} - {proveedor.direccion}")
        return proveedor

    def crear_herramienta(self, nombre, tipo, marca, uso, material, proveedor):
        """Inserta una nueva herramienta asociada a un proveedor."""
        herramienta = Herramienta.create(
            nombre=nombre, tipo=tipo, marca=marca, uso=uso, material=material, proveedor=proveedor
        )
        logging.info(f"Herramienta creada: {herramienta.nombre} - {herramienta.tipo}")
        return herramienta

    def leer_herramientas(self):
        """Lee todas las herramientas y sus proveedores."""
        herramientas = Herramienta.select()
        logging.info("Leyendo herramientas:")
        for herramienta in herramientas:
            logging.info(f"{herramienta.nombre} - {herramienta.tipo} ({herramienta.proveedor.nombre})")
        return herramientas

    def actualizar_proveedor(self, nombre_proveedor, nueva_direccion):
        """Actualiza la dirección de un proveedor dado su nombre."""
        try:
            proveedor = Proveedor.get(Proveedor.nombre == nombre_proveedor)
            proveedor.direccion = nueva_direccion
            proveedor.save()
            logging.info(f"Proveedor '{nombre_proveedor}' actualizado a la dirección '{nueva_direccion}'.")
        except Proveedor.DoesNotExist:
            logging.error(f"No se encontró el proveedor con el nombre '{nombre_proveedor}'.")

    def eliminar_proveedor(self, nombre_proveedor):
        """Elimina un proveedor por su nombre."""
        try:
            proveedor = Proveedor.get(Proveedor.nombre == nombre_proveedor)
            proveedor.delete_instance()
            logging.info(f"Proveedor '{nombre_proveedor}' eliminado.")
        except Proveedor.DoesNotExist:
            logging.error(f"No se encontró el proveedor con el nombre '{nombre_proveedor}'.")

    def actualizar_herramienta(self, nombre_herramienta, nuevo_tipo):
        """Actualiza el tipo de una herramienta dada."""
        try:
            herramienta = Herramienta.get(Herramienta.nombre == nombre_herramienta)
            herramienta.tipo = nuevo_tipo
            herramienta.save()
            logging.info(f"Herramienta '{nombre_herramienta}' actualizada al tipo '{nuevo_tipo}'.")
        except Herramienta.DoesNotExist:
            logging.error(f"No se encontró la herramienta con el nombre '{nombre_herramienta}'.")

    def eliminar_herramienta(self, nombre_herramienta):
        """Elimina una herramienta por su nombre."""
        try:
            herramienta = Herramienta.get(Herramienta.nombre == nombre_herramienta)
            herramienta.delete_instance()
            logging.info(f"Herramienta '{nombre_herramienta}' eliminada.")
        except Herramienta.DoesNotExist:
            logging.error(f"No se encontró la herramienta con el nombre '{nombre_herramienta}'.")
            
    def leer_herramientas_por_proveedor(self, proveedor_nombre):
        """
        Muestra las herramientas asociadas a un proveedor específico.
        :param proveedor_nombre: Nombre del proveedor cuyas herramientas queremos leer.
        :return: Lista de herramientas asociadas al proveedor.
        """
    # Busca el proveedor por nombre
        proveedor = Proveedor.get_or_none(Proveedor.nombre == proveedor_nombre)
    
        if proveedor:
        # Filtra las herramientas asociadas al proveedor
            herramientas = Herramienta.select().where(Herramienta.proveedor == proveedor)
            logging.info(f"Herramientas asociadas al proveedor {proveedor_nombre}:")
            for herramienta in herramientas:
                logging.info(f"Nombre: {herramienta.nombre}, Tipo: {herramienta.tipo}")
            return herramientas
        else:
            logging.warning(f"No se encontró un proveedor con el nombre '{proveedor_nombre}'.")
            return None        

# Código de ejemplo para utilizar la clase DatabaseManagerORM
if __name__ == "__main__":
    manager = DatabaseManagerORM()
    manager.conectar()

    # Crear los proveedores
    proveedor_a = manager.crear_proveedor("Proveedor A", "123-456-789")
    proveedor_b = manager.crear_proveedor("Proveedor B", "987-654-321")

    # Actualizar el contacto del Proveedor A
    manager.actualizar_proveedor("Proveedor A", "77865330A")

    # Eliminar el Proveedor B
    manager.eliminar_proveedor("Proveedor B")

    # Crear herramientas asociadas al Proveedor A
    manager.crear_herramienta("Martillo", "Manual", "Marca A", "Construcción", "Acero", proveedor_a)
    manager.crear_herramienta("Taladro", "Eléctrico", "Marca B", "Reparaciones", "Plástico", proveedor_a)

    # Actualizar el tipo de herramienta Martillo a "Reforzado"
    manager.actualizar_herramienta("Martillo", "Reforzado")

    # Eliminar la herramienta Taladro
    manager.eliminar_herramienta("Taladro")

    # Verificar las herramientas restantes
    manager.leer_herramientas_por_proveedor("Proveedor A")

    manager.desconectar()


    
