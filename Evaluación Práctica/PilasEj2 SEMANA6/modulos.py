

def ordena(pila): # se proporciona el parametro pila
    lista_temp = [] # se crea una lista temporal donde se alamcenaran los valores ingresados por el ususario
    while pila:
        lista_temp.append(pila.pop()) # Sacamos con (pop) los elementos de la pila del ultimo al primero y los agregamos a la lista temporal

    lista_temp.sort(reverse=True) # esto se utiliza para ordenar la pila

    pila_ordenada = [] # se crea una lista la cual almacenara ya los valores ordenalos de la pila
    for num in lista_temp:
        pila_ordenada.append(num) # se agregan los eleementos ordenados a la nueva pila

    return pila_ordenada # retorna la pila ya ordenada de mayor a menor