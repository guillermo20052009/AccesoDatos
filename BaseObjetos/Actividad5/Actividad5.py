import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Define las clases Coche y Motor para almacenar datos persistentes en ZODB
class Coche(Persistent):
    def __init__(self, nombre, modelo, año, tipo, nombre_motor):
        # Atributos de la clase Coche
        self.nombre = nombre  # Nombre del coche (marca)
        self.modelo = modelo  # Modelo del coche
        self.año = año        # Año de fabricación
        self.tipo = tipo      # Tipo de combustible
        self.nombre_motor = nombre_motor  # Motor asociado al coche (clave de motor)

class Motor(Persistent):
    def __init__(self, nombre, potencia, año):
        # Atributos de la clase Motor
        self.nombre = nombre  # Nombre del motor (v5, v8, etc.)
        self.potencia = potencia  # Potencia del motor
        self.año = año        # Año de fabricación del motor

# Abrir y conectar la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')  # Crea un archivo de almacenamiento ZODB
db = ZODB.DB(storage)  # Abre la base de datos en el almacenamiento
connection = db.open()  # Abre una conexión a la base de datos
root = connection.root()  # Obtiene el nodo raíz para almacenar y acceder a los datos

# Inicializa los diccionarios 'coches' y 'motor' en la base de datos si no existen
if 'coches' not in root:
    root['coches'] = {}  # Diccionario para almacenar objetos Coche

if 'motor' not in root:
    root['motor'] = {}  # Diccionario para almacenar objetos Motor

# Agregar registros de motores a la base de datos
root['motor']['v5'] = Motor('v5', 190, "2001")  # Motor v5 con potencia 190 y año 2001
root['motor']['v8'] = Motor('v8', 210, "2002")  # Motor v8 con potencia 210 y año 2002
root['motor']['1800'] = Motor('1800', 150, "2003")  # Motor 1800 con potencia 150 y año 2003

# Agregar registros de coches y enlazarlas con los motores correspondientes
root['coches']['208'] = Coche('Peugeot', '208', 2002, 'Diesel', "v5")  # Coche asociado al motor v5
root['coches']['e36'] = Coche('BMW', 'e36', 2002, 'Diesel', "v5")  # Coche asociado al motor v5
root['coches']['Modely'] = Coche('Tesla', 'Modely', 2022, 'Electrico', "v8")  # Coche asociado al motor v8

transaction.commit()  # Guarda los cambios en la base de datos

print("\nRegistros introducidos correctamente")

# Consulta los coches con motor 'v5'
print("\nCoches v5:\n")

# Filtra los coches que tienen un motor v5
coches_v5 = [
    coche for coche in root['coches'].values()  # Recorre todos los coches
    if coche.nombre_motor == "v5"  # Filtra por el motor v5
]

# Imprime los coches con motor v5
for coche in coches_v5:
   print(f"Nombre: {coche.nombre}, Modelo: {coche.modelo}, Año: {coche.año}, tipo: {coche.tipo}, motor: {coche.nombre_motor}")

transaction.commit()  # Asegura que los cambios se mantengan

# Cerrar la conexión y la base de datos
connection.close()
db.close()
