from database import db
from Coche import Coche


db.connect()
print("Conexión Exitosa")

# Crear la tabla si no existe
db.create_tables([Coche])
print("Tabla 'coches' creada exitosamente o ya existe")
Coche.create(marca='BMW',modelo='E36',año=1995,precio=150000.00,color='Rojo',motor_id=1)
print("Registro Insertado")

if Coche._meta.tabla_existe(Coche._meta.table_name):
    print('La tabla existe')
    db.drop_tables([Coche], cascade=True)
    print("Eliminada")
else:
    print("La tabla no existe") 


