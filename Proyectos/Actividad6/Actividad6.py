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
        cursor.execute("""SELECT * FROM coches LIMIT 5""")
        
        for _ in range(5):
            print(cursor.fetchone())
        
        cursor.execute("""SELECT * FROM coches LIMIT 5""")
        
        for _ in range(5):
            print(cursor.fetchone())
            
except MySQLError as e:
    print(f'El error es{e}')