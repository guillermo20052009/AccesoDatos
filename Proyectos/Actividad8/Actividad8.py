import mysql.connector
try:    
    conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="usuario",
    database="Guillermo1DAM"
)

    with conexion.cursor() as cursor:
       cursor.callproc('obtener_datosPython', [5])
       for resultado in cursor.stored_results():
           print(resultado.fetchall())
        
except mysql.connector.Error as e:
    print(f'El error es{e}')