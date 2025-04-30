
class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad # Inicializa la pila con una capacidad fija 
        self.tope = -1 # Índice del último elemento agregado

    
    def push(self, elemento):  # Agrega un elemento a la cima de la pila si hay espacio
        if self.tope < self.capacidad - 1:
            self.tope += 1
            self.elementos[self.tope] = elemento
        else:
            print("Error: Pila llena. No se puede insertar.")

    def is_empty(self): # Verifica si la pila está vacía
        return self.tope == -1
    def pop(self):
        if self.is_empty():
            print("Error: Pila vacía. No se puede eliminar.")
            return None
        eliminado = self.elementos[self.tope]
        self.elementos[self.tope] = None
        self.tope -= 1
        return eliminado
    
class BinarioPila:
    def __init__(self, capacidad=32):
        # Crea una instancia de la clase Pila con capacidad definida
        self.pila = Pila(capacidad)

    def convertir(self, numero):
        # Convierte un número entero a binario utilizando la pila

        if numero == 0:
            # Caso especial para cero
            return "[0]"

        # Reinicia la pila en caso de reutilización del objeto
        self.pila = Pila(self.pila.capacidad)

        # Paso 1: Convertir el número a binario, guardando los residuos en la pila
        while numero > 0:
            residuo = numero % 2
            self.pila.push(residuo)  # Apilamos el residuo (0 o 1)
            numero //= 2  # División entera por 2

        # Paso 2: Extraer los elementos en orden inverso (de la pila)
        binario = ""
        while not self.pila.is_empty():
            binario += str(self.pila.pop())  # Concatenamos los bits en orden correcto

        return f"[{binario}]"  # Devuelve el binario entre corchetes
   
