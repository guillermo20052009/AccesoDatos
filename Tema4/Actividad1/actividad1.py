from peewee import MySQLDatabase,CharField,IntegerField,Model,PrimaryKeyField,FloatField

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

# La clase Peliculas define cómo será la estructura de la tabla en la base de datos
class Coche(Model):
    id = PrimaryKeyField()  # Clave primaria que se auto-incrementa
    marca = CharField()  # Campo de tipo cadena
    modelo = CharField()  # Campo de tipo cadena
    año = IntegerField()  # Campo de tipo cadena
    precio = FloatField() # Campo de tipo entero para la valoración (0-10)
    color = CharField()  # Campo de tipo cadena
    motor_id = IntegerField()  # Campo de tipo entero para el identificador del motor
    



    # Constructor de la clase
    class Meta:
        database = db
        db_table = 'coches'  # Nombre de la tabla en la base de datos

# Función para mostrar el contenido de la tabla
def mostrar_tabla():
    coches = Coche.select()  # Selecciona todos los registros de la tabla
    for coche in coches:
        print(f"Id: {coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

# Elimina la tabla 'coches' si existe en la base de datos
def eliminar_tabla():
    Coche.drop_table()  # Elimina la tabla usando las funcionalidades de Peewee
    print("Tabla eliminada con éxito\n")

# Función para crear la tabla
def crear_tabla():
    Coche.create_table()  # Crea la tabla automáticamente en base al modelo Coche
    print("Tabla creada con éxito\n")
    
    

# Función para insertar datos en la tabla
# Inserta un nuevo coche en la tabla con los valores proporcionados
def insertar_coche(marca1, modelo1, año1, precio1, color1, motor1):
    Coche.create(marca=marca1, modelo=modelo1, año=año1, precio=precio1, color=color1, id_motor=motor1)  # Inserta una nueva fila
    print("Coche insertado con éxito")

# Eliminar la tabla
eliminar_tabla()

# Crea la tabla 'coches' según la estructura definida en la clase Coche
crear_tabla()

# Insertar 5 coches
insertar_coche("BMW", "Serie 3", 2019, 30000, "Negro", 1)
insertar_coche("Mercedes", "Clase C", 2020, 40000, "Blanco", 2)
insertar_coche("Audi", "A4", 2018, 35000, "Rojo", 3)
insertar_coche("BMW", "Serie 4", 2017, 30000, "Negro", 1)
insertar_coche("BMW", "Serie 5", 2021, 35000, "Azul", 1)



print("\n")

# Mostrar las coches
mostrar_tabla()