# Ejemplificación de operaciones básicas en pila utilizando lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato #dato del nodo
        self.siguiente = None #puntero al siguiente nodo

class Pila: 
    def __init__(self):
        self.tope = None # Inicia vacía
    
    # Agregar un elemento
    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope #el nuevo apunta al anterior tope
        self.tope = nuevo_nodo #el nuevo ahora es el tope
        
    # Eliminar y retornar el último elemento insertado
    def pop(self):
        if self.tope is None:
            print("Error: pila vacía. No se puede eliminar.")
            return None
        eliminado = self.tope.dato
        self.tope = self.tope.siguiente #avanza el tope al siguiente nodo
        return eliminado
    
    def separarParImpar(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        
        pila_par = Pila()
        pila_impar = Pila()
        
        # Separar los elementos en dos pilas
        while self.tope is not None:
            elemento = self.pop()
            if elemento % 2 == 0:
                pila_par.push(elemento)
            else:
                pila_impar.push(elemento)
        
        # Reconstruir la pila original con los pares en la parte inferior y los impares en la parte superior
        while pila_par.tope is not None:
            self.push(pila_par.pop())
        
        while pila_impar.tope is not None:
            self.push(pila_impar.pop())
    # Método para imprimir los datos de la pila
    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        else:
            # Reorganizar la pila antes de imprimir
            self.separarParImpar()
            print("Contenido de la pila (pares abajo, impares arriba):")
            actual = self.tope  # Empieza desde el nodo superior
            while actual is not None:  # Recorre todos los nodos
                print(actual.dato)
                actual = actual.siguiente  # Avanza al siguiente nodo
            print("None")