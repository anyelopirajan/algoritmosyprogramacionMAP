#ejercicio11
#entrada
t=int(input("digite la temperatura"))
d=""
#caja negra 
if(t>85):
    d="natacion"
elif(t>70 and t<=85):
    d="tenis"
elif(t>32 and t<=70):
    d="golf"
elif(t>10 and t<=32):
    d="esqui"
elif(t>0 and t<=10):
    d="marcha"
    
else:
    d="la temperatura no corresponde"
#salida
print(f"el deporte que practicas es: {d} ")
