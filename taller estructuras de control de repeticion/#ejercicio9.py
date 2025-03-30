#ejercicio 9
nombre=()
estudiantes_alto=()
estudiante_bajo=()
puntaje_maximo=0
puntaje_minimo=0
total_estudiantes=0

while True:
    estudiante=input("nombre del estudiante: ")
    puntaje=float(input("ingrese su puntaje: "))

    if(puntaje!=-1):
        total_estudiantes=total_estudiantes+1

    if(puntaje>puntaje_maximo):
        nombre=estudiante
        puntaje_maximo=puntaje_maximo+puntaje

    if(puntaje<puntaje_maximo):
        nombre=estudiante
        puntaje_minimo=puntaje_minimo+puntaje


    print(f"Nombre del estudiantes con el puntaje mas alto: {nombre}")
    print(f"puntaje_maximo obtenido: {puntaje_maximo:.0f}")
    print(f"Nombre del estudiantes con el puntaje mas bajo: {estudiante}")
    print(f"puntaje_minimo obtenido: {puntaje_minimo:.0f}")        
    