import pymysql
from pymysql import MySQLError

try:
    # Conexión a la base de datos con PyMySQL
    conexion = pymysql.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='Guillermo1DAM'
    )
    
    with conexion.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS coches (
    id int NOT NULL AUTO_INCREMENT,
    marca varchar(50) NOT NULL,
    modelo varchar(50) NOT NULL,
    año int NOT NULL,
    precio decimal(10,2) NOT NULL,
    color varchar(20) NOT NULL,
    PRIMARY KEY (id)
    )""")
        cursor.execute("""INSERT INTO coches VALUES(3,"Mercede","Clase A",2013,20000.10,"Blanco");
""")
        conexion.commit()
        cursor.execute("""Select * FROM coches""")
        
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
        
        
except MySQLError as e:
    print(e)
finally:
    if conexion.open:
        conexion.close()
        print("Conexion cerrada")