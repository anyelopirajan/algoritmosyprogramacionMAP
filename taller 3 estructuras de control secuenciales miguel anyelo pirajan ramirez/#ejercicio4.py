#ejercicio4
monto_compra = float(input("ingrese el monto total de la compra"))  
cantidad_inversion = 0
cantidad_credito = 0
monto_intereses = 0
cantidad_prestamo_banco = 0

if monto_compra > 5000000:
    cantidad_inversion = monto_compra * 0.055
    cantidad_prestamo_banco = monto_compra * 0.30
    cantidad_credito = monto_compra - cantidad_inversion - cantidad_prestamo_banco
else:
    cantidad_inversion = monto_compra * 0.70
    cantidad_credito = monto_compra * 0.30
monto_intereses = cantidad_credito * 0.20

print("Cantidad a invertir de los fondos de la empresa:", cantidad_inversion)
print("Cantidad a pagar a crédito al fabricante:", cantidad_credito)
print("Monto a pagar por intereses:", monto_intereses)
if monto_compra > 5000000:
    print("Cantidad prestada al banco:", cantidad_prestamo_banco)
