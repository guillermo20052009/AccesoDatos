import mysql.connector
# Hacemos una llamada a un procedimiento almacenado en la base de datos

try:    
    # Conexión a la base de datos con MySQL Connector
    conexion = mysql.connector.connect(
        host="localhost",       # Dirección del servidor de la base de datos
        user="usuario",         # Usuario de la base de datos
        password="usuario",     # Contraseña del usuario
        database="Guillermo1DAM" # Nombre de la base de datos a la que conectarse
    )

    # Usando un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
        # Llamar al procedimiento almacenado 'obtener_datosPython' con el parámetro 5
        cursor.callproc('obtener_datos_Python2', [5])
        
        # Iterar sobre los resultados devueltos por el procedimiento almacenado
        for resultado in cursor.stored_results():
            print(resultado.fetchall())  # Imprimir todos los registros obtenidos
        
# Manejo de errores relacionados con MySQL
except mysql.connector.Error as e:
    print(f'El error es {e}')  # Mostrar mensaje de error
finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")
