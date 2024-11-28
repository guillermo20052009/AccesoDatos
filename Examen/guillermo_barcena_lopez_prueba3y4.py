from peewee import MySQLDatabase, CharField, IntegerField, Model, PrimaryKeyField,IntegrityError
import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent



# Configuración de la base de datos
db = MySQLDatabase(
    '1dam',  # Nombre de la base de datos
    user='usuario',  # Nombre de usuario para la base de datos
    password='usuario',  # Contraseña del usuario
    host='localhost',  # Servidor de la base de datos
    port=3306  # Puerto donde escucha MySQL (3306 es el predeterminado)
)

# Conectarse a la base de datos
db.connect()
print("Conexión exitosa a la base de datos\n")

# La clase Libro define cómo será la estructura de la tabla en la base de datos
class Libro(Model):
    id = PrimaryKeyField()  
    titulo = CharField(100)  
    autor = CharField(100)  
    anio_publicacion = IntegerField()  
    genero = CharField(50) 
   
    
    # Configuración adicional de la tabla en la base de datos
    class Meta:
        database = db
        db_table = 'libros'  # Nombre de la tabla en la base de datos
        
# Clase para la gestion de prestamos, la administraremos con ZODB
class Prestamo(Persistent):
    def __init__(self,id ,id_libro, nombre_usuario, fecha_prestamo, fecha_devolucion):
        self.id=id
        self.libro_id = id_libro 
        self.nombre_usuario = nombre_usuario  
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

#Asignar el archivo que controlará la base de datos
storage = ZODB.FileStorage.FileStorage('1dam.fs')
dbZ = ZODB.DB(storage)
connection = dbZ.open()
root = connection.root() 

# Funcion que introduce los datos de los prestamos en el archivo .fs, el parametro es una lista de Prestamo, utilizaremos transacciones para manejar los errores y la integridad de los datos
def introducir_datos_ZODB(prestamos):
    try:
        print("Transacción Iniciada")
        root['prestamos'] = prestamos  
        transaction.commit()
        print('Datos insertados con exito')
        print("Transacción completada\n")
    except Exception as e:
        transaction.abort()  # Revertir cambios en caso de error
        print(f"Error durante la transacción, cambios no realizados: {e}\n")

# Funcion que se encarga de crear la tabla
def crear_tabla():
    Libro.create_table()  
    print("Tabla creada con éxito\n")
    
    
# Funcion que se encarga de insertar un Libro en la tabla
def insertar_datos(libro):
    Libro.create(titulo=libro.get("titulo"),autor=libro.get("autor"),anio_publicacion=libro.get("anio_publicacion"),genero=libro.get("genero"))  # Inserta una nueva fila
    print("Libro insertado con éxito")
    
# Funcion que filtrará los prestamos de libros que sean del genero que le pasemos por parametro, si el genero no existe se informará
def buscar_prestamos_por_genero(genero):
    cont=0
    if comprobar_genero(genero):
        novelas = Libro.select().where(Libro.genero == genero)
        lista_novelas = crear_lista_id(novelas)
        if len(lista_novelas) > 0:
            for prestamo in root['prestamos']:
                if hasattr(prestamo, 'libro_id'):  
                    if prestamo.libro_id in lista_novelas:
                        print(prestamo.id,prestamo.libro_id, prestamo.nombre_usuario, prestamo.fecha_prestamo, prestamo.fecha_devolucion)
                        cont+=1
            if cont==0:
                print('No hay prestamos de ese genero')
    else:
        print('Ese genero no existe')
        
    

# Funcion utilizada para obtener la lista de id cuando hagamos una consulta, es utilizada en la linea 76, para filtrar los prestamos que tengan ese id de libro
def crear_lista_id(novelas):
    novela_lista=[]
    for novela in novelas:
        novela_lista.append(novela.id)
    return novela_lista


# Comprueba que el genero que le pasamos por parametro existe, es utilizada en la linea 74, para proceder con la consulta
def comprobar_genero(genero):
    libros = Libro.select()  
    for libro in libros:
        if libro.genero == genero:
            return True
    return False


# lista de libros a introducir
libros = [
{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'anio_publicacion':
1967, 'genero': 'Novela'},
{'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'anio_publicacion':
1605, 'genero': 'Novela'},
{'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry', 'anio_publicacion': 1943,
'genero': 'Infantil'},
{'titulo': 'Crónica de una muerte anunciada', 'autor': 'Gabriel García Márquez',
'anio_publicacion': 1981, 'genero': 'Novela'},
{'titulo': '1984', 'autor': 'George Orwell', 'anio_publicacion': 1949, 'genero': 'Distopía'}
]

print('----Creacion de tabla y inserccion de datos----')
crear_tabla()
# Control de transacciones y manejo de errores al introducir los datos en la base de datos
try: 
    print('Transaccion Iniciada')
    with db.atomic():
        for libro in libros:
            insertar_datos(libro)
    print('Transaccion Completada')
except IntegrityError as e:
        print(f"Error al insertar herramientas: {e}") 


print('\n----Inserccion de Prestamos en ZODB----')
#Prestamos a introducir
prestamos=[Prestamo(1,1, 'Juan Perez', '2023-10-01', '2023-11-01'),
Prestamo(2,2, 'Ana Lopez', '2023-09-15', '2023-10-15'),
Prestamo(3,4, 'Maria Gomez', '2023-09-20', '2023-10-20'),
Prestamo(4,3, 'Jose Vazquez','2023-10-9','2023-11-9')]

introducir_datos_ZODB(prestamos)

print('\n----Prestamos Totales----')
# Imprimimos todos los prestamos
for prestamo in root['prestamos']:
    if hasattr(prestamo, 'fecha_prestamo'):  
        print(prestamo.id,prestamo.libro_id, prestamo.nombre_usuario, prestamo.fecha_prestamo, prestamo.fecha_devolucion)
       
print('\n----Prestamos por genero----')
buscar_prestamos_por_genero('Novela')