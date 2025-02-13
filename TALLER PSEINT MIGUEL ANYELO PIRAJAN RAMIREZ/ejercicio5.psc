Algoritmo ejercicio5
		Definir parcial1, parcial2, parcial3, examenFinal, trabajoFinal, promedioParciales, calificacionFinal Como Real
		Escribir "Introduce la calificación del primer parcial: "
		Leer parcial1
		Escribir "Introduce la calificación del segundo parcial: "
		Leer parcial2
		Escribir "Introduce la calificación del tercer parcial: "
		Leer parcial3
		Escribir "Introduce la calificación del examen final: "
		Leer examenFinal
		Escribir "Introduce la calificación del trabajo final: "
		Leer trabajoFinal
		promedioParciales = (parcial1 + parcial2 + parcial3) / 3
		calificacionFinal = (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)
		Escribir "La calificación final en la materia de computación es: ", calificacionFinal
FinAlgoritmo
