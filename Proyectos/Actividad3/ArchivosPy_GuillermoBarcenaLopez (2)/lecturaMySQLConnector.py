import mysql.connector  # Importar el conector de MySQL
import time  # Importar la librería para medir el tiempo

try:    
    # Establecer conexión con la base de datos MySQL
    conexion = mysql.connector.connect(
        host="localhost",  # Dirección del servidor MySQL
        user="usuario",    # Nombre de usuario de la base de datos
        password="usuario",  # Contraseña del usuario
        database="Guillermo1DAM"  # Nombre de la base de datos
    )

    # Usar un cursor para realizar las consultas SQL
    with conexion.cursor() as cursor:
        start_time = time.time()  # Comenzar a medir el tiempo
        
        # Realizar 10000 consultas a la tabla 'coches'
        for i in range(10000):
            cursor.execute("""SELECT * FROM coches;""")  # Ejecutar consulta para obtener todos los registros de la tabla 'coches'
            cursor.fetchall()  # Recuperar todos los resultados de la consulta
        
        end_time = time.time()  # Terminar de medir el tiempo
        
        # Imprimir el tiempo que tomó realizar las lecturas
        print(f"Tiempo de Lectura con MySQL-connector: {end_time - start_time} segundos")
        
# Manejo de errores relacionados con MySQL
except mysql.connector.Error as e:
    print(f'El error es {e}')

# Cerrar la conexión a la base de datos al final
finally:
    if conexion:
        conexion.close()  # Cierra la conexión
        print("Conexión cerrada")  # Imprimir mensaje indicando que la conexión ha sido cerrada
