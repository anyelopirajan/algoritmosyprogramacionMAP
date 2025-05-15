#1865
C=int(input(""))

for i in range (C):
    force=input("")
    nombre, fuerza= force.split(" ")
    nombre=str(nombre)
    fuerza=int(fuerza)
    if (nombre == "Thor"):
        print("Y")
    else:
        print("N")