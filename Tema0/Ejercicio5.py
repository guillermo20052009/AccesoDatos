num1 = int(input("Introduce el primer numero\n"))

while num1 < 1 or num1 > 7:
    num1 = int(input("Entre 1 y 7\n"))
    
if num1 == 1:
    print("Lunes")
elif num1 == 2:
    print("Martes")
elif num1 == 3:
    print("Miercoles")
elif num1 == 4:
    print("Jueves")
elif num1 == 5:
    print("Viernes")
elif num1 == 6:
    print("Sabado")
elif num1 == 7:
    print("Domingo")
