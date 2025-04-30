

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, valor):
        self.elementos.append(valor)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ordenar(self):
        return sorted(self.elementos, reverse=True)

    def mostrar(self):
        return self.elementos