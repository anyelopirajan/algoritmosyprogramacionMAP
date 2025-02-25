#ejercicio1

inversion_inicial=float(input("ingrese el valor de la inversion inicial")) 


tasa_interes_anual =float(input("ingrese el valor de la tasa de intereses"))


anos_inversion =int(input("ingrese la cantidad de años de inversion"))


intereses_generados = inversion_inicial * (tasa_interes_anual / 100)

# Verifica si los intereses exceden a $100.000 COP
if intereses_generados > 100000:
    # Reinvierte los intereses
    monto_final = inversion_inicial + intereses_generados
else:
    # No reinvierte los intereses
    monto_final = inversion_inicial

print("Intereses generados:", intereses_generados)
print("Monto final en la cuenta:", monto_final)
