#ejercicio7
n = int(input("Ingresa el número de estudiantes: "))
max_altura = 0
for i in range(n):
    altura = float(input(f"Ingresa la altura del estudiante {i}: "))
    if altura > max_altura:
        max_altura = altura
print("La mayor altura es:", max_altura)