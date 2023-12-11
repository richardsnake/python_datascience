
import array as arreglo

l = ["Richard", "Abanto", 35, "M", False, 1.73 ]
lista_paises = ["Peru",  "USA", "Francia"]
lista_enteros = [0,1,2,3,4,5,6,7,8,9,10]
lista_bool = [True, False]
nombre = "Richard"
apellido = "Abanto"
edad =  35
esta_casado = False
lista = [nombre, apellido, edad, esta_casado]

print(l[-1])
print(lista_paises[-2])
print(lista_enteros[-2] + lista_enteros[-6])
print(lista[-3])
print(len(lista_enteros))
l[1] = "Pineda"
print(l) 
print(sum(lista_enteros))
print(min(lista_enteros))
print(max(lista_enteros))

a = arreglo.array('i',lista_enteros)
lista_enteros.append(11)
print(lista_enteros)
a.append(12)
print(a)
lista_enteros.append("12")
print(lista_enteros)
a.append(11)
print(a)
la=[1,5,9,0,""]
lb=[2,4,6,8,""]
lc=[3,7,1,"HOLA", ""]
MATRIZ = [la,lb,lc]

print(MATRIZ[0][0])
print(MATRIZ[1][3])
print(MATRIZ[2][3])

print("diccionarios")

persona = {
    "nombre": "Richard",
    "apellido": "Abanto",
    "edad": 36,
    "sexo": 'M',
    "soltero": True,
    "direccion" :{ 
        "calle" : "Av Alameda sur",
        "nro":  1260
    }
}
clave = "nombre"
print(persona["nombre"])
auto = {
    "marca" : "Toyota",
    "nro_ruedas": 4,
    "nro_puertas": 5,
    "es_full": False
}
print(auto["nro_ruedas"])
print(len(persona))
print(persona.keys())
print(persona.values())
del(persona["sexo"])
print(persona)
