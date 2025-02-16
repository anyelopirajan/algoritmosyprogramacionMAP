#ejercicio7
# Solicitar al usuario que ingrese la cantidad en metros
metros = float(input("Ingrese la cantidad en metros: "))

pulgadas = metros * 39.37

pies = pulgadas // 12  
pulgadas_restantes = pulgadas % 12  


print(metros, "metros son equivalentes a", pies, "pies y", pulgadas_restantes, "pulgadas.")