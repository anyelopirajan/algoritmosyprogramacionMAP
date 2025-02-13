Algoritmo ejercicio21
		Definir P, T, totalCuotas, recargo, porcentajeRecargo Como Real
		Escribir "Introduce el precio al contado (P): "
		Leer P
		Escribir "Introduce el monto de la cuota mensual (T): "
		Leer T
		totalCuotas = T * 12
		recargo = totalCuotas - P
		porcentajeRecargo = (recargo / P) * 100
		Escribir "El porcentaje de recargo aplicado es: ", porcentajeRecargo, "%"
FinAlgoritmo
