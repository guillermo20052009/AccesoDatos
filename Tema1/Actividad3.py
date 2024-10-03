import json

class JSONFileHandler:

    # Este metodo esta en el tema explicado
    def read_json(self, ruta):
        try:
            with open(ruta, 'r') as f:
                #Devuelve lo que recoge del archivo Json con .load
                return json.load(f)
        except Exception as e:
            print(f"Error en la lectura: {e}")
            return None  # Devuelve None si hay un error


    
    def write_json(self, ruta, d):
        try:
            #Abrimos el archivo en modo escritura ('w')
            with open(ruta, 'w') as f:

                #jason.dump nos ayuda a guardar informacion como la de un
                #diccionario en un archivo Json.
                json.dump(d, f) 
        except Exception as e:
            print(f"Error en la escritura: {e}")
    
# Instanciamos la clase
json_handler = JSONFileHandler()

# Creamos el diccionario para escribir en el fichero
d1 = {
  "DNI": "77865330B",
  "FechaNacimiento": "05/01/2005"
}

#llamamos al metodo
json_handler.write_json('data.json', d1)

# Leer el archivo JSON para comprobar que se ha escrito
data = json_handler.read_json('data.json')
print(data)
