#ejercicio3
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

comision_porcentaje = 0.10  # 10% de comisión
comisiones = (venta1 + venta2 + venta3) * comision_porcentaje
sueldo_total = sueldo_base + comisiones
print("El monto total de las comisiones es:", comisiones)
print("El sueldo total del vendedor es:", sueldo_total)