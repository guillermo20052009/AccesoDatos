from peewee import MySQLDatabase, CharField, IntegerField, Model, PrimaryKeyField,FloatField

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

def tarea1():
    print("Tarea 1\n")
    print("Coches con marca BMW\n")
    coches_BMW = Coche.select().where(Coche.marca == "BMW")
    for coches in coches_BMW:
        print(f"id: {coches.id} ,Marca: {coches.marca}, Modelo: {coches.modelo}")

def tarea2():
    print("Tarea 2\n")

    coches = Coche.select()
    for coche in coches:
         print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

    coches_BMW_NEGRO = Coche.get((Coche.marca == 'BMW') & (Coche.color == "Azul"))
    coches_BMW_NEGRO.delete_instance()
    print("\nCoche con Marca = 'BMW' y color = 'azul' eliminada con exito\n")

    coches = Coche.select()
    for coche in coches:
         print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")

def tarea3():
    print("Tarea 3\n")
    Coche.delete().where(Coche.marca == "BMW").execute()
    print("coches con marca BMW eliminados con exito\n")

    coches = Coche.select()
    for coche in coches:
        print(f"id:{coche.id}, Marca: {coche.marca}, Modelo: {coche.modelo}, Año: {coche.año}, Precio: {coche.precio}, Color: {coche.color}, Motor: {coche.motor_id}")


tarea1()
print("\n")
tarea2()
print("\n")
tarea3()