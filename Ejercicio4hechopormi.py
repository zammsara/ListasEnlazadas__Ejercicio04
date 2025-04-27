#Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
#(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
#en ambas direcciones, simulando las acciones de Deshacer y Rehacer
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #referencia
        self.anterior = None  # refrerencia 
        self.deshecho = False  # Atributo para marcar si el nodo ha sido deshecho

class Historial:
    def __init__(self):
        self.cabeza = None #nodo primero
        self.cola = None #ultimo nodo
        self.actual = None #nodo actual

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.actual = self.cola

    def deshacer(self):
        if self.actual and self.actual.anterior:
            print(f"El dato a deshacer es: {self.actual.dato}")
            self.actual.deshecho = True  # Marcar el nodo actual como deshecho
            self.actual = self.actual.anterior
        else:
            print("No hay más acciones por hacer")

    def rehacer(self):
        if self.actual and self.actual.siguiente:
            if self.actual.siguiente.deshecho:  # Si el siguiente nodo está deshecho
                print(f"El dato a rehacer es: {self.actual.siguiente.dato}")
                self.actual.siguiente.deshecho = False  # Reactivar el nodo
                self.actual = self.actual.siguiente  # Mover al siguiente nodo
            else:
                print("No se puede rehacer este nodo porque no está marcado como deshecho.")
        else:
            print("No hay un nodo que se pueda rehacer")

    def imprimirdatos(self):
        actual = self.cabeza
        if actual is None:
            print("No hay datos que mostrar")
        else:
            print("Historial de acciones (sin deshacer):")
            while actual:
                if not actual.deshecho:  # Solo imprimir nodos que no han sido deshechos
                    print(f"- {actual.dato}")
                actual = actual.siguiente


def menu():
    historial = Historial()

    while True:
        print("\n--- Editor de Texto ---")
        print("1. Agregar acción")
        print("2. Deshacer")
        print("3. Rehacer")
        print("4. Mostrar acción actual")
        print("5. Mostrar datos")
        print("6. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            accion = input("Escribe: ")
            historial.agregar(accion)
            print("Acción agregada.")
        elif opcion == 2:
            historial.deshacer()
        elif opcion == 3:
            historial.rehacer()
        elif opcion == 4:
            if historial.actual:
                print(f"Acción actual: {historial.actual.dato}")
            else:
                print("No hay acciones realizadas aún.")
        elif opcion == 5:
            historial.imprimirdatos()
        elif opcion == 6:
            print("Saliendo del editor...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
