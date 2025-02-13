Algoritmo ejercicio15
		Definir precioFinal, PVP, descuento Como Real
		Escribir "Introduce el precio final pagado por el producto: "
		Leer precioFinal
		Escribir "Introduce el precio de venta al público (PVP) del producto: "
		Leer PVP
		descuento = ((PVP - precioFinal) / PVP) * 100
		Escribir "El porcentaje de descuento aplicado es: ", descuento, "%"
FinAlgoritmo
