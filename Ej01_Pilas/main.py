# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# SEPARAR IMPARES || Versión 1.0
# 27.abril.2025

#Descripción del programa: 
"""
Implementa un método que reciba una pila de enteros como único parámetro. Este método llamado “separarParImpar” deberá retornar la pila con los números pares en la parte inferior y los impares en la superior.
"""

from mod_Pila import Pila
import mod_menu_pila as menu
from colorama import Fore, Style, init

pila = Pila()

opcion = 0

while opcion != 3:
    menu.limpiar_consola()  # Limpia la consola antes de mostrar el menú
    menu.menu()
    #Valida si el usuario ingresó un número entero.
    try:
        opcion = int(input("Respuesta: "))
        print("\n")
    except ValueError:
        print(Fore.RED+"Opción no válida. Intenta de nuevo.")
        menu.pausa() 
        continue

    match opcion:
        case 1:  # Agregar elemento a la pila
            #Valida si el usuario ingresó un número entero.
            try:
                elemento = int(input("Ingrese un número entero: "))
                print("\n")
            except ValueError:
                print(Fore.RED+"Respuesta tiene que ser un numero. Intenta de nuevo.")
                menu.pausa() 
                continue
            
            pila.push(elemento)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Elemento agregado a la pila.")  # Verde brillante
            menu.pausa()

        case 2:  # Imprimir pila
            menu.limpiar_consola()  # Limpia la consola antes de mostrar el contenido de la pila
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Contenido de la pila:")  # Azul claro y brillante
            pila.imprimir()
            menu.pausa()

        case 3:  # Salir
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "Saliendo del programa...")  # Rojo brillante
            print(Fore.CYAN+"Gracias por usar el programa. ¡Hasta luego! 👋")

        case _:  # Opción no válida
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")
            menu.pausa()
    
