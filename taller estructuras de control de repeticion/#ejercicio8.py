#ejercicio 8
total_encuestados=0
total_personas_consumen=0
total_mujeres_menores=0
total_hombre_no_aguardiente=0
edad_cerveza=0
cerveza=0
whisky=0

while True:
    #solicitamos los datos
    consume=int(input("consume alcohol: 1=SI ; 2=NO: "))
    licor_preferido=int(input("1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    edad=int(input("que edad tiene: "))
    sexo=int(input("sexo de la persona: 1=M ; 2=F: "))
    #sumamos todos los encuestados
    if(consume!=0):
        total_encuestados=total_encuestados+1
    #sumamos solo los que toman
    if(consume==1):
        total_personas_consumen=total_personas_consumen+1
    #sumamos las mujer menores de edad 
    if(sexo==2 and edad < 18):
        total_mujeres_menores = total_mujeres_menores+1
    #sumamos los hombres que no toman aguardiente
    if(sexo==1 and licor_preferido!=1 and edad >= 20 and edad <= 25):
        total_hombre_no_aguardiente = total_hombre_no_aguardiente+1
    #sumamamos los que solo toman cerveza
    if(licor_preferido==3):
        cerveza=cerveza+1 
    #sumamos las edades de quienes toman solo cerveza
    if(licor_preferido==3):
        edad_cerveza=edad_cerveza+edad
    #sumamos los que tomando solo whisky
    if(licor_preferido==5):
       whisky=whisky+1

    print(f"total de personas encuestadas que consumen licor: {total_personas_consumen}")
    print(f"total mujeres menores de edad: {total_mujeres_menores}")
    print(f"total de hombres que no consumen aguardiente: {total_hombre_no_aguardiente}")
    #sacamos el promedio de edad de quienes toman cerveza
    if(cerveza>0):
        promedio_edad_cerveza = edad_cerveza/cerveza
        print(f"promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.0f}")
    else:
        print("ninguno toma cerveza ")    
    #sacamos el promedio de las personas q solo consumen whiskey
    if(total_encuestados>0):
       promedio_whiskey = (whisky/total_encuestados)*100
       print(f"porcentaje de personas que consumen whiskey: {promedio_whiskey:.0f}")
    else:
        print("ninguno toma whiskey")
    #solicitamos salir de la encuestas
    continuar=input("desea seguir con la encuesta 1=SI ; 2=No:  ")
    if(continuar ==0):
       break
    
