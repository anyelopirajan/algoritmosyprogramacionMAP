#ejercicio5
# entradas
suma = 0
k = 1
cantidad_terminos = 0

# caja negra
while (suma + k <= 1000):
    suma = suma+ k
    cantidad_terminos =  cantidad_terminos+1
    k = k+1

# salida
print("Número de términos necesarios:", cantidad_terminos)