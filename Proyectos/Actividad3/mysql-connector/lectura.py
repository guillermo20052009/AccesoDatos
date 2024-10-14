import mysql.connector
import time;
try:    
    conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="usuario",
    database="Guillermo1DAM"
)

    with conexion.cursor() as cursor:
        start_time = time.time()
        for i in range(10000):
            cursor.execute(f"""Select * from coches;
            """)
            cursor.fetchall()
                
        end_time = time.time()
        print(f"Tiempo de Lectura con MySQL-connector: {end_time - start_time} segundos")
        
except mysql.connector.Error as e:
    print(f'El error es{e}')