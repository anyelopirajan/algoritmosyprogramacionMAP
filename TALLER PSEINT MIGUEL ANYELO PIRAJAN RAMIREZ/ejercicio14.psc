Algoritmo ejercicio14
		Definir lecturaAnterior, lecturaActual, costoPorKilovatio, consumo, montoTotal Como Real
		Escribir "Introduce la lectura anterior (en kilovatios): "
		Leer lecturaAnterior
		Escribir "Introduce la lectura actual (en kilovatios): "
		Leer lecturaActual
		Escribir "Introduce el costo por kilovatio: "
		Leer costoPorKilovatio
		consumo = lecturaActual - lecturaAnterior
		montoTotal = consumo * costoPorKilovatio
		Escribir "El monto total a pagar por el consumo de luz eléctrica es: ", montoTotal, " COP"	
FinAlgoritmo
