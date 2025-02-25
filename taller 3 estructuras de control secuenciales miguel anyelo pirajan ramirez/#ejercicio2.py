#ejercicio2

sueldo = float(input("ingrese el valor de su sueldo"))


if sueldo < 900000:
    aumento = sueldo * 0.15
else:
    aumento = sueldo * 0.12


nuevo_sueldo = sueldo + aumento

print("El nuevo sueldo del trabajador es:", nuevo_sueldo)
