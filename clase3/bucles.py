
lista = [7,2,1,3,4,6,5,0,8,9]
#for
print("antes del for")
suma = 0
#suma de elementos de una lista 
for i in lista:
    print("valor de suma: "+str(suma))
    print("valor de i: "+str(i))
    suma = suma + i
print("despues del for "+str(suma))
#encontrar el mayor valor de la lista
mayor = -1 

for x in lista:
    print("x: "+str(x))

    if x > mayor:
        mayor = x

    print("mayor: "+str(mayor))

print("El mayor valor de la lista es: "+str(mayor) )


#obtener el menor valor de la lista
menor = 100
for y in lista:
    print("y: "+str(y))
    if y < menor:
        menor = y

    print("menor: "+str(menor))
else:
    print("se termino de recorrer la lista")
    print("fin")

print("El menor valor de la lista es: "+str(menor) )

#while
print("inicio while")
num = 1
while num <=10:
    print(num, "Jhon")
    num = num + 1
else:
    print("se terminó el while")
print("fin")

#ejemplo de break [7,2,1,3,4,6,5,0,8,9]

#break: rompe el bucle
#continue: reinicia el bucle con el siguiente valor
#pass : te permite ejecutar la sioguiente linea de codigo (igual como si no existiera)

for i in lista:
    print(i)
    if i%2==0:
        break
    print("despues de la condicion")
    continue #pass
    print("despues del continue")

print("otra nueva linea")