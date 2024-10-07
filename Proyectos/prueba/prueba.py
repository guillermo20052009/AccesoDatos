import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='Guillermo1DAM'
)

    if conexion.is_connected():
            print("Conexión a la base de datos exitosa")
except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")