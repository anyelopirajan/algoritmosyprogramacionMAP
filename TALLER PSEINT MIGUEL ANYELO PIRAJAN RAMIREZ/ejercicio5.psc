Algoritmo ejercicio5
		Definir parcial1, parcial2, parcial3, examenFinal, trabajoFinal, promedioParciales, calificacionFinal Como Real
		Escribir "Introduce la calificaci�n del primer parcial: "
		Leer parcial1
		Escribir "Introduce la calificaci�n del segundo parcial: "
		Leer parcial2
		Escribir "Introduce la calificaci�n del tercer parcial: "
		Leer parcial3
		Escribir "Introduce la calificaci�n del examen final: "
		Leer examenFinal
		Escribir "Introduce la calificaci�n del trabajo final: "
		Leer trabajoFinal
		promedioParciales = (parcial1 + parcial2 + parcial3) / 3
		calificacionFinal = (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)
		Escribir "La calificaci�n final en la materia de computaci�n es: ", calificacionFinal
FinAlgoritmo
