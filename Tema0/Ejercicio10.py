def mayor (num1,num2):
    if num1 > num2:
        return "numero 1 es mayor"
    elif num2 > num1:
        return "numero 2 es mayor"
    else:
        return "Son iguales"

num1=float(input("Introduce el primer numero\n"))
num2=float(input("Introduce el segundo numero\n"))

print(mayor(num1,num2))
