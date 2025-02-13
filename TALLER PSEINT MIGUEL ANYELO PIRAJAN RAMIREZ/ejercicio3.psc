Algoritmo ejercicio3
		Definir sueldoBase, venta1, venta2, venta3, comision, totalComisiones, totalPago Como Real
		Escribir "Introduce el sueldo base del vendedor: "
		Leer sueldoBase
		Escribir "Introduce el monto de la primera venta: "
		Leer venta1
		Escribir "Introduce el monto de la segunda venta: "
		Leer venta2
		Escribir "Introduce el monto de la tercera venta: "
		Leer venta3
		comision = 0.10
		totalComisiones = (venta1 + venta2 + venta3) * comision
		totalPago = sueldoBase + totalComisiones
		Escribir "El total de comisiones por las ventas es: ", totalComisiones
		Escribir "El pago total que recibirá el vendedor es: ", totalPago	
FinAlgoritmo
