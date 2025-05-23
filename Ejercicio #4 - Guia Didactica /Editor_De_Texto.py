# Programa de "Editor de texto"
# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# Versión 1.2
# 27.abril.2025

#Descripción del programa: 
# Editor de texto simple con funcionalidad de deshacer y rehacer
# Este programa permite al usuario escribir texto, deshacer y rehacer acciones, y mostrar el documento actual.
# El programa utiliza una lista enlazada para gestionar el historial de acciones.
# El usuario puede escribir texto, deshacer o rehacer acciones, y mostrar el documento actual.

from colorama import Fore, Back, Style
#

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
            print(Fore.GREEN+"\nDeshaciendo acción:", self.current.description)
            self.current = self.current.prev
        else:
            print(Fore.YELLOW+"\nNo hay más acciones para deshacer.")

    def rehacer(self):
        # Moverse a next
        #Si hay un nodo actual y un nodo siguiente, moverse al siguiente
        if self.current and self.current.next: 
            print(Fore.GREEN+"\nRehaciendo acción:", self.current.description)
            self.current = self.current.next
        else:
            print(Fore.YELLOW+"No hay más acciones para rehacer.")

    def mostrarHistorial(self):
        # Mostrar lista
        current = self.current
        while current:
            print(current.description)
            current = current.prev
        print(Style.BRIGHT+"Fin del historial")
        
    def mostrar_Texto(self):
        if self.current:
            print("\n--- Documento Actual ---")
            contenido_limpio = self.current.description.replace(";", "\n")
            print(self.current.description)
            print("--------------------------\n")
        else:
            print(Fore.YELLOW+"\nDocumento vacío.\n")
            return
        # Si no hay nodos (el historial está vacío), mostrar mensaje
        

            
    def mostrar_Texto_Sin_Formato(self):
        if self.current:
            contenido_limpio = self.current.description.replace(";", "\n")
            print(self.current.description)
            
        else:
            print(Fore.LIGHTRED_EX+"\nDocumento vacío.\n")



    
    