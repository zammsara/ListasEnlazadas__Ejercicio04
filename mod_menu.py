import os
from colorama import Fore, Style, init

def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')

def mostrar_menu():
    limpiar_consola()  # Limpia la consola antes de mostrar el menú
    print("\n=== Menú ===")
    print("1. Agregar texto")
    print("2. Deshacer")
    print("3. Rehacer")
    print("4. Ver contenido")
    print("5. Salir")



# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def pausa():
    print(Fore.LIGHTBLACK_EX + Style.DIM + "Presione Enter para continuar...")  # Gris y tenue
    input()