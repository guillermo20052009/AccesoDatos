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
        
        cursor.execute("UPDATE coches SET precio = %s WHERE marca = %s", (25, 'BMW'))
        conexion.commit()
        print(cursor.rowcount, "registro(s) actualizado(s)")
        
except MySQLError as e:
    print(f'El error es{e}')