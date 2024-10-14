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
        # Crear la tabla 'motor' si no existe
        cursor.execute("""CREATE TABLE IF NOT EXISTS motor (
            id INT NOT NULL AUTO_INCREMENT,
            tipo ENUM('diesel', 'gasolina', 'híbrido', 'eléctrico') NOT NULL,
            potencia INT NOT NULL,
            fecha_fabricacion DATE,
            marca VARCHAR(50),
            modelo VARCHAR(50),
            precio DECIMAL(10, 2),
            PRIMARY KEY (id)
        )""")
        
        # Modificar la tabla 'coches' para agregar una columna 'motor_id'
        # y definir una clave foránea que referencia a 'motor(id)'
        cursor.execute("""ALTER TABLE coches
            ADD COLUMN motor_id INT,
            ADD CONSTRAINT fk_vehiculo_motor
            FOREIGN KEY (motor_id) REFERENCES motor(id);
        """)

        # Insertar datos en la tabla 'motor'
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('diesel', 150, '2021-06-15', 'Ford', 'F-150', 15000.50)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('gasolina', 120, '2022-03-22', 'Toyota', 'Corolla', 12000.75)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('híbrido', 180, '2023-01-10', 'Honda', 'Civic', 18000.00)")
        cursor.execute("INSERT INTO motor (tipo, potencia, fecha_fabricacion, marca, modelo, precio) VALUES ('eléctrico', 200, '2023-09-05', 'Tesla', 'Model 3', 30000.99)")
        
        # Confirmar los cambios en la base de datos
        conexion.commit()
        
        # Consultar todos los registros de la tabla 'motor'
        cursor.execute("SELECT * FROM motor")
        
        # Obtener y mostrar los resultados de la consulta
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)  # Imprimir cada fila de resultados obtenidos
        
except MySQLError as e:
    # Manejo de errores en caso de fallo en la conexión o consulta
    print(e)

finally:
    # Cerrar la conexión a la base de datos
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")
