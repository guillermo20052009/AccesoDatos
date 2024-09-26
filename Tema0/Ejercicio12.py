import random #Esta libreria nos va a permitir generar numeros aleatorios 
numeros = []

for i in range (1,11):
    numeros.append(random.randint(1,50))
    #El metodo random.randint nos permite generar un numero entero aleatorio
    #entre los numero que les pasamos como parametro en este caso 1 y 50
print(numeros)
