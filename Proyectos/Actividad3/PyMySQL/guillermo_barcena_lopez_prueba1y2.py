import pymysql
import csv,json
from pymysql import MySQLError

class JSONFileHandler:

    # Este metodo esta en el tema explicado
    def read_json(self, ruta):
        try:
            with open(ruta, 'r') as f:
                return json.load(f) #Devuelve lo que recoge del archivo Json con .load
        except Exception as e:
            print(f"Error en la lectura: {e}")
            return None  # D
    def write_json(self, ruta, d):
        try:
            with open(ruta, 'w') as f: #Abrimos el archivo en modo
                json.dump(d, f) #jason.dump nos ayuda a guardar
        except Exception as e:
            print(f"Error en la escritura: {e}")
    
class CSVFileHandler:
    def read_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='') as f:
                reader = csv.DictReader(f) # Creamos el objeto reader
                rows = [] # Lista vacía para almacenar las filas
                for row in reader: # Recorremos cada fila en el archivo
                    rows.append(row) # Añadimos cada fila (un
                return rows # Devolvemos la lista con todas las filas
        except Exception as e:
            print(f"Error leyendo el archivo CSV: {e}")

def borrarRepetidos(cursor):
    data=[]
    cursor.execute("SELECT * FROM libros")
    resto_filas = cursor.fetchall()
    for fila in resto_filas:
       if fila[1] in data:
           cursor.execute("DELETE FROM libros WHERE titulo = %s && id_libro = %s", (fila[1],fila[0]))
       else:
           data.append(fila[1])
    
try:
# Conexión a la base de datos MySQL utilizando PyMySQL
    conexion = pymysql.connect(
    host='localhost', # Dirección del servidor MySQL (en este
    user='usuario', # Nombre de usuario de la base de datos
    password='usuario', # Contraseña del usuario
    database='1dam' # Nombre de la base de datos a la que

    )
# Usando un cursor para ejecutar consultas SQL
    with conexion.cursor() as cursor:
# Crear la tabla "coches" si no existe, con las columnas 
        cursor.execute("""CREATE TABLE IF NOT EXISTS libros (
            id_libro INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(30),
            autor VARCHAR(30),
            genero VARCHAR(30),
            fecha_publicacion INT,
            libreria_Origen VARCHAR(30)
            )""")
        print("tabla creada o ya existe")
        
        libros_iniciales = [
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "genero": "Novela", "ano_publicacion": 1605, "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Novela", "ano_publicacion": 1967, "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "genero": "Novela", "ano_publicacion": 1866, "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "La Casa de los Espíritus", "autor": "Isabel Allende", "genero": "Novela", "ano_publicacion": 1982, "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "El Nombre de la Rosa", "autor": "Umberto Eco", "genero": "Misterio", "ano_publicacion": 1980, "libreria_origen": "Ramón Valle Inclán"}
    ]
# Insertar un registro en la tabla coches
        for registro in libros_iniciales:
            cursor.execute(
        """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, libreria_Origen) VALUES (%s, %s, %s, %s, %s)""",
        (registro.get("titulo"),registro.get("autor"),registro.get("genero"),registro.get("ano_publicacion"),registro.get("libreria_origen"))
        )
            print("Registro añadido")
        conexion.commit()
            
        json_handler = JSONFileHandler()
        csv_handler=CSVFileHandler() 
       
        data = json_handler.read_json('libros_machado.json')
        data2=csv_handler.read_csv('libros_unamuno.csv')
        
        print("Empezando transacción")
        
        for registro in data:
            cursor.execute(
        """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, libreria_Origen) VALUES (%s, %s, %s, %s, %s)""",
        (registro.get("titulo"),registro.get("autor"),registro.get("genero"),registro.get("año_publicacion"),"Machado")
        )
            
        for registro in data2:
            cursor.execute(
        """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, libreria_Origen) VALUES (%s, %s, %s, %s, %s)""",
        (registro.get("titulo"),registro.get("autor"),registro.get("genero"),registro.get("año_publicacion"),"Unamuno")
        )
        conexion.commit()
        print("Transacción realizada con éxito")
    
        borrarRepetidos(cursor)
        conexion.commit()
        print("Datos borrados con exito")
        
        cursor.execute("SELECT * FROM libros")
        
           
        
except MySQLError as e:
    print(e)
    conexion.rollback()
    print("Transacción cancelada")
    
finally:
    if conexion.open:
        conexion.close() # Cierra la conexión
        print("Conexion cerrada") 