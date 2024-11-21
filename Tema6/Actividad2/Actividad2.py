import logging
import mysql.connector
from mysql.connector import Error

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("databasemanager.log"),  # Logs guardados en un archivo
        logging.StreamHandler(),  # Logs también en consola
    ]
)

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """Conectar a la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logging.info("Conexión exitosa a la base de datos.")
        except Error as e:
            logging.error(f"Error al conectar a la base de datos: {e}")

    def desconectar(self):
        """Cerrar la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logging.info("Conexión cerrada.")

    def crear_coche(self, marca, modelo, año, color, tipo):
        """Insertar un nuevo coche en la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO Coches (marca, modelo, año, color, tipo)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (marca, modelo, año, color, tipo))
            logging.info(f"Coche '{modelo}' insertado exitosamente.")
        except Error as e:
            logging.error(f"Error al insertar el coche '{modelo}': {e}")

    def leer_coches(self):
        """Leer todos los coches de la base de datos"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Coches")
            coches = cursor.fetchall()
            logging.info("Coches recuperados:")
            for coche in coches:
                logging.info(coche)
            return coches
        except Error as e:
            logging.error(f"Error al leer los coches: {e}")
            return None

    def actualizar_coche(self, id, marca, modelo, año, color, tipo):
        """Actualizar un coche en la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Coches
            SET marca = %s, modelo = %s, año = %s, color = %s, tipo = %s
            WHERE id = %s
            """
            cursor.execute(query, (marca, modelo, año, color, tipo, id))
            self.connection.commit()
            logging.info(f"Coche con ID {id} actualizado exitosamente.")
        except Error as e:
            logging.error(f"Error al actualizar el coche con ID {id}: {e}")

    def eliminar_coche(self, id):
        """Eliminar un coche de la base de datos"""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Coches WHERE id = %s"
            cursor.execute(query, (id,))
            self.connection.commit()
            logging.info(f"Coche con ID {id} eliminado exitosamente.")
        except Error as e:
            logging.error(f"Error al eliminar el coche con ID {id}: {e}")

    def iniciar_transaccion(self):
        """Iniciar una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.start_transaction()
                logging.info("Transacción iniciada.")
        except Error as e:
            logging.error(f"Error al iniciar la transacción: {e}")

    def confirmar_transaccion(self):
        """Confirmar (commit) una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.commit()
                logging.info("Transacción confirmada.")
        except Error as e:
            logging.error(f"Error al confirmar la transacción: {e}")

    def revertir_transaccion(self):
        """Revertir (rollback) una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.rollback()
                logging.info("Transacción revertida.")
        except Error as e:
            logging.error(f"Error al revertir la transacción: {e}")

# Ejemplo de uso del componente DatabaseManager
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "usuario", "usuario", "1dam")
    db_manager.conectar()

    # Insertar un nuevo coche
    db_manager.crear_coche("Toyota", "Corolla", 2020, "Blanco", "Sedán")

    # Leer todos los coches
    db_manager.leer_coches()

    # Actualizar un coche
    db_manager.actualizar_coche(1, "Toyota", "Corolla", 2021, "Negro", "Sedán")

    # Eliminar un coche
    db_manager.eliminar_coche(1)

    # Gestionar transacciones
    db_manager.iniciar_transaccion()
    db_manager.crear_coche("Honda", "Civic", 2022, "Rojo", "Hatchback")
    db_manager.revertir_transaccion()  # No se guardará la inserción
    db_manager.desconectar()
