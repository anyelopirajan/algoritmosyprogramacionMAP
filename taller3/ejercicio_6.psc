Algoritmo ejercicio_6
	Escribir "ingrese un año"
	Leer año	
	operacion1=año%4
	operacion2=año%400
	operacion3=año%100
	Si operacion1=0 & operacion2=0 Entonces
		Escribir"es bisiesto"
	SiNo
		si operacion3=1 Entonces			
			Escribir "no es bisiesto"
		FinSi
	Fin Si
FinAlgoritmo
