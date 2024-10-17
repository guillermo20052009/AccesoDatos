import mysql.connector
import time;
import random;
try:    
    conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="usuario",
    database="Guillermo1DAM"
)
    marcas = ["Mercedes", "BMW", "Renault", "Peugeot", "Skoda"]
    modelos = ["2", "3", "4", "5", "6"]
    años = [2013, 2014, 2015, 2016, 2017]
    precios = [20000.10, 25000.00, 15000.50, 18000.00, 22000.25]
    colores = ["Blanco", "Negro", "Rojo", "Azul", "Gris"]

    with conexion.cursor() as cursor:
        start_time = time.time()
        for i in range(10000):
            marca= random.choice(marcas)
            modelo= random.choice(modelos)
            año= random.choice(años)
            precio= random.choice(precios)
            color= random.choice(colores)
            cursor.execute(f"""INSERT INTO coches (marca, modelo, año, precio, color) 
            VALUES ("{marca}", "{modelo}", {año}, {precio}, "{marca}");
            """)
                
        end_time = time.time()
        print(f"Tiempo de escritura con MySQL-connector: {end_time - start_time} segundos")
        conexion.commit()
except mysql.connector.Error as e:
    print(f'El error es{e}')
    
finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")