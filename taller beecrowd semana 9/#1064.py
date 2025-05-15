#1064
numero=[]
ingreso=6
positivos=[]
for i in range (1, ingreso+1):
    N=float(input(""))
    numero.append(N)
for i in numero:
    if i >= 0:
        positivos.append(i)

numeros_positi=len(positivos)
promedio = sum(positivos) / numeros_positi

print(f"{numeros_positi} valores positivos")
print(f"{promedio:.1f}")