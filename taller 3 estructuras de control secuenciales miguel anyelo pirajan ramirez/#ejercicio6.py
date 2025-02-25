#ejercicio6

A = int(input("Introduce el dígito A: "))
B = int(input("Introduce el dígito B: "))
C = int(input("Introduce el dígito C: "))
D = int(input("Introduce el dígito D: "))

N = A * 1000 + B * 100 + C * 10 + D


if C >= 5:
    N_redondeado = ((N // 100) + 1) * 100
else:
    N_redondeado = (N // 100) * 100

# Mostrar el resultado
print("El número original es:", N)
print("El número redondeado a la centena más próxima es:", N_redondeado)
