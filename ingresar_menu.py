from menu import menu

def menu_ingresar_alumno():


    menu_ingresar = """
        MENU ingresar alumno

         a . ---------> nombre
         b . ---------> telefono

         s . ---------> VOLVER
    """

    opciones_ingresarios = {
            'a' : 'ingresa nombre',
            'b' : 'ingresa telefono',
    }

    menu(menu_ingresar, opciones_ingresarios)

def consultar_alumno():
    input('Nombre del alumno a consultar')