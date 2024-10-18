import pymysql
from pymysql import MySQLError
# Hacemos operaciones de lectura en la base de datos
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
        # Ejecutar una consulta para obtener los primeros 5 registros de la tabla 'coches'
        cursor.execute("""SELECT * FROM coches LIMIT 5""")   
        # Imprimir cada uno de los 5 registros obtenidos
        for _ in range(5):
            print(cursor.fetchone())  # Obtener y mostrar una fila a la vez
        # Ejecutar nuevamente una consulta para obtener otra vez los 5 registros de la tabla 'coches' ya que si no 
        print("\n Segunda lectura del cursor: \n")
        cursor.execute("""SELECT * FROM coches LIMIT 5""") 
        # Imprimir cada uno de los 5 registros obtenidos
        for _ in range(5):
            print(cursor.fetchone())  # Obtener y mostrar otra fila a la vez    
# Manejo de errores relacionados con MySQL
except MySQLError as e:
    print(f'El error es {e}')
# Cerrar la conexión a la base de datos al finalizar
finally:
    if conexion:
        conexion.close()  # Cierra la conexión a la base de datos
        print("La conexión ha sido cerrada")  # Imprimir mensaje indicando que la conexión ha sido cerrada
