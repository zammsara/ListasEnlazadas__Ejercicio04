

class Pila:
    def __init__(self):
        self.elementos = []  # Lista interna para almacenar los elementos

    def push(self, valor):
        self.elementos.append(valor)  # Agrega un valor a la pila (tope)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()  # Elimina y devuelve el tope de la pila

    def esta_vacia(self):
        return len(self.elementos) == 0  # Verifica si la pila está vacía

    def mostrar(self):
        return self.elementos.copy()  # Devuelve una copia de la pila

    def ordenar(self):
         # Usamos una lista temporal para sacar todos los elementos
        lista_temp = []

        # Sacamos todos los elementos de la pila y los guardamos en lista_temp
        while not self.esta_vacia():
            lista_temp.append(self.pop())

        # Ordenamos la lista de mayor a menor usando sort
        lista_temp.sort(reverse=True)

        # Creamos una nueva pila ordenada
        pila_ordenada = Pila()
        for num in lista_temp:
            pila_ordenada.push(num)

        return pila_ordenada  # Retornamos la pila ordenada