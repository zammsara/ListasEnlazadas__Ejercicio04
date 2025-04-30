from modulos import Pila



# Bucle principal del programa
while True:
    # Entrada del usuario
    entrada = input("Ingrese los números separados por espacios: ")

    valores = []  # Lista para los números convertidos
    numero = ""   # Acumulador de caracteres

    # Recorremos cada carácter de la cadena
    for caracter in entrada:
        if caracter != " ":
            numero += caracter  # Acumulamos el dígito
        else:
            if numero != "":
                valores.append(int(numero))  # Convertimos y guardamos
                numero = ""  # Reiniciamos para el siguiente número

    # Agregamos el último número si no hay espacio al final
    if numero != "":
        valores.append(int(numero))

    # Crear pila e insertar valores
    mi_pila = Pila()
    for num in valores:
        mi_pila.push(num)

    # Ordenar la pila
    pila_ordenada = mi_pila.ordenar()

    # Mostrar resultado
    print("Pila ordenada (de mayor a menor):", pila_ordenada)

    # Preguntar al usuario si desea continuar
    continuar = input("¿Desea ingresar otra lista de números? (s/n): ").lower()
    if continuar != "s":
        print("Programa finalizado.")
        break