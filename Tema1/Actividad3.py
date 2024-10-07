import json

class JSONFileHandler:

    # Este metodo esta en el tema explicado
    def read_json(self, ruta):
        try:
            with open(ruta, 'r') as f:
                return json.load(f) #Devuelve lo que recoge del archivo Json con .load
        except Exception as e:
            print(f"Error en la lectura: {e}")
            return None  # Devuelve None si hay un error
    
    def write_json(self, ruta, d):
        try:
            with open(ruta, 'w') as f: #Abrimos el archivo en modo escritura ('w')
                json.dump(d, f) #jason.dump nos ayuda a guardar informacion como la de un diccionario en un archivo Json.
        except Exception as e:
            print(f"Error en la escritura: {e}")
    
json_handler = JSONFileHandler() # Instanciamos la clase
d1 = {
  "DNI": "77865330B",
  "FechaNacimiento": "05/01/2005" # Creamos el diccionario para escribir en el fichero
}
json_handler.write_json('data.json', d1) #llamamos al metodo
data = json_handler.read_json('data.json') # Leer el archivo JSON para comprobar que se ha escrito
print(data)

