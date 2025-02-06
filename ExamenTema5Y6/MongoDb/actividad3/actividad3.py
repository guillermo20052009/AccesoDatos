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
    
    coches=[{"marca": "Ford",
    "modelo": "Clase A",
    "año": 2020,
    "color": "Blanco",
    "kilometraje": 25000,
    "precio": 15000},{"marca": "Peugeot",
    "modelo": "2009",
    "año": 2020,
    "color": "Blanco",
    "kilometraje": 25000,
    "precio": 15000},{"marca": "suzuki",
    "modelo": "swift",
    "año": 2020,
    "color": "Blanco",
    "kilometraje": 25000,
    "precio": 15000}]
    
    resultado=coleccion_coches.insert_many(coches)
    print("Ids de documentos insertados:", resultado.inserted_ids)
  
  
    print('\nCoche antes de ser editado:\n')
    coches_ford = coleccion_coches.find({"modelo": "2009"})
    for coche in coches_ford:
        print(coche)
        
    resultado=coleccion_coches.update_one({"modelo":"2009"},{"$set":{"marca":"cambio"}})
    if resultado.modified_count>0:
        print("actualizado con exito")
    else:
        print("no se encontró el documento o no hubo cambios")
    
    # Eliminar un solo documento (eliminar el Martillo)
    resultado = coleccion_coches.delete_one({"marca": "suzuki"})
# Verificar si el documento fue eliminado
    if resultado.deleted_count > 0:
        print("Documento eliminado con éxito.")
    else:
        print("No se encontró el documento para eliminar.")
        
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
