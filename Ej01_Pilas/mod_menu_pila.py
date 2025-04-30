import os
from colorama import Fore, Style, init

def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')
        
def menu():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n=== Menú ===")  # Azul claro y brillante
    print("1. Agregar elemento a la pila")
    print("2. Imprimir pila")
    print("3. Salir")
    print(Fore.LIGHTBLACK_EX + Style.DIM + "====================")  # Gris y tenue

# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def pausa():
    print(Fore.LIGHTBLACK_EX + Style.DIM + "Presione Enter para continuar...")  # Gris y tenue
    input()