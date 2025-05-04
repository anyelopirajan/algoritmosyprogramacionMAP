#ejercicio#1
lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
frecuencia = {}  

for numero in lista:
    if numero in frecuencia:
        frecuencia[numero] += 1
    else:
        frecuencia[numero] = 1

print(frecuencia)