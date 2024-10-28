import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

class Coche(Persistent):
    def __init__(self, nombre, tipo, material, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.año = material
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

for clave, coche in root.items():
    if hasattr(coche, 'nombre'):
        print('objeto con nombre')
        if (coche.nombre == 'Mercedes'):
            print(coche)
    else:
        print('objeto sin nombre')