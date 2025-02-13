Algoritmo ejercicio12
		Definir examenMatematica, tareaMatematica1, tareaMatematica2, tareaMatematica3 Como Real
		Definir examenFisica, tareaFisica1, tareaFisica2 Como Real
		Definir examenQuimica, tareaQuimica1, tareaQuimica2, tareaQuimica3 Como Real
		Definir promedioMatematica, promedioFisica, promedioQuimica, promedioGeneral Como Real
		
		Escribir "Introduce la calificación del examen de Matemática: "
		Leer examenMatematica
		Escribir "Introduce la calificación de la primera tarea de Matemática: "
		Leer tareaMatematica1
		Escribir "Introduce la calificación de la segunda tarea de Matemática: "
		Leer tareaMatematica2
		Escribir "Introduce la calificación de la tercera tarea de Matemática: "
		Leer tareaMatematica3
		
		Escribir "Introduce la calificación del examen de Física: "
		Leer examenFisica
		Escribir "Introduce la calificación de la primera tarea de Física: "
		Leer tareaFisica1
		Escribir "Introduce la calificación de la segunda tarea de Física: "
		Leer tareaFisica2
		
		Escribir "Introduce la calificación del examen de Química: "
		Leer examenQuimica
		Escribir "Introduce la calificación de la primera tarea de Química: "
		Leer tareaQuimica1
		Escribir "Introduce la calificación de la segunda tarea de Química: "
		Leer tareaQuimica2
		Escribir "Introduce la calificación de la tercera tarea de Química: "
		Leer tareaQuimica3
		
		promedioMatematica = (examenMatematica * 0.90) + (((tareaMatematica1 + tareaMatematica2 + tareaMatematica3) / 3) * 0.10)
		promedioFisica = (examenFisica * 0.80) + (((tareaFisica1 + tareaFisica2) / 2) * 0.20)
		promedioQuimica = (examenQuimica * 0.85) + (((tareaQuimica1 + tareaQuimica2 + tareaQuimica3) / 3) * 0.15)
		
		promedioGeneral = (promedioMatematica + promedioFisica + promedioQuimica) / 3
		
		Escribir "El promedio en Matemática es: ", promedioMatematica
		Escribir "El promedio en Física es: ", promedioFisica
		Escribir "El promedio en Química es: ", promedioQuimica
		Escribir "El promedio general en las tres materias es: ", promedioGeneral
	
FinAlgoritmo
