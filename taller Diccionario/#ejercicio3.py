#ejercicio3
usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"Bienvenido {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}!")
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos. Intento", intentos)

if intentos == 3:
    print("Has alcanzado el máximo de intentos. Acceso denegado.")