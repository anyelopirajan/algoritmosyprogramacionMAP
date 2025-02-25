#ejercicio9
nombre_cliente = input("Introduce el nombre del cliente: ")
monto_compra = float(input("Introduce el monto de la compra en COP: "))

descuento = 0
monto_pagar = 0

if monto_compra < 50000:
    descuento = 0
    monto_pagar = monto_compra
elif 50000 <= monto_compra <= 100000:
    descuento = monto_compra * 0.05
    monto_pagar = monto_compra - descuento
elif 100000 < monto_compra <= 700000:
    descuento = monto_compra * 0.11
    monto_pagar = monto_compra - descuento
elif 700000 < monto_compra <= 1500000:
    descuento = monto_compra * 0.18
    monto_pagar = monto_compra - descuento
else:
    descuento = monto_compra * 0.25
    monto_pagar = monto_compra - descuento

print("Nombre del cliente: " + nombre_cliente)
print("Monto de la compra: " + str(monto_compra) + " COP")
print("Descuento recibido: " + str(descuento) + " COP")
print("Monto a pagar: " + str(monto_pagar) + " COP")
