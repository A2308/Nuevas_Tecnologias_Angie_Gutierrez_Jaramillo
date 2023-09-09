"""print("1. Registro?\n 2. Login \n 3. Salir")
opc = 0

if opc == 1:
    print("Registro")
elif opc == 2:
    print("Login")
elif opc == 3:
    print("Salir")
else:
    print("Seleccione una opción valida")"""
    
# Generar un programa que permita hacer el registro e iniciar sesión, dentro de un while
#debe imprimir el menú usando la implementación de if, elif, else (selector multiple)
# Cuando inicie sesión que implemente la solución del calculo de cuotas
#creada en el reto anterior
import time
import os
import getpass
 
#declaracion de variables
 
User = ('Angie')
Clave = ('1098')
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in User:
        if passw in Clave:
            return 1
        else:
            print("\n\tUsuario o contraseña incorrectos...\n")
    else:
        return 2
 
 #inicializacion de procesos
usuario=input('User: ')
passw = getpass.getpass('Password: ')
 
if login(usuario,passw)==1:
    print('Welcome ',usuario)
else:
    print('ERROR! El usuario no está registrado.')
    
#################################    ##################################################
print("1. Registro\n 2. Compra \n 3. Salir")
ang = 0

if ang == "1":
    print("Registro")
elif ang == "2":
    print("Compra")
elif ang == "3":
    print("Salir")
else:
    print("Seleccione una opción valida")