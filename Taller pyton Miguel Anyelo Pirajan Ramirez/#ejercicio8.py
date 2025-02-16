#ejercicio8

a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))


s = (a + b + c) / 2


area = (s * (s - a) * (s - b) * (s - c)) ** 0.5


print("El área del triángulo es:", area)