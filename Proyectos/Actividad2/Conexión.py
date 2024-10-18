import pymysql
from pymysql import MySQLError

try:
    # Conexión a la base de datos MySQL utilizando PyMySQL
    conexion = pymysql.connect(
        host='localhost',    # Dirección del servidor MySQL (en este caso, localhost)
        user='usuario',      # Nombre de usuario de la base de datos
        password='usuario',  # Contraseña del usuario
        database='Guillermo1DAM'  # Nombre de la base de datos a la que nos conectamos
    )
    
    # Usando un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
        # Crear la tabla "coches" si no existe, con las columnas id, marca, modelo, año, precio, color
        cursor.execute("""CREATE TABLE IF NOT EXISTS coches (
    id int NOT NULL AUTO_INCREMENT,  # Columna id con auto-incremento
    marca varchar(50) NOT NULL,      # Columna marca, tipo varchar
    modelo varchar(50) NOT NULL,     # Columna modelo, tipo varchar
    año int NOT NULL,                # Columna año, tipo int
    precio decimal(10,2) NOT NULL,   # Columna precio, tipo decimal con 2 decimales
    color varchar(20) NOT NULL,      # Columna color, tipo varchar
    PRIMARY KEY (id)                 # Definir id como clave primaria
    )""")
        
        # Insertar un registro en la tabla coches
        cursor.execute("""INSERT INTO coches (marca, modelo, año, precio, color) VALUES ("Mercede", "Clase A", 2013, 20000.10, "Blanco");
""")
        
        # Confirmar (commit) los cambios en la base de datos
        conexion.commit()
        
        # Consultar todos los registros de la tabla coches
        cursor.execute("""SELECT * FROM coches""")
        
        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()
        
        # Iterar sobre los resultados e imprimir cada fila
        for fila in resultados:
            print(fila)
        
except MySQLError as e:
    # Captura cualquier error relacionado con MySQL y lo imprime
    print(e)
finally:
    # Asegurarse de cerrar la conexión si está abierta
    if conexion.open:
        conexion.close()  # Cierra la conexión
        print("Conexion cerrada")  # Mensaje indicando que la conexión se ha cerrado
