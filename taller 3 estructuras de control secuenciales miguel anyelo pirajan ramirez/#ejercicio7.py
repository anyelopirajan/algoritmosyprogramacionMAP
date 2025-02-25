#ejercicio7

distancia_recorrida = int(input("Introduce la distancia recorrida en kilómetros: "))
pago = 0
if distancia_recorrida <= 300:
    pago = 50000
elif distancia_recorrida > 300 and distancia_recorrida < 1000:
    pago = 70000 + (distancia_recorrida - 300) * 30000
else:
    pago = 150000 + (distancia_recorrida - 1000) * 9000

print("El monto a pagar es:", pago, "COP")
