from menu import menu
from ingresar_menu import menu_ingresar_alumno, consultar_alumno


menu_home = """
    MENU 1

     a . ---------> ingresar alumno
     b . ---------> consultar alumno


     s . ---------> SALIR
"""

opciones_home = {
        'a' : menu_ingresar_alumno,
        'b' : consultar_alumno,

}

def mostrar_menu_home():
    menu(menu_home, opciones_home)
