tupla1 = (1,2,3,4,5,6,7, False, "Richard", 7,"C")
print(tupla1)
print(tupla1[-1])
edad = 36
tupla2 = ("a", "b", "c", edad)
print(tupla1 == tupla2)
print(10 in tupla1)
print(tupla2[0:6])
print(tupla1[0:10])
t3 = tupla1 + tupla2
print(t3 == tupla1)

print(36 in tupla2) 
print(tupla2*3)

auto = {
    "marca" : "Toyota",
    "nro_ruedas": 4,
    "nro_puertas": 5,
    "es_full": False,
    "marca": "Toyata"
}
print(auto)