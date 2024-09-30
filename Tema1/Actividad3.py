import json

class JSONFileHandler:
    def read_json(self, ruta):
        try:
            with open(ruta, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error en la lectura: {e}")
            return None  # Devuelve None si hay un error

    def write_json(self, ruta, d):
        try:
            with open(ruta, 'w') as f:
                json.dump(d, f) 
        except Exception as e:
            print(f"Error en la escritura: {e}")
    
# Uso
json_handler = JSONFileHandler()

# Escribir nuevo dato al archivo JSON
d1 = {
  "DNI": "77865330B",
  "FechaNacimiento": "05/01/2005"
}
json_handler.write_json('data.json', d1)

# Leer el archivo JSON nuevamente
data = json_handler.read_json('data.json')
print(data)
