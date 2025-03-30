# Saldo inicial de la cuenta
saldo = 1000 

def mostrar_menu():
    print("\n--- Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ") 
    
    if opcion == "1":
        # Depositar dinero
        deposito = float(input("Ingresa la cantidad a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Has depositado ${deposito:}.")
        else:
            print("El monto a depositar debe ser positivo.")
    
    elif opcion == "2":
        # Retirar dinero
        retiro = float(input("Ingresa la cantidad a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Has retirado ${retiro:}.")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("El monto a retirar debe ser positivo.")
    
    elif opcion == "3":
        # Consultar saldo
        print(f"Tu saldo actual es: ${saldo:}.")
    
    elif opcion == "4":
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
