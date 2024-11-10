import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Definición de la clase Coche para almacenar datos de coches de forma persistente en ZODB
class Coche(Persistent):
    def __init__(self, nombre, modelo, año, tipo):
        self.nombre = nombre  # Nombre de la marca del coche
        self.modelo = modelo  # Modelo del coche
        self.año = año        # Año de fabricación
        self.tipo = tipo      # Tipo de combustible

# Abrir la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')  # Almacenamiento en archivo
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()  # Acceso al diccionario raíz

# Función para crear y almacenar coches en la base de datos
def crearCoches():
    try:
        print("Transacción Iniciada")
        # Crear un diccionario de coches si no existe ya en la raíz
        if 'coches' not in root:
            root['coches'] = {}  # Diccionario para almacenar coches por identificador
            transaction.commit()  # Confirmar la creación del diccionario

        # Añadir varios objetos Coche al diccionario 'coches'
        root['coches']['208'] = Coche('Peugeot', '208', 2002, 'Diesel')
        root['coches']['e36'] = Coche('BMW', 'e36', 2002, 'Diesel')
        root['coches']['Modely'] = Coche('Tesla', 'Modely', 2022, 'Eléctrico')

        transaction.commit()  # Confirmar los cambios en la base de datos
        print("Transacción completada\n")
    except Exception as e:
        transaction.abort()  # Revertir cambios en caso de error
        print(f"Error durante la transacción, cambios no realizados: {e}\n")

# Llamar a la función para crear los coches
crearCoches()

# Recuperar y mostrar los coches almacenados
print("Coches en la base de datos:")
if 'coches' in root:
    for nombre, coche in root['coches'].items():
        # Imprimir información detallada de cada coche en la base de datos
        print(f"Nombre: {coche.nombre}, Modelo: {coche.modelo}, Año: {coche.año}, Tipo: {coche.tipo}")

# Cerrar la conexión y la base de datos
connection.close()
db.close()
