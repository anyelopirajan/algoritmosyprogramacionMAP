Algoritmo ejercicio_8
	Escribir "ingrese la nota"
	leer calificacion
	
	Si calificacion >= 90 Entonces
		Escribir "A"
	SiNo
		Si calificacion >= 80 & calificacion <90 Entonces
			Escribir "B"
		SiNo
			Si calificacion >= 70 & calificacion < 80 Entonces
				Escribir "C"
			SiNo
				Si calificacion >= 60 & calificacion < 70 Entonces
					Escribir "D"
				SiNo
					Si calificacion < 60 Entonces
						Escribir  "F"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
