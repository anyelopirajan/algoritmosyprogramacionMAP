#ejercicio14
lectura_anterior = int(input("Introduce la lectura anterior en Kwh: "))
lectura_actual = int(input("Introduce la lectura actual en Kwh: "))

consumo = lectura_actual - lectura_anterior

monto_pagar = 0

if consumo <= 100:
    monto_pagar = consumo * 4600
elif 101 <= consumo <= 300:
    monto_pagar = 100 * 4600 + (consumo - 100) * 8000
elif 301 <= consumo <= 500:
    monto_pagar = 100 * 4600 + 200 * 8000 + (consumo - 300) * 100000
else:
    monto_pagar = 100 * 4600 + 200 * 8000 + 200 * 100000 + (consumo - 500) * 120000

print("El monto a pagar por consumo de luz eléctrica y servicio de aseo urbano es:", monto_pagar, "COP")
