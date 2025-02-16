#ejercicio4
total_compra = float(input("Ingrese el monto total de la compra: "))
descuento_porcentaje = 0.15  # 15% de descuento
descuento = total_compra * descuento_porcentaje
precio_final = total_compra - descuento

print("El precio final de la compra con descuento es:", precio_final)