#ejercicio11

nombre = input("Ingrese el nombre del trabajador: ")
horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
pago_hora_normal = float(input("Ingrese el pago por hora normal: "))
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
num_hijos = int(input("Ingrese el número de hijos: "))


sueldo_base = (horas_normales * pago_hora_normal) + (horas_extras * pago_hora_normal * 1.25)


pago_forzoso = sueldo_base * 0.05
politica_habitacional = sueldo_base * 0.02
caja_ahorro = sueldo_base * 0.07
deducciones = pago_forzoso + politica_habitacional + caja_ahorro


actualizacion_academica = 250000
prima_hogar = 180000
asignacion_hijos = num_hijos * 173000
asignaciones = actualizacion_academica + prima_hogar + asignacion_hijos


sueldo_neto = sueldo_base - deducciones + asignaciones


print("\n--- Resultados ---")
print("Nombre:", nombre)
print("Sueldo base:", sueldo_base)
print("Deducciones:")
print("  Pago forzoso:", pago_forzoso)
print("  Política habitacional:", politica_habitacional)
print("  Caja de ahorro:", caja_ahorro)
print("  Total deducciones:", deducciones)
print("Asignaciones:")
print("  Actualización académica:", actualizacion_academica)
print("  Prima por hogar:", prima_hogar)
print("  Asignación por hijos:", asignacion_hijos)
print("  Total asignaciones:", asignaciones)
print("Sueldo neto:", sueldo_neto)