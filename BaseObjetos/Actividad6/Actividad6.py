import ZODB, ZODB.FileStorage, transaction, copy
from persistent import Persistent

# Clases Coche y Motor
class Coche(Persistent):
    def __init__(self, nombre, modelo, año, tipo, nombre_motor):
        self.nombre = nombre
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.nombre_motor = nombre_motor

class Motor(Persistent):
    def __init__(self, nombre, potencia, año):
        self.nombre = nombre
        self.potencia = potencia
        self.año = año

# Crear el objeto Motor
motor_original = Motor("V8", 450, 2020)

# Crear el objeto Coche usando el objeto Motor
coche_original = Coche("Ford", "Mustang", 2021, "Gasolina", motor_original)

# Realizar una copia profunda del objeto Coche
coche_copia = copy.deepcopy(coche_original)

# Modificar algunos atributos del objeto copiado
coche_copia.nombre = "Chevrolet"
coche_copia.modelo = "Camaro"
coche_copia.nombre_motor.nombre = "V6"
coche_copia.nombre_motor.potencia = 350

# Imprimir para verificar que los cambios en la copia no afectaron al original
print("Objeto Coche original:")
print(f"Nombre: {coche_original.nombre}, Modelo: {coche_original.modelo}, Año: {coche_original.año}, Tipo: {coche_original.tipo}")
print(f"Motor - Nombre: {coche_original.nombre_motor.nombre}, Potencia: {coche_original.nombre_motor.potencia}, Año: {coche_original.nombre_motor.año}")

print("\nObjeto Coche copiado:")
print(f"Nombre: {coche_copia.nombre}, Modelo: {coche_copia.modelo}, Año: {coche_copia.año}, Tipo: {coche_copia.tipo}")
print(f"Motor - Nombre: {coche_copia.nombre_motor.nombre}, Potencia: {coche_copia.nombre_motor.potencia}, Año: {coche_copia.nombre_motor.año}")
