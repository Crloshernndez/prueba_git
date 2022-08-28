# Archivo principal
import os



print("Prueba Git")
print("archivo descargado")

print("cambio el print")

#def run():
#    a, b = 0, 1
#    while b <= 1597:
#        print(a, b, end=' ')
#        a = a + b
#        b = a + b
#
#run()


def menu():
    menu = """
    SELECCIONE UNA OPCION

     a . ---------> ingresar alumno
     b . ---------> consultar alumno
     c . ---------> buscar alumno
     d . ---------> eliminar

     s . ---------> SALIR
    """

    opciones = {
        'a' : 'ingresar alumno',
        'b' : 'consultar alumno',
        'c' : 'buscar alumno',
        'd' : 'eliminar'
    }


    opcion_seleccionada = input(menu).lower()
    os.system("clear")
    while opcion_seleccionada != "s":
        if opcion_seleccionada in opciones:
          opcion_ejecutar = opciones[opcion_seleccionada]
          os.system("clear")
          input(opcion_ejecutar)
        else :
           os.system("clear")
           print("Ingrese una opcion valida")
           input("<<< Enter para continuar >>>")

        opcion_seleccionada = input(menu).lower()

    os.system("clear")


menu()


