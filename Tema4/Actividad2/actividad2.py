from peewee import MySQLDatabase, CharField, IntegerField, Model, PrimaryKeyField, FloatField

# Configuración de la base de datos
db = MySQLDatabase(
    'Guillermo1DAM',  # Nombre de la base de datos
    user='usuario',  # Nombre de usuario para la base de datos
    password='usuario',  # Contraseña del usuario
    host='localhost',  # Servidor de la base de datos
    port=3306  # Puerto donde escucha MySQL (3306 es el predeterminado)
)

# Conectarse a la base de datos
db.connect()
print("Conexión exitosa a la base de datos\n")

# La clase Coche define cómo será la estructura de la tabla en la base de datos
class Coche(Model):
    id = PrimaryKeyField()  # Clave primaria que se auto-incrementa
    marca = CharField()  # Campo de tipo cadena para almacenar la marca del coche
    modelo = CharField()  # Campo de tipo cadena para almacenar el modelo del coche
    año = IntegerField()  # Campo de tipo entero para almacenar el año de fabricación
    precio = FloatField() # Campo de tipo float para almacenar el precio del coche
    color = CharField()  # Campo de tipo cadena para almacenar el color del coche
    motor_id = IntegerField()  # Campo de tipo entero para el identificador del motor
    
    # Configuración adicional de la tabla en la base de datos
    class Meta:
        database = db
        db_table = 'coches'  # Nombre de la tabla en la base de datos

# Función que muestra todos los coches de la marca BMW
def tarea1():
    print("Tarea 1\n")
    print("Coches con marca BMW\n")
    coches_BMW = Coche.select().where(Coche.marca == "BMW")  # Filtra coches con marca 'BMW'
    for coches in coches_BMW:
        print(f"id: {coches.id} ,Marca: {coches.marca}, Modelo: {coches.modelo}")

# Función que muestra todos los coches y elimina el coche de marca BMW y color Azul si existe
def tarea2():
    print("Tarea 2\n")

    # Muestra todos los coches antes de eliminar
    coches = Coche.select()
    for coche in coches:
        print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

    # Busca y elimina un coche de marca 'BMW' y color 'Azul'
    coches_BMW_NEGRO = Coche.get((Coche.marca == 'BMW') & (Coche.color == "Azul"))
    coches_BMW_NEGRO.delete_instance()  # Elimina la instancia de coche seleccionada
    print("\nCoche con Marca = 'BMW' y color = 'azul' eliminada con éxito\n")

    # Muestra todos los coches después de eliminar
    coches = Coche.select()
    for coche in coches:
        print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

# Función que elimina todos los coches de marca BMW y muestra la lista de coches restantes
def tarea3():
    print("Tarea 3\n")
    Coche.delete().where(Coche.marca == "BMW").execute()  # Elimina todos los coches con marca 'BMW'
    print("Coches con marca BMW eliminados con éxito\n")

    # Muestra todos los coches después de eliminar los BMW
    coches = Coche.select()
    for coche in coches:
        print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

# Ejecución de las funciones para verificar su comportamiento
tarea1()
print("\n")
tarea2()
print("\n")
tarea3()
