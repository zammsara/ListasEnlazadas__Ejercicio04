from Pila import Pila, separarParImpar
from colorama import Fore, init, Style
init(autoreset=True)

#Se le solicita al usuario que ingrese números separados por comas
entrada_usuario = input(Style.BRIGHT+"Ingresa números enteros separados por comas (ej. 2,5,6,8): ")

#Convertimos la cadena en una lista de enteros, ignorando espacios en blanco
numeros = [int(n.strip()) for n in entrada_usuario.split(",") if n.strip().isdigit()]

#Creamos una pila y agregamos los números ingresados
entrada = Pila()
for numero in numeros:
    entrada.push(numero)

#Llamamos a la función que separa pares e impares
salida = separarParImpar(entrada)

print(Fore.YELLOW + "Entrada:", numeros)
print(Fore.GREEN + "Salida :", salida)

