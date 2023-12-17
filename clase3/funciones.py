
def sumar(num1,num2):
    suma  = num1 + num2
    return suma

print(sumar(3,4))
print(sumar(5,9))
print(sumar(-3,-7))
print(sumar(2,6))

def saludar(nombre):
    print("Hola "+ nombre)


saludar("Maria Alejandra")
saludar("Heberth")

lista = [7,2,1,3,4,6,5,0,8,9]

def mayor(l):
    mayor = -1
    for i in l:
        if i > mayor:
            mayor = i
    return mayor

def menor(list):
    menor = 9999
    for i in list:
        if i < menor:
            menor = i
    return menor
m = mayor(lista)
print(m)
print(menor(lista))
negativos = [-3, -99,-1, -10, 0]
print(menor(negativos))
print(mayor(negativos))

def area_triangulo(base=5, altura=10):
    area = (base * altura)/2
    return area

print(area_triangulo(6, 9))
area_triangulo(6, 9)
print(area_triangulo(6))
print(area_triangulo(6, 5))
print(area_triangulo())

edad = 30
print("Hola Mariale")
print(edad)

def prueba():
    potencia = 5**2
    return potencia


print(prueba())



