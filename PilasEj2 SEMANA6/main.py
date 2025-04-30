from modulos import ordena



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


# Creamos la pila original
pila = []

# Agregamos los valores a la pila 
for num in valores:
    pila.append(num)

# Ordenamos la pila
resultado = ordena(pila)

# Mostramos el resultado final
print("Pila ordenada (de mayor a menor):", resultado)
