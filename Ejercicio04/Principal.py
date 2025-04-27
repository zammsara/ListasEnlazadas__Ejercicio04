# Programa principal
from Editor_De_Texto import Historial

from colorama import init, Fore, Style
init(autoreset=True)

def contar_palabras(texto):
    palabras = texto.replace("\n", " ").split()
    return len(palabras)

def main():
    editorHistorial = Historial()
    editorHistorial.crearNodo("") #Acá creamos un nodo vacío
    
    lineas_maximas = 10 #Número máximo de líneas, si no se crea una nueva pagina 
    
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
            print(Fore.RED+"Ingrese un número válido.\n")
            continue
        

        match opc:
            
            # Escribir texto
            case 1: 
            
                # Obtenemos el texto actual del documento
                texto_actual = editorHistorial.current.description

                # Pedimos al usuario que escriba nuevo texto
                nuevo_texto = input("Escribe el texto que quieres agregar: ") 

                # Procesar si hay punto y coma para hacer saltos de línea
                nuevo_texto = nuevo_texto.replace(";", "\n")

                # Concatenar el texto nuevo
                if len(texto_actual) > 50:
                    texto_actualizado = texto_actual + "\n" + nuevo_texto
                else:
                    texto_actualizado = texto_actual + " " + nuevo_texto


                # Separar líneas
                lineas = texto_actualizado.split("\n")

                if len(lineas) <= lineas_maximas:
                    # Si no supera el límite, crear un solo nodo
                    editorHistorial.crearNodo(texto_actualizado)
                else:
                    # Si supera el límite, dividir en páginas
                    pagina1 = "\n".join(lineas[:lineas_maximas])
                    pagina2 = "\n".join(lineas[lineas_maximas:])
                    
                    editorHistorial.crearNodo(pagina1)
                    editorHistorial.crearNodo("---------- Nueva Página ----------\n" + pagina2)

                # Mostrar el texto actualizado
                print(Fore.GREEN+"\nTexto actualizado:\n")
                editorHistorial.mostrar_Texto_Sin_Formato()

                # Mostrar contador de palabras
                cantidad_palabras = contar_palabras(texto_actualizado)
                print("\n---------------------------------------")
                print(f"Número de palabras actuales: {cantidad_palabras}")

                print("---------------------------------------\n")

            
            # Deshacer    
            case 2:
                editorHistorial.deshacer()
                editorHistorial.mostrar_Texto()
            
            # Rehacer   
            case 3:
                editorHistorial.rehacer()
                editorHistorial.mostrar_Texto()
            
            # Mostrar documento    
            case 4:
                #editorHistorial.mostrarHistorial()
                editorHistorial.mostrar_Texto()
            
            # Salir    
            case 5:
                print(Fore.CYAN+"\nSaliendo del editor de texto.")
                break
            
            case _:
                print(Fore.RED+"Opción no válida. Intenta de nuevo.")
if __name__ == "__main__":
    main()