import mod_menu as menu
from mod_editor import Record 

opcion = 0 #Variable para almacenar la opción ingresada por el usuario.

editor = Record()

while opcion != 5: #Mientras la opción no sea 5(salir del programa), siga corriendo.
    
    menu.mostrar_menu() #Muestra el menú de opciones al usuario.
    ##Se asegura de que la opción ingresada sea un número entero.
    try:
        opcion = int(input("Respuesta: "))
    except ValueError:
        print("Opción inválida, por favor escriba un número.")
        continue
    
    #Evalua la opción ingresada por el usuario.
    match opcion: 
        case 1: #Agregar texto
            texto = input("Ingrese el texto a agregar: ")
            editor.add_action(texto) #Llama a la función para agregar texto al editor.
            print("Texto agregado.")
            editor.print_editor_content()
            
        case 2: #Deshacer
            editor.remove_action() #Llama a la función para deshacer la última acción.
            print("Acción deshecha.")
            editor.print_editor_content()
            
        case 3: #Rehacer
            editor.redo_action() #Llama a la función para rehacer la última acción deshecha.
            print("Acción rehecha.")
            editor.print_editor_content()
            
        case 4: #Ver contenido
            editor.print_editor_content() #Llama a la función para imprimir el contenido del editor.
            
        case 5: #Salir
            print("Saliendo del programa...")
            
        case _: #En caso de que la opción no sea válida, se muestra un mensaje de error.
            print("Opción inválida o inexistente, por favor intente nuevamente.")


    