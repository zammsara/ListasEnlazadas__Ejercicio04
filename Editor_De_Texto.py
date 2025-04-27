
# Editor de texto simple con funcionalidad de deshacer y rehacer
# Este programa permite al usuario escribir texto, deshacer y rehacer acciones, y mostrar el documento actual.
# El programa utiliza una lista enlazada para gestionar el historial de acciones.
# El usuario puede escribir texto, deshacer o rehacer acciones, y mostrar el documento actual.
class Nodo:
    def __init__(self, description):
        self.description = description
        self.prev = None
        self.next = None
class Historial:
    def __init__(self):
        self.current = None

    def crearNodo(self, description):
        # Crear y conectar un nuevo "Nodo"
        new_action = Nodo(description)
        # Si hay un nodo actual, conectar el nuevo nodo al anterior
        
        if self.current:
            self.current.next = new_action
            new_action.prev = self.current
        self.current = new_action

    def deshacer(self):
        # Moverse a prev
        #Si hay un nodo actual y un nodo anterior, moverse al anterior
        if self.current and self.current.prev: 
            print("Deshaciendo acción:", self.current.description)
            self.current = self.current.prev
        else:
            print("No hay más acciones para deshacer.")

    def rehacer(self):
        # Moverse a next
        #Si hay un nodo actual y un nodo siguiente, moverse al siguiente
        if self.current and self.current.next: 
            print("Rehaciendo acción:", self.current.description)
            self.current = self.current.next
        else:
            print("No hay más acciones para rehacer.")

    def mostrarHistorial(self):
        # Mostrar lista
        current = self.current
        while current:
            print(current.description)
            current = current.prev
        print("Fin del historial")
        
    def mostrar_Texto(self):
        if self.current:
            print("\n--- Documento Actual ---")
            contenido_limpio = self.current.description.replace(";", "\n")
            print(self.current.description)
            
            
            print("--------------------------\n")
        else:
            print("\nDocumento vacío.\n")
            
    def mostrar_Texto_Sin_Formato(self):
        if self.current:
            contenido_limpio = self.current.description.replace(";", "\n")
            print(self.current.description)
            
        else:
            print("\nDocumento vacío.\n")
            
# Programa principal
def contar_palabras(texto):
    palabras = texto.replace("\n", " ").split()
    return len(palabras)

def main():
    editorHistorial = Historial()
    editorHistorial.crearNodo("") #Acá creamos un nodo vacío
    
    lineas_maximas = 10 #Número máximo de líneas, si no se crea una nueva pagina 
    
    while True:
        print("=== Editor de Texto ===")
        print("1. Escribir Texto")
        print("2. Deshacer")
        print("3. Rehacer")
        print("4. Mostrar Documento")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))
        

        match opcion:
            case 1: 
                # Escribir texto
                
                print("\n--- Documento Actual ---")
                editorHistorial.mostrar_Texto_Sin_Formato()
                # Obtenemos el texto actual del documento
                texto_actual = editorHistorial.current.description
                
                # Pedimos al usuario que escriba nuevo texto
                nuevo_texto = input("Escribe el texto que quieres agregar: ") 
                
                # Procesar si hay punto y coma para hacer saltos de línea
                nuevo_texto = nuevo_texto.replace(";", "\n")
                if len(texto_actual) > 50:
                    #Se escribe en la siguente linea el nuevo texto
                    texto_actualizado = texto_actual + "\n" + nuevo_texto
                else:
                    texto_actualizado = texto_actual + " " + nuevo_texto   #Concatenamos el texto actual con el nuevo texto
                
                # Manejar límite de líneas
                lineas = texto_actualizado.split("\n")
                if len(lineas) > lineas_maximas:
                    texto_actualizado += "\n--- Nueva Página ---"
                    
                 # Mostrar el texto actualizado (sin punto y coma)
                print("\nTexto actualizado:")
                print(texto_actualizado.replace(";", ""))

                #Creamos un nuevo nodo con el texto actualizado
                editorHistorial.crearNodo(texto_actualizado)  
                print("--------------------------\n")
                
                # Mostrar contador de palabras
                cantidad_palabras = contar_palabras(texto_actualizado)
                print(f"\nNúmero de palabras actuales: {cantidad_palabras}")

                print("--------------------------\n")
                
            case 2:
                editorHistorial.deshacer()
                editorHistorial.mostrar_Texto()
            case 3:
                editorHistorial.rehacer()
                editorHistorial.mostrar_Texto()
            case 4:
                #editorHistorial.mostrarHistorial()
                editorHistorial.mostrar_Texto()
            case 5:
                print("Saliendo del editor de texto.")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
if __name__ == "__main__":
    main()