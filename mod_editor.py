class Node:
    def __init__(self, valor, type): #Atributos del Nodo
        self.valor = valor
        self.next = None
        self.prev = None
        self.type = type
        
class Record:
    def __init__(self): #Atributos de la lista, Cabeza, cola y cursor
        self.head = None
        self.tail = None
        self.cursor = None
        
    def add_action(self, valor, tipo):
        new_node = Node(valor, tipo)
        if not self.head: #Si la lista está vacía
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node #Asume que es de tipo Node
            new_node.prev = self.tail
            self.tail = new_node
        self.cursor = new_node
            

        
        
    