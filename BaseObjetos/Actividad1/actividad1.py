import ZODB, ZODB.FileStorage, transaction
# Establecer conexión a la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('1dam.fs') # Almacenamiento en archivo
db = ZODB.DB(storage)
connection = db.open()
root = connection.root() # Diccionario raíz para acceder a los objetos almacenados
# Almacenar una lista simple en la base de datos
root['mi_lista'] = ['BMW', 'Mercedes', 'Mazda']
transaction.commit() # Confirmar los cambios para que sean persistentes
# Recuperar la lista almacenada y mostrarla
print(root['mi_lista']) # Salida: ['Martillo', 'Taladro', 'Destornillador']
# Cerrar la conexión y la base de datos
connection.close()
db.close()