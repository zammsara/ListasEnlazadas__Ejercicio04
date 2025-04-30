# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# EDITOR DE TEXTO || Versión 1.0
# 27.abril.2025

#Descripción del programa: 
# Editor de texto simple con funcionalidad de deshacer y rehacer
# Este programa permite al usuario escribir texto, deshacer y rehacer acciones, y mostrar el documento actual.
# El programa utiliza una lista enlazada para gestionar el historial de acciones.
# El usuario puede escribir texto, deshacer o rehacer acciones, y mostrar el documento actual.

import mod_menu as menu
from mod_editor import Record 
from colorama import Fore

opcion = 0 

editor = Record()

while opcion != 5: #Mientras la opción no sea 5(salir del programa), siga corriendo.
    
    menu.mostrar_menu() #Menú de opciones al usuario.
    #Se asegura de que la opción ingresada sea un número entero.
    try:
        opcion = int(input("Respuesta: "))
        print("\n")
    except ValueError:
        print(Fore.RED+"Opción no válida. Intenta de nuevo.")
        menu.pausa() 
        continue
    
    #Evalua la opción ingresada por el usuario.
    match opcion: 
        case 1: #Llama a la función para agregar texto al editor.
            texto = input("Ingrese el texto a agregar: ")
            editor.add_action(texto) 
            editor.print_editor_content()
            menu.pausa()
            
        case 2: #Llama a la función para deshacer la última acción.
            editor.remove_action() 
            editor.print_editor_content()
            menu.pausa()
            
        case 3: #Llama a la función para rehacer la última acción deshecha.
            editor.redo_action()
            editor.print_editor_content()
            menu.pausa()
            
        case 4: #Ver contenido
            menu.limpiar_consola()
            editor.print_editor_content() 
            menu.pausa()
            
        case 5: #Salir
            print(Fore.CYAN+"\nSaliendo del editor de texto.")
            print(Fore.CYAN+"Gracias por usar el programa. ¡Hasta luego! 👋")
            
        case _: #En caso de que la opción no sea válida, se muestra un mensaje de error.
            print(Fore.RED+"Opción no válida. Intenta de nuevo.")
            menu.pausa()
            continue


    