#ejercicio10
categoria = int(input("Introduce la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Introduce el sueldo bruto del trabajador en COP: "))

aumento = 0

if categoria == 1 and sueldo_bruto == 5000000:
    aumento = sueldo_bruto * 0.10
elif categoria == 2 and sueldo_bruto == 4300000:
    aumento = sueldo_bruto * 0.15
elif categoria == 3 and sueldo_bruto == 3600000:
    aumento = sueldo_bruto * 0.20
elif categoria == 4 and sueldo_bruto == 2000000:
    aumento = sueldo_bruto * 0.40
elif categoria == 5 and sueldo_bruto == 900000:
    aumento = sueldo_bruto * 0.60

nuevo_sueldo = sueldo_bruto + aumento

print("Categoría del trabajador: " + str(categoria))
print("Sueldo bruto del trabajador: " + str(sueldo_bruto) + " COP")
print("Aumento recibido: " + str(aumento) + " COP")
print("Nuevo sueldo del trabajador: " + str(nuevo_sueldo) + " COP")
