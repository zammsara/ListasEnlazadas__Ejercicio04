# Programa de "Pila de enteros"
# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# Versión 1
# 30.abril.2025

# Descripción: 
# Se implementará un método que reciba una pila de enteros como único parámetro.
# este método llamado "separarParImpar" deberá retornar una pila con números pares
# en la parte superior y los impares en la inferior.

def separarParImpar(pila):
    pares = []
    impares = []

    #mientras haya elementos en la pila original, los extraemos uno a uno
    while pila:
        #extraemos el último número de la pila (eliminando el último elemento)
        numero = pila.pop()
        
        #si el número es par, lo agregamos a la lista de pares
        if numero % 2 == 0:
            pares.append(numero)
        #si el número es impar, lo agregamos a la lista de impares
        else:
            impares.append(numero)

    # Reconstruimos la pila con pares primero, luego impares
    # Como las pilas funcionan tipo LIFO (Last In First Out), y usamos append/pop,
    # invertimos las listas al unirlas
    resultado = []

    # Primero agregamos los números pares al resultados
    while pares:
        # Extraemos el último número de la lista de pares (recuerda que el orden se invierte al usar pop)
        resultado.append(pares.pop())

    # Luego agregamos los números impares al resultado
    while impares:
        # Extraemos el último número de la lista de impares y lo agregamos al resultado
        resultado.append(impares.pop())

    # Finalmente, retornamos la lista reconstruida con los números pares primero y los impares después
    return resultado