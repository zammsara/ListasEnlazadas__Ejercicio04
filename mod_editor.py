from colorama import Fore
class Node: #Mi nodo (Lista Dobl.Enlazada)
    def __init__(self, valor): #Atributos del Nodo
        self.valor = valor
        self.next = None
        self.prev = None
        
        
class Record: #Basicamente mi lista Dobl.Enlazada
    def __init__(self): #Atributos 
        self.head = None
        self.tail = None
        self.redo_stack = [] #Pila para almacenar nodos deshechos (Pila: último elemento que se agrega es el primero en salir)
    
    
    #Agrega un nuevo nodo a la lista, al final.
    def add_action(self, valor):
        new_node = Node(valor)
        #En caso de que la lista esté vacía, el nuevo nodo se convierte en cabeza y cola.
        if not self.head: 
            self.head = self.tail = new_node
        #Sino, se agrega al final de la lista. 
        else: 
            self.tail.next = new_node #Conecta el nodo anterior con el nuevo nodo
            new_node.prev = self.tail
            self.tail = new_node #El nuevo nodo se convierte en la nueva cola de la lista.
        print(Fore.GREEN + "✔ Texto agregado correctamente.") 
        self.redo_stack.clear()  
    
    
    #Deshacer la última acción.
    def remove_action(self):
        if not self.head: #Verifica si la lista está vacía.
            print(Fore.RED + "✖ No hay acciones para deshacer.")
        #En caso de tener elementos... (Se elimina ultimo nodo de la lista)
        else:
            #Si la lista tiene un solo nodo, se elimina y se establece la cabeza y cola como None. Lo agrega a pila de redo
            if self.head == self.tail:
                self.redo_stack.append(self.tail) 
                self.head = self.tail = None
            #Sino, la cola se mueve al nodo anterior y se elimina el enlace al nodo actual. Y se agrega el nodo a la pila de redo.
            else:
                self.redo_stack.append(self.tail) 
                self.tail = self.tail.prev
                self.tail.next = None
            print(Fore.YELLOW + "↩ Acción deshecha.")  
    
    
    #Rehacer la última acción deshecha.
    def redo_action(self):
        if not self.redo_stack: #Verifica si la pila de redo está vacía.
            print(Fore.RED + "✖ No hay acciones para rehacer.")  
        #En caso de tener elementos... (Se elimina el último nodo de la pila de redo y se agrega a la lista)
        else:
            redo_node = self.redo_stack.pop() #Saca el último nodo de la pila de redo.
            #Si la lista está vacía, el nodo se convierte en cabeza y cola.
            if not self.head:
                self.head = self.tail = redo_node
            #Sino, se agrega al final de la lista.
            else:
                self.tail.next = redo_node #Conecta el nodo anterior con el nuevo nodo
                redo_node.prev = self.tail
                self.tail = redo_node #El nuevo nodo se convierte en la nueva cola de la lista.
            print(Fore.CYAN + "↪ Acción rehecha.") 
    

    # Imprime el contenido actual del editor basado en los valores de los nodos.
    def print_editor_content(self):
        if not self.head:  # Verifica si la lista está vacía.
            print(Fore.RED + "✖ El editor está vacío.")
        else:
            current = self.head  # Empieza desde la cabeza.
            content = ""  # Inicializa una cadena vacía para almacenar el contenido.
            while current:  # Recorre la lista hasta que no haya más nodos.
                content += current.valor  # Concatena el valor del nodo al contenido.
                current = current.next  # Avanza al siguiente nodo.
            
            print(Fore.BLUE + "*" * 30)  # Imprime una línea divisoria en azul
            print(Fore.BLUE + "CONTENIDO:")  # Mensaje en azul
            print(Fore.BLUE + "-" * 30)  # Imprime una línea divisoria en azul
            print(Fore.WHITE + content)  # Contenido en blanco
            print("\n\n"+Fore.BLUE + "*" * 30)  # Imprime una línea divisoria en azul   
      
            

        
        
    