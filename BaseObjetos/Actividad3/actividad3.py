import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Definición de la clase Coche para almacenar datos persistentes en ZODB
class Coche(Persistent):
    def __init__(self, nombre, modelo, año, tipo):
        self.nombre = nombre  # Nombre de la marca del coche
        self.modelo = modelo  # Modelo del coche
        self.año = año        # Año de fabricación
        self.tipo = tipo      # Tipo de combustible

# Abrir la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()  # Acceso al diccionario raíz

# Crear tres coches y añadirlos a la base de datos si no existen ya
if '208' not in root:
    coche = Coche('Peugeot', '208', 2002, 'Diesel')
    root['208'] = coche  # Guardar el coche bajo la clave '208'
if 'e36' not in root:
    coche = Coche('BMW', 'e36', 2002, 'Diesel')
    root['e36'] = coche  # Guardar el coche bajo la clave 'e36'
if 'modely' not in root:
    coche = Coche('Tesla', 'Modely', 2022, 'Eléctrico')
    root['Modely'] = coche  # Guardar el coche bajo la clave 'Modely'
transaction.commit()  # Confirmar los cambios en la base de datos

print("Coches añadidos correctamente")

# Recuperar el coche con la clave 'e36' y modificar su modelo
coche = root.get('e36')
if coche:
    print("\nAntes de la modificación")
    print(f"Nombre: {coche.nombre}, Modelo: {coche.modelo}, Año: {coche.año}, Tipo: {coche.tipo}")

    # Modificar el modelo del coche e36
    coche.modelo = 'e36 cambiado'
    transaction.commit()  # Confirmar el cambio en la base de datos

    print("\nDespués de la modificación")
    print(f"Nombre: {coche.nombre}, Modelo: {coche.modelo}, Año: {coche.año}, Tipo: {coche.tipo}")
else:
    print("El coche no se encontró en la base de datos")

# Cerrar la conexión y la base de datos
connection.close()
db.close()
