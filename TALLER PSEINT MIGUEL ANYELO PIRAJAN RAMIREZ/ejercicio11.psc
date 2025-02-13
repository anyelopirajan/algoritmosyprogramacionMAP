Algoritmo ejercicio11
		Definir nombre Como Caracter
		Definir horasNormales, pagoHoraNormal, horasExtras, numHijos, totalAsignaciones, totalDeducciones, sueldoBase, sueldoNeto Como Real
		Definir pagoHorasExtras, deduccionForzoso, deduccionPolitica, deduccionCajaAhorro, actualizacionAcademica, primaHogar, pagoExtraHijos Como Real
		
		Escribir "Introduce el nombre del trabajador: "
		Leer nombre
		Escribir "Introduce el número de horas normales trabajadas: "
		Leer horasNormales
		Escribir "Introduce el pago por una hora normal: "
		Leer pagoHoraNormal
		Escribir "Introduce el número de horas extras trabajadas: "
		Leer horasExtras
		Escribir "Introduce el número de hijos: "
		Leer numHijos
		pagoHorasExtras = horasExtras * pagoHoraNormal * 1.25
		sueldoBase = horasNormales * pagoHoraNormal
		deduccionForzoso = sueldoBase * 0.05
		deduccionPolitica = sueldoBase * 0.02
		deduccionCajaAhorro = sueldoBase * 0.07
		actualizacionAcademica = 250000
		primaHogar = 180000
		pagoExtraHijos = numHijos * 173000
		totalAsignaciones = sueldoBase + pagoHorasExtras + actualizacionAcademica + primaHogar + pagoExtraHijos
		totalDeducciones = deduccionForzoso + deduccionPolitica + deduccionCajaAhorro
		sueldoNeto = totalAsignaciones - totalDeducciones
		Escribir "Asignaciones: ", totalAsignaciones
		Escribir "Deducciones: ", totalDeducciones
		Escribir "Sueldo neto de ", nombre, " para el mes de diciembre es: ", sueldoNeto
FinAlgoritmo
