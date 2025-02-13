Algoritmo ejercicio10
		Definir chelines, dracmas, pesetas, pesetasADolares, pesetasALiras Como Real
		Definir pesetasDeChelines, francosDeDracmas, dolares, liras Como Real
		
		Escribir "Introduce la cantidad en chelines austriacos: "
		Leer chelines
		pesetasDeChelines = (chelines / 100) * 956.871
		Escribir "Equivalente en pesetas: ", pesetasDeChelines
		
		Escribir "Introduce la cantidad en dracmas griegos: "
		Leer dracmas
		pesetas = (dracmas / 100) * 88.607
		francosDeDracmas = pesetas / 20.110
		Escribir "Equivalente en francos franceses: ", francosDeDracmas
		
		Escribir "Introduce la cantidad en pesetas: "
		Leer pesetasADolares
		dolares = pesetasADolares / 122.499
		Escribir "Equivalente en dólares: ", dolares
		
		Escribir "Introduce la cantidad en pesetas: "
		Leer pesetasALiras
		liras = (pesetasALiras / 100) * 9.289
		Escribir "Equivalente en liras italianas: ", liras

FinAlgoritmo
