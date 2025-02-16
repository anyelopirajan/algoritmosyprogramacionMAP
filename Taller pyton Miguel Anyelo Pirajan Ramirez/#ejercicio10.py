#ejercicio10

chelines_a_pesetas = 9.56871  
dracmas_a_pesetas = 0.88607  
pesetas_a_francos_franceses = 1 / 20.110  
pesetas_a_dolares = 1 / 122.499  
pesetas_a_liras_italianas = 100 / 9.289  


chelines = float(input("Ingrese la cantidad en chelines austriacos: "))
pesetas_chelines = chelines * chelines_a_pesetas / 100
print(chelines, "chelines austriacos son equivalentes a", pesetas_chelines, "pesetas.")


dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
pesetas_dracmas = dracmas * dracmas_a_pesetas / 100
francos_franceses = pesetas_dracmas * pesetas_a_francos_franceses
print(dracmas, "dracmas griegos son equivalentes a", francos_franceses, "francos franceses.")


pesetas = float(input("Ingrese la cantidad en pesetas: "))
dolares = pesetas * pesetas_a_dolares
liras_italianas = pesetas * pesetas_a_liras_italianas / 100
print(pesetas, "pesetas son equivalentes a", dolares, "dólares y", liras_italianas, "liras italianas.")