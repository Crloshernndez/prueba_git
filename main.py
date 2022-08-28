# Archivo principal

<<<<<<< HEAD
print("Prueba Git")
print("archivo descargado")
=======
print("cambio el print")

def run():
    a, b = 0, 1
    while b <= 1597:
        print(a, b, end=' ')
        a = a + b
        b = a + b

run()
def menu():
    opcion = 0
    salir = 4
    while opcion != salir:
        print ("menu")
        print ("1.- ingresar alumno")
        print ("2.- consultar alumno")
        print ("3.- buscar alumno")
        print ("4.- salir")

        opcion = input ("ingrese una opcion: ")