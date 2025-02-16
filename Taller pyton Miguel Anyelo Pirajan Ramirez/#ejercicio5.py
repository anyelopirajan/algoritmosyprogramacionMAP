#ejercicio5
  
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

promedio = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("El promedio de las calificaciones parciales es:", promedio)
print("La calificación final del alumno es:", calificacion_final)