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

# Clase para gestionar la conexión y operaciones con la base de datos
class DatabaseManager:
    def __init__(self, host, user, password, database):
        """
        Inicializa el gestor de la base de datos con los parámetros de conexión.
        """
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
                logging.info("Conexión exitosa a la base de datos.")  # Registro de éxito
        except Error as e:
            logging.error(f"Error al conectar a la base de datos: {e}")  # Registro de error

    def desconectar(self):
        """Cerrar la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()  # Cierra la conexión
            logging.info("Conexión cerrada.")  # Registro de desconexión exitosa

    def crear_coche(self, marca, modelo, año, color, tipo):
        """Insertar un nuevo coche en la base de datos"""
        try:
            cursor = self.connection.cursor()  # Crea un cursor para ejecutar consultas
            query = """
            INSERT INTO Coches (marca, modelo, año, color, tipo)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (marca, modelo, año, color, tipo))  # Ejecuta la consulta de inserción
            logging.info(f"Coche '{modelo}' insertado exitosamente.")  # Registro de éxito
        except Error as e:
            logging.error(f"Error al insertar el coche '{modelo}': {e}")  # Registro de error

    def leer_coches(self):
        """Leer todos los coches de la base de datos"""
        try:
            cursor = self.connection.cursor(dictionary=True)  # Usa cursor para obtener resultados en formato dict
            cursor.execute("SELECT * FROM Coches")  # Consulta para obtener todos los coches
            coches = cursor.fetchall()  # Recupera todos los registros
            logging.info("Coches recuperados:")  # Registro de información
            for coche in coches:
                logging.info(coche)  # Imprime cada coche recuperado
            return coches  # Devuelve los datos recuperados
        except Error as e:
            logging.error(f"Error al leer los coches: {e}")  # Registro de error
            return None

    def actualizar_coche(self, id, marca, modelo, año, color, tipo):
        """Actualizar un coche en la base de datos"""
        try:
            cursor = self.connection.cursor()  # Cursor para ejecutar consultas
            query = """
            UPDATE Coches
            SET marca = %s, modelo = %s, año = %s, color = %s, tipo = %s
            WHERE id = %s
            """
            cursor.execute(query, (marca, modelo, año, color, tipo, id))  # Ejecuta la consulta de actualización
            self.connection.commit()  # Guarda los cambios
            logging.info(f"Coche con ID {id} actualizado exitosamente.")  # Registro de éxito
        except Error as e:
            logging.error(f"Error al actualizar el coche con ID {id}: {e}")  # Registro de error

    def eliminar_coche(self, id):
        """Eliminar un coche de la base de datos"""
        try:
            cursor = self.connection.cursor()  # Cursor para ejecutar consultas
            query = "DELETE FROM Coches WHERE id = %s"  # Consulta de eliminación
            cursor.execute(query, (id,))  # Ejecuta la consulta con el ID proporcionado
            self.connection.commit()  # Guarda los cambios
            logging.info(f"Coche con ID {id} eliminado exitosamente.")  # Registro de éxito
        except Error as e:
            logging.error(f"Error al eliminar el coche con ID {id}: {e}")  # Registro de error

    def iniciar_transaccion(self):
        """Iniciar una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.start_transaction()  # Inicia una transacción
                logging.info("Transacción iniciada.")  # Registro de inicio de transacción
        except Error as e:
            logging.error(f"Error al iniciar la transacción: {e}")  # Registro de error

    def confirmar_transaccion(self):
        """Confirmar (commit) una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.commit()  # Confirma los cambios
                logging.info("Transacción confirmada.")  # Registro de confirmación exitosa
        except Error as e:
            logging.error(f"Error al confirmar la transacción: {e}")  # Registro de error

    def revertir_transaccion(self):
        """Revertir (rollback) una transacción"""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.rollback()  # Revertir los cambios
                logging.info("Transacción revertida.")  # Registro de reversión
        except Error as e:
            logging.error(f"Error al revertir la transacción: {e}")  # Registro de error

# Ejemplo de uso del componente DatabaseManager
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "usuario", "usuario", "1dam")  # Configuración de conexión
    db_manager.conectar()  # Conectar a la base de datos

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
    db_manager.desconectar()  # Cierra la conexión
