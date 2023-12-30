
fd = open("archivo.txt",  "r")

#print(fd.read())
print(fd.readline())
print("------")
for line in fd:
    print(line)

print("=======")
print(fd.readline())
fd.seek(0)
print(fd.readline())
print(fd.closed)
if(not fd.closed):
    print(fd.readline())
else:
    print("el archivo está cerrado ...") 

fd.close()
if(not fd.closed):
    print(fd.readline())
else:
    print("el archivo está cerrado ...")
print(fd.closed)

fd = open("archivo.txt", "w")
fd.write("bye bye\n")
fd.writelines(["que te vaya bien\n", "saludos\n", "chao\n"])

fd.close()

fd = open("archivo.txt", "a")
fd.write("hola otra vez\n")
fd.close

fd = open("archivo.txt", "r+")

print(fd.readlines())
fd.write("estoy leyendo y escribiendo ...")

fd.close()