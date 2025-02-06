import logging
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("ProductoManager.log"), # Logs guardados en un archivo
        logging.StreamHandler(), # Logs también en consola
    ]
)

class ProductoManager:
    def __init__(self, database_name, collection_name):
        """Inicializa el componente DatabaseManagerDocumental."""
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None
        
    def conectar(self):
        """Conectar a la base de datos MongoDB"""
        try:
            self.client = MongoClient("mongodb://localhost:27017")
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]
            logging.info(f"Conectado a MongoDB: {self.database_name}.{self.collection_name}")
            print(f"Conectado a MongoDB: {self.database_name}.{self.collection_name}")
        except PyMongoError as e:
            logging.error(f"Error al conectar a MongoDB: {e}")

    def cerrar_conexion(self):
        """Cerrar la conexión a MongoDB"""
        if self.client:
            self.client.close()
            logging.info("Conexión a MongoDB cerrada.")
            print("Conexión a MongoDB cerrada.")

    def Insertar_productos(self, productos):
        """Insertar un nuevo documento en la colección"""
        try:
            result = self.collection.insert_many(productos)
            logging.info(f"Documentos insertado con ID: {result.inserted_ids}")
            print(f"Documentos insertado con ID: {result.inserted_ids}")
            return result.inserted_ids
        except PyMongoError as e:
            logging.error(f"Error al insertar el documento: {e}")

    def consultar_proyeccion_ordenada(self, filtro, proyeccion, orden):
        try:
            for producto in self.collection.find(filtro,proyeccion).sort(orden,-1):
                print(producto)
                logging.info(f"Producto con el siguiente filtro: {filtro} encontrado: {producto}")
        except:
            logging.error(f"Error al consultar productos")
        
    def mostrar_todos_productos(self):
        try:
            for producto in self.collection.find():
                print(f"{producto}\n")
                logging.info(f"Producto encontrado: {producto}")
        except:
            logging.error(f"Error al consultar productos")


    def actualizar_productos(self,filtro,actualizacion):
        try:
                    if self.collection.count_documents(filtro)>0:
                        result = self.collection.update_many(filtro, {"$set": actualizacion})
                        if result.modified_count > 0:
                            print(f"Documento actualizado: {filtro}")
                            logging.info(f"Documento actualizado: {filtro}")
                    else:
                        print(f"no existe el nombre:")
        except:
            logging.error(f"Error al actualizar productos")
        
    def contar_documentos(self):
        try:
            print(self.collection.count_documents({}))
            logging.info(f"numero de documentos: {self.collection.count_documents({})}")
        except:
            logging.error(f"Error al contar documentos")

    def eliminar_documentos(self,filtro):
        try:
            result=self.collection.delete_many(filtro)
            if result.deleted_count > 0:
                print("Eliminado con exito")     
                logging.info(f"Producto eliminado con exito")  
        except:
            logging.error("Error al eliminar el producto")

    def consulta_compleja(self,filtro,proyeccion,orden):
        try:
            for producto in self.collection.find(filtro,proyeccion).sort(orden,1):
                print(producto)
                logging.info(f"Consulta realizada con exito, producto obtenido: {producto}")
        except:
            logging.error("Fallo en la consulta")


if __name__ == "__main__":
    # Configurar el componente
    db_manager = ProductoManager(
    database_name="1dam",
    collection_name="productos"
)
    
db_manager.conectar()

#-----Ejercicio 1-------
print("\n\nEjercicio 1: \n\n")
productos=[{"nombre": "Drone Phantom X", "categoria": "Drones", "precio": 1200.50, "stock": 4},
{"nombre": "Auriculares Sonic Boom", "categoria": "Auriculares", "precio": 301, "stock": 14},
{"nombre": "Cámara Action Pro", "categoria": "Cámaras", "precio": 499.99, "stock": 10},
{"nombre": "Asistente SmartBuddy", "categoria": "Asistentes Inteligentes", "precio": 199.99,
"stock": 20},
{"nombre": "Cargador Solar Ultra", "categoria": "Accesorios", "precio": 49.99, "stock": 3}]

db_manager.Insertar_productos(productos)


#------Ejercicio 2------
print("\n\nEjercicio 2: \n\n")
proyeccion = {"nombre": 1, "precio": 1, "stock": 1,"_id":0}
orden = "precio"
filtro={"categoria": "Auriculares"}
db_manager.consultar_proyeccion_ordenada(filtro,proyeccion,orden)



#-----Ejercicio 3------
print("\n\nEjercicio 3: \n\n")
db_manager.mostrar_todos_productos()
filtro={
"$or": [
{"nombre": {"$eq": "Drone Phantom X"}},
{"nombre": {"$eq": "Cámara Action Pro"}}
]
}

actualizacion={"precio": 2500}
db_manager.actualizar_productos(filtro,actualizacion)
db_manager.mostrar_todos_productos()


#------Ejercicio 4-------
print("\n\nEjercicio 4: \n\n")
db_manager.contar_documentos()
filtro={"stock": {"$lt": 5}}
db_manager.eliminar_documentos(filtro)
db_manager.contar_documentos()

#------Ejercicio 5-------
print("\n\nEjercicio 5: \n\n")
filtro={
"$and": [
{"precio": {"$gt": 300}},
{"stock": {"$lt": 15}}
]
}
proyeccion = {"nombre": 1, "categoria": 1, "precio": 1,"_id":0}
orden="categoria"

db_manager.consulta_compleja(filtro,proyeccion,orden)

db_manager.cerrar_conexion()