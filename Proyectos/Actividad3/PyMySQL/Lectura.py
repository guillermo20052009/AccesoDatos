import pymysql
from pymysql import MySQLError
import time

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
        
        start_time = time.time()
        for i in range(10000):
            cursor.execute("""Select * FROM coches;""")
                
        end_time = time.time()
        print(f"Tiempo de Lectura con PyMySQL: {end_time - start_time} segundos")
except MySQLError as e:
    print(f'El error es{e}')