import os

def menu(menu, opciones):

    opcion_seleccionada = input(menu).lower()
    os.system("clear")
    while opcion_seleccionada != "s":
        if opcion_seleccionada in opciones:
          opcion_ejecutar = opciones[opcion_seleccionada]
          opcion_ejecutar()
          
        else :
           os.system("clear")
           print("Ingrese una opcion valida")
           input("<<< Enter para continuar >>>")

        opcion_seleccionada = input(menu).lower()

    os.system("clear")