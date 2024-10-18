import mysql.connector  # Importar el conector de MySQL
import time  # Importar la librería para medir el tiempo
import random  # Importar la librería para seleccionar valores aleatorios

try:    
    # Establecer conexión con la base de datos MySQL
    conexion = mysql.connector.connect(
        host="localhost",  # Dirección del servidor MySQL
        user="usuario",    # Nombre de usuario de la base de datos
        password="usuario",  # Contraseña del usuario
        database="Guillermo1DAM"  # Nombre de la base de datos
    )
    
    # Listas de datos aleatorios para insertar en la tabla 'coches'
    marcas = ["Mercedes", "BMW", "Renault", "Peugeot", "Skoda"]
    modelos = ["2", "3", "4", "5", "6"]
    años = [2013, 2014, 2015, 2016, 2017]
    precios = [20000.10, 25000.00, 15000.50, 18000.00, 22000.25]
    colores = ["Blanco", "Negro", "Rojo", "Azul", "Gris"]

    # Usando un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
        start_time = time.time()  # Comenzar a medir el tiempo
        
        # Insertar 10,000 registros en la tabla 'coches'
        for i in range(10000):
            # Seleccionar valores aleatorios de las listas
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            año = random.choice(años)
            precio = random.choice(precios)
            color = random.choice(colores)
            
            # Insertar un registro en la tabla 'coches' con los valores seleccionados
            cursor.execute(f"""INSERT INTO coches (marca, modelo, año, precio, color) 
            VALUES ("{marca}", "{modelo}", {año}, {precio}, "{marca}");
            """)
                
        end_time = time.time()  # Terminar de medir el tiempo
        
        # Imprimir el tiempo que tomó ejecutar las inserciones
        print(f"Tiempo de escritura con MySQL-connector: {end_time - start_time} segundos")
        
        # Confirmar (commit) los cambios en la base de datos
        conexion.commit()

# Manejo de errores relacionados con MySQL
except mysql.connector.Error as e:
    print(f'El error es {e}')
    
finally:
    # Cerrar la conexión si está abierta
    if conexion:
        conexion.close()  # Cierra la conexión
        print("Conexión cerrada")  # Imprimir mensaje de que la conexión ha sido cerrada
