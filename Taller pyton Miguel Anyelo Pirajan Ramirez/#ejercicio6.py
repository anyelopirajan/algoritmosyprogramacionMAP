#ejercicio6

num_hombres = int(input("Ingrese el número de hombres en el grupo: "))
num_mujeres = int(input("Ingrese el número de mujeres en el grupo: "))

total_estudiantes = num_hombres + num_mujeres

porcentaje_hombres = (num_hombres / total_estudiantes) * 100

porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100

print("El porcentaje de hombres en el grupo es:", porcentaje_hombres, "%")
print("El porcentaje de mujeres en el grupo es:", porcentaje_mujeres, "%")