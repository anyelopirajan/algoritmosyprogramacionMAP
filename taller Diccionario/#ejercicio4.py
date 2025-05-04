#ejercicio4
estudiantes = {}  
max_estudiantes = 10  

for i in range(1, max_estudiantes + 1):
    nombre = input(f"Ingrese el nombre del estudiante {i}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[str(i)] = {"nombre": nombre, "nota": nota}

aprobados = []
suspendidos = []
suma_notas = 0

for datos in estudiantes.values():
    suma_notas += datos["nota"]
    if datos["nota"] >= 5:
        aprobados.append(datos["nombre"])
    else:
        suspendidos.append(datos["nombre"])

nota_media = suma_notas / len(estudiantes)

print("\nEstudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspendidos)
print(f"Nota media de la clase: {nota_media:.2f}")