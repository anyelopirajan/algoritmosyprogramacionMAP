#ejercicio12

print("--- Matemática ---")
examen_matematica = float(input("Ingrese la calificación del examen de matemáticas: "))
tarea1_matematica = float(input("Ingrese la calificación de la primera tarea de matemáticas: "))
tarea2_matematica = float(input("Ingrese la calificación de la segunda tarea de matemáticas: "))
tarea3_matematica = float(input("Ingrese la calificación de la tercera tarea de matemáticas: "))

promedio_tareas_matematica = (tarea1_matematica + tarea2_matematica + tarea3_matematica) / 3
promedio_matematica = (examen_matematica * 0.90) + (promedio_tareas_matematica * 0.10)

print("Promedio de tareas:", promedio_tareas_matematica)
print("Promedio final de matemáticas:", promedio_matematica)


print("\n--- Física ---")
examen_fisica = float(input("Ingrese la calificación del examen de física: "))
tarea1_fisica = float(input("Ingrese la calificación de la primera tarea de física: "))
tarea2_fisica = float(input("Ingrese la calificación de la segunda tarea de física: "))

promedio_tareas_fisica = (tarea1_fisica + tarea2_fisica) / 2
promedio_fisica = (examen_fisica * 0.80) + (promedio_tareas_fisica * 0.20)

print("Promedio de tareas:", promedio_tareas_fisica)
print("Promedio final de física:", promedio_fisica)


print("\n--- Química ---")
examen_quimica = float(input("Ingrese la calificación del examen de química: "))
tarea1_quimica = float(input("Ingrese la calificación de la primera tarea de química: "))
tarea2_quimica = float(input("Ingrese la calificación de la segunda tarea de química: "))
tarea3_quimica = float(input("Ingrese la calificación de la tercera tarea de química: "))

promedio_tareas_quimica = (tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3
promedio_quimica = (examen_quimica * 0.85) + (promedio_tareas_quimica * 0.15)

print("Promedio de tareas:", promedio_tareas_quimica)
print("Promedio final de química:", promedio_quimica)


promedio_general = (promedio_matematica + promedio_fisica + promedio_quimica) / 3

print("\n--- Promedio general ---")
print("El promedio general de las tres materias es:", promedio_general)