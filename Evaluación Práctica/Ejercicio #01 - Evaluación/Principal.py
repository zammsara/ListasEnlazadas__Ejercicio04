from Ejercicio01 import separarParImpar
from colorama import Fore, init
init(autoreset=True)

# Ejemplo de uso
entrada = [2, 5, 6, 8, 11, 15, 14, 23]
salida = separarParImpar(entrada.copy())

print(Fore.YELLOW+"Entrada:", entrada)
print(Fore.GREEN+"Salida :", salida)