#ejercicio3
#entrada
a=int(input("ingrese el dato a"))
b=int(input("ingrese el dato b")) 
c=int(input("ingrese el dato c"))
d=int(input("ingrese el dato d"))  
p=int
#caja negra
if(d==0):
    p=(a-c)**2
elif(d>0):
    p=((a-b)**3)/d
#salida
print("el resultado es ",p)
print("los datos son","a",a,"b",b,"c",c,"d",d)