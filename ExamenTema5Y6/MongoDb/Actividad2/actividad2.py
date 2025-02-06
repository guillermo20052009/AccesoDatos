from pymongo import MongoClient, errors

# Datos de conexión
usuario = "usuario"
clave = "usuario"
base_datos = "1dam"
host = "localhost"
puerto = 27017

try:
    # Intentar conectarse al servidor MongoDB
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}",
                         serverSelectionTimeoutMS=5000)
    
    # Seleccionar la base de datos
    db = client[base_datos]
    
    # Seleccionar la colección correcta (coches)
    coleccion_coches = db["coches"]
    
    # Consultar solo los coches de la marca Ford
    print('\nCoches marca ford:\n')
    coches_ford = coleccion_coches.find({"marca": "Ford"})
    for coche in coches_ford:
        print(coche)
        
        
    print('\nCoches marca ford (nombre y modelo):\n')    
    proyeccion = {"marca": 1, "modelo": 1, "_id": 0}  # Incluye marca y modelo, excluye _id
    cochesProyeccion = coleccion_coches.find({"marca": "Ford"}, proyeccion)
    for coche in cochesProyeccion:
        print(coche)
        
        
    print('\nCoches marca ford, limitacion de 2 registros y ordenados alfabeticamente por modelo:\n')
    proyeccion = {"marca": 1, "modelo": 1, "_id": 0}  # Incluye marca y modelo, excluye _id
    cocheslimitados = coleccion_coches.find({"marca": "Ford"}, proyeccion).limit(2)
    cocheslimitados.sort("modelo")
    for coche in cocheslimitados:
        print(coche)
        
except errors.ServerSelectionTimeoutError as err:
    # Este error ocurre si el servidor no está disponible o no se puede conectar
    print(f"No se pudo conectar a MongoDB: {err}")
except errors.OperationFailure as err:
    # Este error ocurre si las credenciales son incorrectas o no se tienen los permisos necesarios
    print(f"Fallo en la autenticación o permisos insuficientes: {err}")
except Exception as err:
    # Manejar cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {err}")
finally:
    # Cerrar la conexión si se estableció correctamente
    if 'client' in locals():
        client.close()
        print("Conexión cerrada.")
