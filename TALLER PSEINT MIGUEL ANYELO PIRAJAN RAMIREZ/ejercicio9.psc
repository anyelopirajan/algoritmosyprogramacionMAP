Algoritmo ejercicio9
		Definir horasTrabajadas, precioPorHora, sueldoBase, descuentoImpuestos, salarioNeto Como Real
		Escribir "Introduce el número de horas trabajadas: "
		Leer horasTrabajadas
		Escribir "Introduce el precio por hora: "
		Leer precioPorHora
		sueldoBase = horasTrabajadas * precioPorHora
		descuentoImpuestos = sueldoBase * 0.20
		salarioNeto = sueldoBase - descuentoImpuestos
		Escribir "El sueldo base es: ", sueldoBase, " COP"
		Escribir "El descuento por impuestos es: ", descuentoImpuestos, " COP"
		Escribir "El salario neto es: ", salarioNeto, " COP"
FinAlgoritmo
