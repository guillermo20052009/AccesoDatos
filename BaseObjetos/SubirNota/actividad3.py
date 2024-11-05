import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Definición de la clase Movil
class Movil(Persistent):
    def __init__(self, marca, modelo, anio_lanzamiento, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.anio_lanzamiento = anio_lanzamiento
        self.sistema_operativo = sistema_operativo

# Establecer conexión a la base de datos ZODB
storage = ZODB.FileStorage.FileStorage('moviles.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()   

if not hasattr(root, 'moviles'):
    root.moviles = {}

# Recuperar y modificar un objeto
movil = root['moviles'].get("movil1")

if movil:
    print("Antes de la modificación:")
    print(f"Marca: {movil.marca}, Modelo: {movil.modelo}, Año de lanzamiento: {movil.anio_lanzamiento}, Sistema Operativo: {movil.sistema_operativo}")
    
    # Modificar el atributo 'sistema_operativo'
    movil.sistema_operativo = 'Android raro Cambio demostracionnnnn'
    
    # Imprimir el sistema operativo antes de confirmar los cambios
    
    transaction.commit()  # Confirmar los cambios en la base de datos
    
    print("Después de la modificación:")
    print(f"Marca: {movil.marca}, Modelo: {movil.modelo}, Año de lanzamiento: {movil.anio_lanzamiento}, Sistema Operativo: {movil.sistema_operativo}")

else:
    print("el movil no se encontró en la base de datos.")
# Cerrar la conexión
connection.close()
db.close()
