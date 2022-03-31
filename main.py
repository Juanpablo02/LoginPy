# Crear login usuario "admin" contra "aadmin123" y que dig verdadero, sino cuente las veces que se intento

usuario = "admin"
contraseña = "admin123"

def login():
    contador = 0
    intentos = 0
    while contador < 1:
        usuario  = input("Usuario: ")
        contraseña = input("contraseña: ")
        if(usuario == "admin" and contraseña == "admin123"):
            print("Verdadero")
            contador = 2
            print(intentos)
        else:
            intentos+=1
print(login())