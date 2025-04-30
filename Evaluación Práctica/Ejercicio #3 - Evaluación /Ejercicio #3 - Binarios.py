#3. Diseñar un método “Convbinario” que reciba un entero como parámetro.
#La función, usando una pila, deberá mostrar el número en código binario.
from PilaBinaria import BinarioPila
import os 
def limpiarPantalla(): 
    os.system("clear")
    os.system("cls")
def main(): 
    
    
    #Menu 
    while True:
        limpiarPantalla() 
        print("======        Ejercicio 3       ======")
        print("=== Conversor de Decimal a Binario ===")
        print("1. Convertir un número entero a binario")
        print("2. Salir")  
        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.\n")
            continue
        
        match opc:
            case 1: 
                 # Crear una instancia de la clase BinarioPila
                binario_pila = BinarioPila()

                # Solicitar al usuario un número entero
                numero = int(input("Ingrese un número entero: "))

                # Convertir el número a binario y mostrar el resultado
                resultado = binario_pila.convertir(numero)
                print(f"El número {numero} en binario es: {resultado}")
                input("Presione Enter para continuar...")
            case 2:
                print("Saliendo del programa...")
                return
            case _:
                print("Opción no válida. Intente nuevamente.\n")
   
if __name__ == "__main__":
    main()
