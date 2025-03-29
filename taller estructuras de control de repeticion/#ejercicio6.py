#ejercicio6
# Leer los números
dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))

# Inicializar variables
cociente = 0

# Ciclo para restar sucesivamente
while dividendo >= divisor:
    dividendo = dividendo-divisor
    cociente =cociente +1

# Imprimir los resultados
print("Cociente:", cociente)
print("Residuo:", dividendo)