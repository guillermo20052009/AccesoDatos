import mysql.connector


        

from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='1dam'
    )
    if conexion.is_connected():
        cursor = conexion.cursor()
# Crear la tabla si no existe
# Fernando Usero Fuentes
# Módulo profesional: Acceso a datos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
            id_libro INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(30),
            autor VARCHAR(30),
            genero VARCHAR(30),
            fecha_publicacion VARCHAR(15),
            libreria_Origen VARCHAR(30)
            )
        """)
        print ("Tabla creada correctamente o ya existe")
        
        libros_iniciales = [
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "genero": "Novela", "ano_publicacion": "1605", "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Novela", "ano_publicacion": "1967", "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "genero": "Novela", "ano_publicacion": "1866", "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "La Casa de los Espíritus", "autor": "Isabel Allende", "genero": "Novela", "ano_publicacion": "1982", "libreria_origen": "Ramón Valle Inclán"},
        {"titulo": "El Nombre de la Rosa", "autor": "Umberto Eco", "genero": "Misterio", "ano_publicacion": "1980", "libreria_origen": "Ramón Valle Inclán"}
    ]

      
    
        cursor.execute(
        """INSERT INTO libros (titulo, autor, genero, fecha_publicacion, libreria_Origen) VALUES (%s, %s, %s, %s, %s)""",
        (libros_iniciales[0].get("titulo"),libros_iniciales[0].get("autor"),libros_iniciales[0].get("genero"),libros_iniciales[0].get("ano_publicacion"),libros_iniciales[0].get("libreria_origen"))
        )
        print("registro insertado")
        
        
except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")