import mysql.connector
import time;
from pymysql import MySQLError

try
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
                
        end_time = time.time()
        print(f"Tiempo de inserción con PyMySQL: {end_time - start_time} segundos")