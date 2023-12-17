def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def residuo(num1, num2):
    return num1 % num2

def potencia(num1, num2):
    return num1 ** num2


x = int(input("ingrese valor de x: "))
y = int(input("ingrese valor de y: "))

print("La suma de X y Y es: ", sumar(x,y))
print("La resta de X y Y es: ", restar(x,y))
print("La multiplicacion de X y Y es: ", multiplicar(x,y))
print("La division de X y Y es: ", dividir(x,y))
print("El residuo de X y Y es: ", residuo(x,y))
print("La potencia de X y Y es: ", potencia(x,y))