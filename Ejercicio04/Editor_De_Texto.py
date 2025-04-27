# Programa de "Editor de texto"
# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# Versión 1.2
# 27.abril.2025

#Descripción del programa: 
# Editor de texto simple con funcionalidad de deshacer y rehacer
# Este programa permite al usuario escribir texto, deshacer y rehacer acciones, y mostrar el documento actual.
# El programa utiliza una lista enlazada para gestionar el historial de acciones.
# El usuario puede escribir texto, deshacer o rehacer acciones, y mostrar el documento actual.

from colorama import init, Fore, Style
init(autoreset=True)

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
        if self.current:
            self.current.next = new_action
            new_action.prev = self.current
        self.current = new_action

    def deshacer(self):
        if self.current and self.current.prev:
            print(Fore.GREEN + "\nDeshaciendo acción:", self.current.description)
            self.current = self.current.prev
        else:
            print(Fore.YELLOW + "\nNo hay más acciones para deshacer.")

    def rehacer(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(Fore.GREEN + "\nRehaciendo acción:", self.current.description)
        else:
            print(Fore.YELLOW + "No hay más acciones para rehacer.")

    def mostrarHistorial(self):
        current = self.current
        while current:
            print(current.description)
            current = current.prev
        print(Style.BRIGHT + "Fin del historial")

    def mostrar_Texto(self):
        if not self.current:
            print(Fore.YELLOW + "\nDocumento vacío.\n")
            return
        print("\n--- Documento Actual ---")
        contenido_limpio = self.current.description.replace(";", "\n")
        print(contenido_limpio)
        print("--------------------------\n")

    def mostrar_Texto_Sin_Formato(self):
        if self.current:
            print(self.current.description)
        else:
            print(Fore.YELLOW + "\nDocumento vacío.\n")
