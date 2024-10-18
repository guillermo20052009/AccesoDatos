import pymysql
from pymysql import MySQLError

try:
    # Establece la conexión a la base de datos MySQL
    conexion = pymysql.connect(
        host='localhost',    # Dirección del servidor MySQL (en este caso, localhost)
        user='usuario',      # Nombre de usuario de la base de datos
        password='usuario',  # Contraseña del usuario de la base de datos
        database='Guillermo1DAM'  # Nombre de la base de datos con la que se desea conectar
    )

    # Verifica si la conexión está abierta
    if conexion.open:
        print("Conexión a la base de datos exitosa")  # Imprime mensaje si la conexión fue exitosa
except MySQLError as e:
    # Captura cualquier error relacionado con MySQL y lo imprime
    print(f"Error de conexión: {e}")
finally:
    # Asegura que la conexión se cierre si está abierta
    if conexion.open:
        conexion.close()  # Cierra la conexión a la base de datos
        print("Conexión cerrada")  # Imprime mensaje confirmando que la conexión se cerró
