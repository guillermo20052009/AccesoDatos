import pymysql
from pymysql import MySQLError
# Hacemos operaciones de actualización en la base de datos

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
        # Actualizar el precio de un coche en la tabla 'coches'
        # Cambia el precio a 25 donde el id del coche es 1
        cursor.execute("UPDATE coches SET precio = %s WHERE id = %s", (25, 1))
        
        # Confirmar los cambios (commit) en la base de datos
        conexion.commit()
        
        # Imprimir cuántos registros fueron actualizados
        print(cursor.rowcount, "registro(s) actualizado(s)")
        
# Manejo de errores relacionados con MySQL
except MySQLError as e:
    print(f'El error es {e}')

# Cerrar la conexión a la base de datos al finalizar
finally:
    if conexion:
        conexion.close()  # Cierra la conexión a la base de datos
        print("Conexión cerrada")  # Imprimir mensaje indicando que la conexión ha sido cerrada
