#ejercicio5
# Ventas de los tres departamentos
ventas_departamento1 = float(input("ingrese el valor de ventas del departamento 1:"))
ventas_departamento2 = float(input("ingrese el valor de ventas del departamento 2:")) 
ventas_departamento3 = float(input("ingrese el valor de ventas del departamento 3:")) 

sueldo_bruto = float(input("ingrese el monto del sueldo:"))

ventas_totales = ventas_departamento1 + ventas_departamento2 + ventas_departamento3

limite_incentivo = ventas_totales * 0.33

incentivo_departamento1 = 0
incentivo_departamento2 = 0
incentivo_departamento3 = 0


if ventas_departamento1 > limite_incentivo:
    incentivo_departamento1 = sueldo_bruto * 0.20
if ventas_departamento2 > limite_incentivo:
    incentivo_departamento2 = sueldo_bruto * 0.20
if ventas_departamento3 > limite_incentivo:
    incentivo_departamento3 = sueldo_bruto * 0.20

nuevo_sueldo_departamento1 = sueldo_bruto + incentivo_departamento1
nuevo_sueldo_departamento2 = sueldo_bruto + incentivo_departamento2
nuevo_sueldo_departamento3 = sueldo_bruto + incentivo_departamento3


print("Nuevo sueldo de los vendedores del departamento 1:", nuevo_sueldo_departamento1)
print("Nuevo sueldo de los vendedores del departamento 2:", nuevo_sueldo_departamento2)
print("Nuevo sueldo de los vendedores del departamento 3:", nuevo_sueldo_departamento3)
