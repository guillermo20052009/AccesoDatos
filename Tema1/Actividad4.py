import csv
import json
class FileConverter:

    #Metodo explicado en el tema
    def csv_to_json(self, csv_file, json_file):
        try:
            #Abrimos el archivo CSV modo lectura
            with open(csv_file, 'r') as f:
                #Instanciamos un objeto DictReader que nos va a servir
                #para leer del csv
                reader = csv.DictReader(f)
                #Obtenemos las filas haciendo uso de list
                rows = list(reader)
                #Abrimos en modo Escritura
            with open(json_file, 'w') as f:
                #Con dump escribimos las filas del archivo CSV
                json.dump(rows, f)
            print(f'Conversión de {csv_file} a {json_file} completada.')
        except Exception as e:
            print(f"Error en la conversión: {e}")
   
    def json_to_csv(self, csv_file, json_file):
        try:
            #Abrimos en modo lectura
            with open(json_file, 'r') as f:
                #Cargamos con .load el contenido del archivo json
                data = json.load(f)
                #Abrimos el CSV en modo escritura, newline lo ponemos porque
                #da un mejor formato de los saltos de linea
            with open(csv_file, mode='w', newline='') as f:
                #Obtenemos las claves del contenido del archivo CSV
                claves = list(data.keys())
               #Instanciamos un objeto de la clave DictWriter que se usa para
               #escribir en el fichero CSV, fieldname serán los nombre de los campos
                writer = csv.DictWriter(f, fieldnames=claves)
               #Escribimos los campos
                writer.writeheader()
               #Escribimos cada una de las filas de datos
                writer.writerow(data)
                print("Se ha transformado correctamente")
        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")
    
# Uso
converter = FileConverter()
#converter.csv_to_json('data.csv', 'data.json')
converter.json_to_csv('data.csv','data.json')
