import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

class Coche(Persistent):
    def __init__(self, nombre,modelo,año,tipo):
        self.nombre = nombre
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
# Establecer conexión
storage = ZODB.FileStorage.FileStorage('1dam.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()
# Almacenar un coche

cochelista=[Coche('seat','ibiza',2010,'gasolina'),Coche('Mercedes','Clase A',2015,'diésel'),Coche('BMW','serie 3',2018,'gasolina')]

root['coches'] = cochelista
transaction.commit()


for coche in root['coches']:  # Iteramos en la lista de coches
    if hasattr(coche, 'nombre'):
        print('objeto con nombre')
        if coche.nombre == 'Mercedes':
            print(coche.nombre, coche.modelo, coche.año, coche.tipo +"\n")
        else:
            print("Pero no es Mercedes\n")
    else:
        print('objeto sin nombre\n')


