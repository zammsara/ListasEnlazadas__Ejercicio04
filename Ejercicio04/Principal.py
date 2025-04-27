# main.py
from Editor_De_Texto import Historial
from colorama import init, Fore, Style
init(autoreset=True)

def contar_palabras(texto):
    palabras = texto.replace("\n", " ").split()
    return len(palabras)

def main():
    editorHistorial = Historial()
    editorHistorial.crearNodo("")  # Nodo vacío inicial
    
    lineas_maximas = 10  # Límite de líneas por página

    while True:
        print('=' * 35)
        print("Editor de texto")
        print('=' * 35)
        print("1. Escribir Texto")
        print("2. Deshacer")
        print("3. Rehacer")
        print("4. Mostrar Documento")
        print("5. Salir")
        print('=' * 35)

        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print(Fore.RED + "Ingrese un número válido.\n")
            continue

        match opc:
            case 1:
                # Mostrar documento actual
                print("\n--- Documento Actual ---")
                editorHistorial.mostrar_Texto_Sin_Formato()

                texto_actual = editorHistorial.current.description
                nuevo_texto = input("Escribe el texto que quieres agregar: ")
                nuevo_texto = nuevo_texto.replace(";", "\n")

                if len(texto_actual) > 50:
                    texto_actualizado = texto_actual + "\n" + nuevo_texto
                else:
                    texto_actualizado = texto_actual + " " + nuevo_texto

                lineas = texto_actualizado.split("\n")
                if len(lineas) > lineas_maximas:
                    texto_actualizado += "\n--- Nueva Página ---"

                print(Fore.GREEN + "\nTexto actualizado:")
                print(texto_actualizado.replace(";", ""))

                editorHistorial.crearNodo(texto_actualizado)
                print("--------------------------\n")

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
                editorHistorial.mostrar_Texto()

            case 5:
                print(Fore.CYAN + "\nSaliendo del editor de texto.")
                break

            case _:
                print(Fore.RED + "Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
