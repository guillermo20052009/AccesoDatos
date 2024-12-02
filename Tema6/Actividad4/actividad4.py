import logging
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager_coche.log"),  # Logs guardados en un archivo
        logging.StreamHandler(),  # Logs también en consola
    ]
)

class DatabaseManagerCoche:
    def __init__(self, uri, database_name, collection_name):
        """Inicializa el componente DatabaseManagerCoche."""
        self.uri = uri
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def conectar(self):
        """Conectar a la base de datos MongoDB"""
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]
            logging.info(f"Conectado a MongoDB: {self.database_name}.{self.collection_name}")
        except PyMongoError as e:
            logging.error(f"Error al conectar a MongoDB: {e}")

    def desconectar(self):
        """Cerrar la conexión a MongoDB"""
        if self.client:
            self.client.close()
            logging.info("Conexión a MongoDB cerrada.")

    def crear_coche(self, coche):
        """Insertar un nuevo coche en la colección"""
        try:
            result = self.collection.insert_one(coche)
            logging.info(f"Coche insertado con ID: {result.inserted_id}")
            return result.inserted_id
        except PyMongoError as e:
            logging.error(f"Error al insertar el coche: {e}")

    def leer_coches(self, filtro={}):
        """Leer coches de la colección según un filtro"""
        try:
            coches = list(self.collection.find(filtro))
            logging.info(f"Coches recuperados: {len(coches)}")
            for coche in coches:
                logging.info(coche)
            return coches
        except PyMongoError as e:
            logging.error(f"Error al leer los coches: {e}")
            return []

    def actualizar_coche(self, filtro, actualizacion):
        """Actualizar un coche en la colección"""
        try:
            result = self.collection.update_one(filtro, {"$set": actualizacion})
            if result.modified_count > 0:
                logging.info(f"Coche actualizado: {filtro}")
            else:
                logging.warning(f"No se encontró coche para actualizar: {filtro}")
        except PyMongoError as e:
            logging.error(f"Error al actualizar el coche: {e}")

    def eliminar_coche(self, filtro):
        """Eliminar un coche de la colección"""
        try:
            result = self.collection.delete_one(filtro)
            if result.deleted_count > 0:
                logging.info(f"Coche eliminado: {filtro}")
            else:
                logging.warning(f"No se encontró coche para eliminar: {filtro}")
        except PyMongoError as e:
            logging.error(f"Error al eliminar el coche: {e}")

    def iniciar_transaccion(self):
        """Iniciar una transacción"""
        try:
            self.session = self.client.start_session()
            self.session.start_transaction()
            logging.info("Transacción iniciada.")
        except PyMongoError as e:
            logging.error(f"Error al iniciar la transacción: {e}")

    def confirmar_transaccion(self):
        """Confirmar (commit) una transacción"""
        try:
            if self.session:
                self.session.commit_transaction()
                logging.info("Transacción confirmada.")
        except PyMongoError as e:
            logging.error(f"Error al confirmar la transacción: {e}")

    def revertir_transaccion(self):
        """Revertir (rollback) una transacción"""
        try:
            if self.session:
                self.session.abort_transaction()
                logging.info("Transacción revertida.")
        except PyMongoError as e:
            logging.error(f"Error al revertir la transacción: {e}")

# Ejemplo de uso del componente DatabaseManagerCoche
if __name__ == "__main__":
    # Configurar el componente
    db_manager = DatabaseManagerCoche(
        uri="mongodb://localhost:27017",
        database_name="1dam",
        collection_name="coches"
    )

    db_manager.conectar()

    try:
        # Crear coches dentro de una transacción
        db_manager.iniciar_transaccion()
        db_manager.crear_coche({"marca": "Toyota", "modelo": "Corolla", "anio": 2020, "color": "Rojo"})
        db_manager.crear_coche({"marca": "Honda", "modelo": "Civic", "anio": 2021, "color": "Azul"})
        db_manager.confirmar_transaccion()

        # Leer todos los coches
        db_manager.leer_coches()

        # Actualizar un coche
        db_manager.iniciar_transaccion()
        db_manager.actualizar_coche({"marca": "Toyota", "modelo": "Corolla"}, {"color": "Negro"})
        db_manager.confirmar_transaccion()

        # Eliminar un coche
        db_manager.iniciar_transaccion()
        db_manager.eliminar_coche({"marca": "Honda", "modelo": "Civic"})
        db_manager.confirmar_transaccion()

    except Exception as e:
        logging.error(f"Error general: {e}")
        db_manager.revertir_transaccion()

    finally:
        db_manager.desconectar()
