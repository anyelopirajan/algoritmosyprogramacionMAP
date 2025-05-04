diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

valores_unicos = set() 

for valor in diccionario.values():
    valores_unicos.add(valor)  

lista_resultado = list(valores_unicos)
print(lista_resultado)