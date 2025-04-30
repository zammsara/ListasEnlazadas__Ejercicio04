# Programa de "Pila de enteros"
# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# Versión 1.1
# 30.abril.2025

# Descripción: 
# Se implementará un método que reciba una pila de enteros como único parámetro.
# este método llamado "separarParImpar" deberá retornar una pila con números pares
# en la parte superior y los impares en la inferior.

# Descripción:
# Se implementará una clase llamada Pila para simular el comportamiento de una pila de enteros.
# Luego, se implementará un método llamado "separarParImpar" que recibe una pila como parámetro
# y retorna una nueva pila con los números pares en la parte superior y los impares en la inferior.

class Pila:
    def __init__(self):
        # Lista interna que almacenará los elementos de la pila
        self.elementos = []

    def push(self, elemento):
        # Agrega un elemento a la cima de la pila
        self.elementos.append(elemento)

    def pop(self):
        # Extrae y retorna el último elemento (LIFO)
        return self.elementos.pop()

    def esta_vacia(self):
        # Retorna True si la pila está vacía, False en caso contrario
        return len(self.elementos) == 0

    def __str__(self):
        # Representación en forma de lista para impresión
        return str(self.elementos)


def separarParImpar(pila_original):
    #creamos dos pilas auxiliares: una para pares y otra para impares
    pares = Pila()
    impares = Pila()

    #mientras haya elementos en la pila original, los extraemos uno a uno
    while not pila_original.esta_vacia():
        #extraemos el número de la cima de la pila
        numero = pila_original.pop()

        #si el número es par, lo agregamos a la pila de pares
        if numero % 2 == 0:
            pares.push(numero)
        #si el número es impar, lo agregamos a la pila de impares
        else:
            impares.push(numero)

    #creamos la pila resultado donde se unirán los pares primero, luego los impares
    resultado = Pila()

    # Primero agregamos los números pares a la pila resultado
    while not pares.esta_vacia():
        resultado.push(pares.pop())

    #luego agregamos los números impares a la pila resultado
    while not impares.esta_vacia():
        resultado.push(impares.pop())

    #retornamos la pila reconstruida con los pares en la cima y los impares debajo
    return resultado
