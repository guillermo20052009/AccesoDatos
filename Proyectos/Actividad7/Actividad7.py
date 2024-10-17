import pymysql
from pymysql import MySQLError
#Hacemos operaciones

try:
    # Conexión a la base de datos con PyMySQL
    conexion = pymysql.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='Guillermo1DAM'
    )
    with conexion.cursor() as cursor:
        
        print("Iniciando Transacción...")
        cursor.execute("""INSERT INTO coche (marca,modelo,año,precio,color,id_motor)
                       Values ("BMW","E36",2005,40000.10,"rojo",1)""")
        conexion.commit()
        print ("Transacción exitosa")
        
except MySQLError as e:
    print(f'Error en la transacción{e}')
    if conexion:
        conexion.rollback
        print("Rollback realizado")
finally:
    if conexion:
        conexion.close()
        cursor.close()
        print("Conexión cerrada")