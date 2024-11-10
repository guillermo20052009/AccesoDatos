import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Definición de la clase Coche para almacenar datos persistentes en ZODB
class Coche(Persistent):
    def __init__(self, nombre, modelo, año, tipo):
        self.nombre = nombre  # Nombre de la marca del coche
        self.modelo = modelo  # Modelo del coche
        self.año = año        # Año de fabricación
        self.tipo = tipo      # Tipo de combustible

# Establecer conexión con la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()  # Acceso al diccionario raíz

# Almacenar una lista de objetos Coche en la base de datos
cochelista = [
    Coche('Seat', 'Ibiza', 2010, 'gasolina'),
    Coche('Mercedes', 'Clase A', 2015, 'diésel'),
    Coche('BMW', 'Serie 3', 2018, 'gasolina')
]
root['coches'] = cochelista  # Guardar la lista en la clave 'coches'
transaction.commit()  # Confirmar los cambios en la base de datos

# Recuperar y mostrar los coches almacenados
for coche in root['coches']:  # Iteramos en la lista de coches
    if hasattr(coche, 'nombre'):  # Verificamos si el objeto tiene el atributo 'nombre'
        print('Objeto con nombre')
        if coche.nombre == 'Mercedes':  # Comprobamos si el coche es un Mercedes
            print(coche.nombre, coche.modelo, coche.año, coche.tipo + "\n")
        else:
            print("Pero no es Mercedes\n")
    else:
        print('Objeto sin nombre\n')  # En caso de que no tenga el atributo 'nombre'
