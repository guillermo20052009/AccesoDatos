import logging
import transaction
from ZODB import DB, FileStorage
from persistent import Persistent

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager_object.log"),  # Logs guardados en un archivo
        logging.StreamHandler(),  # Logs también en consola
    ]
)


class Coche(Persistent):
    """Clase que representa un coche."""
    def __init__(self, modelo, marca, anio, color, tipo):
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.color = color
        self.tipo = tipo

class DatabaseManagerObject:
    """Componente para gestionar bases de datos orientadas a objetos con ZODB."""
    def __init__(self, filepath="coches.fs"):
        self.filepath = filepath
        self.db = None
        self.connection = None
        self.root = None
        self.transaccion_iniciada = False

    def conectar(self):
        """Conecta a la base de datos ZODB."""
        try:
            storage = FileStorage.FileStorage(self.filepath)
            self.db = DB(storage)
            self.connection = self.db.open()
            self.root = self.connection.root()
            if "coches" not in self.root:
                self.root["coches"] = {}
            transaction.commit()
            logging.info("Conexión establecida con ZODB.")
        except Exception as e:
            logging.error(f"Error al conectar a ZODB: {e}")

    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        try:
            if self.connection:
                self.connection.close()
            self.db.close()
            logging.info("Conexión a ZODB cerrada.")
        except Exception as e:
            logging.error(f"Error al cerrar la conexión a ZODB: {e}")

    def iniciar_transaccion(self):
        """Inicia una transacción."""
        try:
            transaction.begin()
            self.transaccion_iniciada = True
            logging.info("Transacción iniciada.")
        except Exception as e:
            logging.error(f"Error al iniciar la transacción: {e}")

    def confirmar_transaccion(self):
        """Confirma la transacción."""
        if self.transaccion_iniciada:
            try:
                transaction.commit()
                self.transaccion_iniciada = False
                logging.info("Transacción confirmada.")
            except Exception as e:
                logging.error(f"Error al confirmar la transacción: {e}")

    def revertir_transaccion(self):
        """Revierte la transacción."""
        if self.transaccion_iniciada:
            try:
                transaction.abort()
                self.transaccion_iniciada = False
                logging.info("Transacción revertida.")
            except Exception as e:
                logging.error(f"Error al revertir la transacción: {e}")

    def crear_coche(self, id, modelo, marca, anio, color, tipo):
        """Crea y almacena un nuevo coche."""
        try:
            if id in self.root["coches"]:
                raise ValueError(f"Ya existe un coche con ID {id}.")
            self.root["coches"][id] = Coche(modelo, marca, anio, color, tipo)
            logging.info(f"Coche con ID {id} creado exitosamente.")
        except Exception as e:
            self.revertir_transaccion()
            logging.error(f"Error al crear el coche con ID {id}: {e}")

    def leer_coches(self):
        """Lee y muestra todos los coches almacenados."""
        try:
            coches = self.root["coches"]
            for id, coche in coches.items():
                logging.info(
                    f"ID: {id}, Modelo: {coche.modelo}, Marca: {coche.marca}, Año: {coche.anio}, "
                    f"Color: {coche.color}, Tipo: {coche.tipo}"
                )
            return coches
        except Exception as e:
            logging.error(f"Error al leer los coches: {e}")

    def actualizar_coche(self, id, modelo, marca, anio, color, tipo):
        """Actualiza los atributos de un coche."""
        try:
            coche = self.root["coches"].get(id)
            if not coche:
                raise ValueError(f"No existe un coche con ID {id}.")
            coche.modelo = modelo
            coche.marca = marca
            coche.anio = anio
            coche.color = color
            coche.tipo = tipo
            logging.info(f"Coche con ID {id} actualizado exitosamente.")
        except Exception as e:
            logging.error(f"Error al actualizar el coche con ID {id}: {e}")

    def eliminar_coche(self, id):
        """Elimina un coche por su ID."""
        try:
            if id not in self.root["coches"]:
                raise ValueError(f"No existe un coche con ID {id}.")
            del self.root["coches"][id]
            logging.info(f"Coche con ID {id} eliminado exitosamente.")
        except Exception as e:
            self.revertir_transaccion()
            logging.error(f"Error al eliminar el coche con ID {id}: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración del componente
    db_manager = DatabaseManagerObject(filepath="coches.fs")
    db_manager.conectar()

    try:
        # Insertar tres coches (controlado con transacciones)
        db_manager.iniciar_transaccion()
        db_manager.crear_coche(1, "Modelo S", "Tesla", 2020, "Rojo", "Eléctrico")
        db_manager.crear_coche(2, "Civic", "Honda", 2019, "Azul", "Sedán")
        db_manager.crear_coche(3, "Mustang", "Ford", 2022, "Negro", "Deportivo")
        db_manager.confirmar_transaccion()

        # Mostrar todos los coches
        print("Coches actuales en la base de datos:")
        db_manager.leer_coches()

        # Intentar insertar un coche con un ID ya creado (controlado con transacciones)
        db_manager.iniciar_transaccion()
        db_manager.crear_coche(1, "Corolla", "Toyota", 2021, "Blanco", "Sedán")  # ID duplicado
        db_manager.confirmar_transaccion()

    except Exception as e:
        logging.error(f"Error general: {e}")
        db_manager.revertir_transaccion()

    try:
        # Mostrar todos los coches después del intento de inserción fallido
        print("\nCoches después de intentar insertar un ID duplicado:")
        db_manager.leer_coches()

        # Actualizar un coche cambiando cualquier atributo (controlado con transacciones)
        db_manager.iniciar_transaccion()
        db_manager.actualizar_coche(2, "Civic", "Honda", 2020, "Azul", "Híbrido")  # Cambio en tipo
        db_manager.confirmar_transaccion()

        # Mostrar todos los coches después de la actualización
        print("\nCoches después de la actualización:")
        db_manager.leer_coches()

        # Intentar eliminar un coche con un ID que no exista (controlado con transacciones)
        db_manager.iniciar_transaccion()
        db_manager.eliminar_coche(10)  # ID no existente
        db_manager.confirmar_transaccion()

    except Exception as e:
        logging.error(f"Error general: {e}")
        db_manager.revertir_transaccion()

    # Mostrar todos los coches después del intento de eliminación de un ID no existente
    print("\nCoches después de intentar eliminar un ID no existente:")
    db_manager.leer_coches()
    
    # Desconectar
    db_manager.desconectar()
