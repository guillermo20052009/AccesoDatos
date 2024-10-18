import pymysql
from pymysql import MySQLError

try:
    # Conexión a la base de datos con PyMySQL
    conexion = pymysql.connect(
        host='localhost',       # Dirección del servidor de la base de datos
        user='usuario',         # Usuario de la base de datos
        password='usuario',     # Contraseña del usuario
        database='Guillermo1DAM' # Nombre de la base de datos a la que conectarse
    )
    
    with conexion.cursor() as cursor:
        # Crear la tabla 'motor' si no existe, con las columnas especificadas
        cursor.execute("""CREATE TABLE IF NOT EXISTS motor (
            id INT NOT NULL AUTO_INCREMENT,  # ID autoincremental como clave primaria
            tipo ENUM('diesel', 'gasolina', 'híbrido', 'eléctrico') NOT NULL,  # Tipo de motor, valores definidos
            potencia INT NOT NULL,  # Potencia del motor, tipo entero
            fecha_fabricacion DATE,  # Fecha de fabricación del motor
            marca VARCHAR(50),  # Marca del motor
            modelo VARCHAR(50),  # Modelo del motor
            precio DECIMAL(10, 2),  # Precio del motor, con 2 decimales
            PRIMARY KEY (id)  # Definir id como clave primaria
        )""")
        
        # Modificar la tabla 'coches' para agregar una columna 'motor_id'
        # y definir una clave foránea que referencia la columna 'id' de la tabla 'motor'
        cursor.execute("""ALTER TABLE coches
            ADD COLUMN motor_id INT,  # Agregar columna motor_id en la tabla coches
            ADD CONSTRAINT fk_vehiculo_motor  # Definir la clave foránea
            FOREIGN KEY (motor_id) REFERENCES motor(id);  # motor_id referencia al id de la tabla 'motor'
        """)

        # Insertar datos en la tabla 'motor'
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('diesel', 150, '2021-06-15', 'Ford', 'F-150', 15000.50)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('gasolina', 120, '2022-03-22', 'Toyota', 'Corolla', 12000.75)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('híbrido', 180, '2023-01-10', 'Honda', 'Civic', 18000.00)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('eléctrico', 200, '2023-09-05', 'Tesla', 'Model 3', 30000.99)")
        
        # Confirmar los cambios (commit) en la base de datos
        conexion.commit()
        
        # Consultar todos los registros de la tabla 'motor'
        cursor.execute("SELECT * FROM motor")
        
        # Obtener y mostrar los resultados de la consulta
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)  # Imprimir cada fila de los resultados obtenidos
        
except MySQLError as e:
    # Manejo de errores en caso de fallo en la conexión o consulta
    print(e)

finally:
    # Cerrar la conexión a la base de datos
    if conexion.open:
        conexion.close()  # Cierra la conexión a la base de datos
        print("Conexión cerrada")  # Imprimir mensaje de confirmación
