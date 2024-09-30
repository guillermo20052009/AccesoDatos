import csv
import json
class FileConverter:
    def csv_to_json(self, csv_file, json_file):
        try:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            with open(json_file, 'w') as f:
                json.dump(rows, f)
            print(f'Conversión de {csv_file} a {json_file} completada.')
        except Exception as e:
            print(f"Error en la conversión: {e}")
   
    def json_to_csv(self, csv_file, json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            with open(csv_file, mode='w', newline='') as f:
               claves = list(data[0].keys())
               writer = csv.DictWriter(f, fieldnames=claves)
               writer.writeheader()
               writer.writerows(data)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")
    
# Uso
converter = FileConverter()
#converter.csv_to_json('data.csv', 'data.json')
converter.json_to_csv('data.csv','data.json')
