import pymysql
from pymysql import MySQLError
# Hacemos operaciones de inserción en la base de datos
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
        print("Iniciando Transacción...")  
        # Insertar un nuevo registro en la tabla 'coche' Aquí esta el error intencionado,
        # ya que no existe la tabla coche es coches.
        cursor.execute("""INSERT INTO coche (marca, modelo, año, precio, color, id_motor)
                          VALUES ("BMW", "E36", 2005, 40000.10, "rojo", 1)""")   
        # Confirmar los cambios (commit) en la base de datos
        conexion.commit()
        print("Transacción exitosa")  
# Manejo de errores relacionados con MySQL
except MySQLError as e:
    print(f'Error en la transacción: {e}')  # Mostrar mensaje de error
    if conexion:
        # Realizar rollback si ocurre un error
        conexion.rollback()  # Corregir el error en la transacción
        print("Rollback realizado")
# Cerrar la conexión a la base de datos al finalizar
finally:
    if conexion:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cierra la conexión a la base de datos
        print("Conexión cerrada")  # Imprimir mensaje indicando que la conexión ha sido cerrada
