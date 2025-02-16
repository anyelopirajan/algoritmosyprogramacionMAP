#ejercicio9

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora: "))


sueldo_base = horas_trabajadas * precio_hora


impuestos = sueldo_base * 0.20


salario_neto = sueldo_base - impuestos


print("El sueldo base del trabajador es:", sueldo_base)
print("El descuento por impuestos es:", impuestos)
print("El salario neto del trabajador es:", salario_neto)