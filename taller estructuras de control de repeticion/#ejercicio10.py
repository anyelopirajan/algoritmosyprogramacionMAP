#ejercicio10
# Verificar si un número es perfecto
def es_numero_perfecto(numero):
    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

numero = int(input("Ingresa un número entero positivo: "))

if numero > 0:
    if es_numero_perfecto(numero):
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")
else:
    print("Por favor ingresa un número positivo.")