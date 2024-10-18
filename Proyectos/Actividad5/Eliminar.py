import pymysql
from pymysql import MySQLError
# Hacemos operaciones de eliminación en la base de datos
try:
    # Conexión a la base de datos con PyMySQL
    conexion = pymysql.connect(
        host='localhost',       # Dirección del servidor de la base de datos
        user='usuario',         # Usuario de la base de datos
        password='usuario',     # Contraseña del usuario
        database='Guillermo1DAM' # Nombre de la base de datos a la que conectarse
    )
   
    # Usando un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
        # Eliminar los registros en la tabla 'coches' donde el id es menor a 25
        cursor.execute("DELETE FROM coches WHERE precio < %s", (20))        
        # Confirmar los cambios (commit) en la base de datos
        conexion.commit()
        # Imprimir cuántos registros fueron eliminados
        print(cursor.rowcount, "registro(s) eliminado(s)")       
# Manejo de errores relacionados con MySQL
except MySQLError as e:
    print(f'El error es {e}')

# Cerrar la conexión a la base de datos al finalizar
finally:
    if conexion:
        conexion.close()  # Cierra la conexión a la base de datos
        print("Conexión cerrada")  # Imprimir mensaje indicando que la conexión ha sido cerrada
