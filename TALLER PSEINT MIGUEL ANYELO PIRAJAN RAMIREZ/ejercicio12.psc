Algoritmo ejercicio12
		Definir examenMatematica, tareaMatematica1, tareaMatematica2, tareaMatematica3 Como Real
		Definir examenFisica, tareaFisica1, tareaFisica2 Como Real
		Definir examenQuimica, tareaQuimica1, tareaQuimica2, tareaQuimica3 Como Real
		Definir promedioMatematica, promedioFisica, promedioQuimica, promedioGeneral Como Real
		
		Escribir "Introduce la calificaci�n del examen de Matem�tica: "
		Leer examenMatematica
		Escribir "Introduce la calificaci�n de la primera tarea de Matem�tica: "
		Leer tareaMatematica1
		Escribir "Introduce la calificaci�n de la segunda tarea de Matem�tica: "
		Leer tareaMatematica2
		Escribir "Introduce la calificaci�n de la tercera tarea de Matem�tica: "
		Leer tareaMatematica3
		
		Escribir "Introduce la calificaci�n del examen de F�sica: "
		Leer examenFisica
		Escribir "Introduce la calificaci�n de la primera tarea de F�sica: "
		Leer tareaFisica1
		Escribir "Introduce la calificaci�n de la segunda tarea de F�sica: "
		Leer tareaFisica2
		
		Escribir "Introduce la calificaci�n del examen de Qu�mica: "
		Leer examenQuimica
		Escribir "Introduce la calificaci�n de la primera tarea de Qu�mica: "
		Leer tareaQuimica1
		Escribir "Introduce la calificaci�n de la segunda tarea de Qu�mica: "
		Leer tareaQuimica2
		Escribir "Introduce la calificaci�n de la tercera tarea de Qu�mica: "
		Leer tareaQuimica3
		
		promedioMatematica = (examenMatematica * 0.90) + (((tareaMatematica1 + tareaMatematica2 + tareaMatematica3) / 3) * 0.10)
		promedioFisica = (examenFisica * 0.80) + (((tareaFisica1 + tareaFisica2) / 2) * 0.20)
		promedioQuimica = (examenQuimica * 0.85) + (((tareaQuimica1 + tareaQuimica2 + tareaQuimica3) / 3) * 0.15)
		
		promedioGeneral = (promedioMatematica + promedioFisica + promedioQuimica) / 3
		
		Escribir "El promedio en Matem�tica es: ", promedioMatematica
		Escribir "El promedio en F�sica es: ", promedioFisica
		Escribir "El promedio en Qu�mica es: ", promedioQuimica
		Escribir "El promedio general en las tres materias es: ", promedioGeneral
	
FinAlgoritmo
