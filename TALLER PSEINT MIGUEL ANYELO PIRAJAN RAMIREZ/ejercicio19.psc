Algoritmo ejercicio19
		Definir x, l, k, costoTotal, ganancia, porcentajeGanancia Como Real
		Escribir "Introduce la cantidad de naranjas (X): "
		Leer x
		Escribir "Introduce el precio por docena (Y): "
		Leer l
		Escribir "Introduce el monto total obtenido al vender todas las naranjas (K): "
		Leer K
		costoTotal = (X / 12) * l
		ganancia = K - costoTotal
		porcentajeGanancia = (ganancia / costoTotal) * 100
		Escribir "El porcentaje de ganancia obtenida es: ", porcentajeGanancia, "%"

FinAlgoritmo
