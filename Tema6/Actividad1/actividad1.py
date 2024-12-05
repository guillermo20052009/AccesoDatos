import json
import csv
import logging
import os
from copy import deepcopy

# Configuración de logging para guardar en un archivo y mostrar en consola
logging.basicConfig(
    level=logging.INFO,  # Nivel de log (INFO, WARNING, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log con timestamp
    handlers=[
        logging.FileHandler("log_datos.log"),  # Guardar logs en un archivo llamado 'log_datos.log'
        logging.StreamHandler()               # Mostrar logs en la consola
    ]
)

# Clase para gestionar datos en diferentes formatos (JSON, CSV)
class DataManager:
    def __init__(self, ruta_archivo, tipo_archivo='json'):
        """
        Constructor de la clase DataManager.

        :param ruta_archivo: Ruta del archivo donde se almacenarán los datos.
        :param tipo_archivo: Tipo del archivo (json o csv).
        """
        self.ruta_archivo = ruta_archivo  # Ruta del archivo
        self.tipo_archivo = tipo_archivo  # Tipo del archivo (json o csv)
        self.version = 1  # Versión inicial de los datos
        self.transaccion_activa = False  # Bandera para saber si hay una transacción activa
        self.copia_datos = None  # Copia de seguridad de los datos para revertir transacciones

        # Cargar datos si el archivo existe, o inicializar con una lista vacía si no existe
        if os.path.exists(ruta_archivo):
            self.datos = self._leer_archivo()  # Leer los datos del archivo
            logging.info(f"Archivo {tipo_archivo.upper()} cargado con éxito. Versión actual: {self.version}")
        else:
            self.datos = []  # Inicializar datos como una lista vacía
            self._guardar_archivo()  # Guardar el archivo vacío inicialmente

    def _leer_archivo(self):
        """
        Leer los datos del archivo especificado según su tipo.
        :return: Datos cargados desde el archivo.
        """
        if self.tipo_archivo == 'json':
            # Leer archivo JSON
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        elif self.tipo_archivo == 'csv':
            # Leer archivo CSV
            with open(self.ruta_archivo, mode='r') as archivo:
                lector = csv.DictReader(archivo)
                return [fila for fila in lector]
        else:
            # Tipo de archivo no soportado
            raise ValueError("Tipo de archivo no soportado. Use 'json' o 'csv'.")

    def _guardar_archivo(self):
        """
        Guardar los datos en el archivo especificado según su tipo.
        """
        if self.tipo_archivo == 'json':
            # Guardar archivo JSON
            with open(self.ruta_archivo, 'w') as archivo:
                json.dump(self.datos, archivo, indent=4)
        elif self.tipo_archivo == 'csv' and self.datos:
            # Guardar archivo CSV (requiere que haya datos)
            with open(self.ruta_archivo, mode='w', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.datos[0].keys())
                escritor.writeheader()
                escritor.writerows(self.datos)
        logging.info(f"Archivo {self.tipo_archivo.upper()} guardado. Versión actual: {self.version}")

    def iniciar_transaccion(self):
        """
        Iniciar una transacción para realizar cambios en los datos.
        """
        if self.transaccion_activa:
            raise Exception("Ya hay una transacción activa.")
        self.transaccion_activa = True
        self.copia_datos = deepcopy(self.datos)  # Hacer una copia de los datos actuales
        logging.info("Transacción iniciada.")

    def confirmar_transaccion(self):
        """
        Confirmar y guardar los cambios realizados durante la transacción.
        """
        if not self.transaccion_activa:
            raise Exception("No hay una transacción activa para confirmar.")
        self.version += 1  # Incrementar la versión al confirmar
        self.transaccion_activa = False
        self.copia_datos = None  # Eliminar la copia de seguridad
        self._guardar_archivo()  # Guardar los datos actualizados
        logging.info("Transacción confirmada y cambios guardados.")

    def revertir_transaccion(self):
        """
        Revertir los cambios realizados durante una transacción activa.
        """
        if not self.transaccion_activa:
            raise Exception("No hay una transacción activa para revertir.")
        self.datos = self.copia_datos  # Revertir a la copia original
        self.transaccion_activa = False
        self.copia_datos = None  # Eliminar la copia de seguridad
        logging.warning("Transacción revertida. Los cambios no se guardaron.")

    def leer_dato(self, clave, valor):
        """
        Leer datos que coincidan con una clave y un valor específicos.

        :param clave: Clave a buscar en los datos.
        :param valor: Valor a buscar en los datos.
        :return: Lista de datos que coinciden con la clave y el valor.
        """
        return [dato for dato in self.datos if dato.get(clave) == valor]

    def escribir_dato(self, nuevo_dato):
        """
        Agregar un nuevo dato a los datos existentes.

        :param nuevo_dato: Dato a agregar.
        """
        if not self.transaccion_activa:
            raise Exception("Debe iniciar una transacción antes de realizar cambios.")
        self.datos.append(nuevo_dato)
        logging.info(f"Dato agregado: {nuevo_dato}")

    def eliminar_dato(self, clave, valor):
        """
        Eliminar datos que coincidan con una clave y un valor específicos.

        :param clave: Clave a buscar en los datos.
        :param valor: Valor a buscar para eliminar.
        """
        if not self.transaccion_activa:
            raise Exception("Debe iniciar una transacción antes de realizar cambios.")
        self.datos = [dato for dato in self.datos if dato.get(clave) != valor]
        logging.info(f"Datos con {clave}={valor} eliminados.")

    def obtener_configuracion(self):
        """
        Obtener la configuración actual del DataManager.
        :return: Diccionario con los detalles de configuración.
        """
        return {
            "ruta_archivo": self.ruta_archivo,
            "tipo_archivo": self.tipo_archivo,
            "version": self.version,
            "transaccion_activa": self.transaccion_activa
        }

    def actualizar_configuracion(self, nueva_ruta, nuevo_tipo=None):
        """
        Actualizar la configuración del DataManager.

        :param nueva_ruta: Nueva ruta para el archivo de datos.
        :param nuevo_tipo: Nuevo tipo de archivo (opcional).
        """
        if self.transaccion_activa:
            raise Exception("No se puede cambiar la configuración durante una transacción.")
        self.ruta_archivo = nueva_ruta
        if nuevo_tipo:
            self.tipo_archivo = nuevo_tipo
        logging.info(f"Configuración actualizada. Nueva ruta del archivo: {self.ruta_archivo}")


# Datos de prueba
coches = [{
    "marca": "peugeot",
    "modelo": 2008,
    "Año": 2018,
}, {
    "marca": "toyota",
    "modelo": "corolla",
    "Año": 2018,
}, {
    "marca": "BMW",
    "modelo": "e36",
    "Año": 2018,
}]

# Crear instancia de DataManager para gestionar datos en JSON
data_manager = DataManager("coches.json")

# Iniciar una transacción para agregar datos
data_manager.iniciar_transaccion()
data_manager.escribir_dato(coches[0])
data_manager.escribir_dato(coches[1])
data_manager.escribir_dato(coches[2])
data_manager.confirmar_transaccion()  # Confirmar los cambios

# Cambiar configuración para trabajar con CSV
data_manager.actualizar_configuracion("nuevo.csv", "csv")

# Iniciar otra transacción para trabajar en CSV
data_manager.iniciar_transaccion()
data_manager.escribir_dato(coches[0])
data_manager.escribir_dato(coches[1])
data_manager.escribir_dato(coches[2])
data_manager.confirmar_transaccion()  # Confirmar los cambios
