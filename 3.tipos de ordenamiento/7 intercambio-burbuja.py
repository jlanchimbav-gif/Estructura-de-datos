## el ordenamiento por intercambio o burbuja es un algoritmo de ordenamiento que compara cada elemento de la lista con el siguiente
# y si el elemento actual es mayor que el siguiente, se intercambian los elementos #
# es un algoritmo de ordenamiento inestable, es decir, que no mantiene el orden de los elementos iguales #

# ordenar los numeros de una lista ##

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [5, 3, 8, 4, 2]
print(burbuja(lista))

## Ejercicio 2 ##
# Lista desordenada de numeros (por ejemplo, IDs de pokemon)
pokemon = [7, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def burbuja(pokemon):
    # n guarda cuantos elementos hay; se usa para saber hasta donde recorremos
    n = len(pokemon)

    # i = pasada actual. En cada pasada el mayor de los pendientes "sube" al final
    for i in range(n):

        # j recorre los pares vecinos. n-i-1 evita revisar lo que ya quedo ordenado al final
        for j in range(0, n - i - 1):

            # Si el de la izquierda es mayor que el de la derecha, estan en mal orden
            if pokemon[j] > pokemon[j + 1]:

                # Intercambio (swap): el mayor avanza una posicion hacia la derecha
                pokemon[j], pokemon[j + 1] = pokemon[j + 1], pokemon[j]

    # Al terminar todas las pasadas, la lista queda de menor a mayor
    return pokemon

print(burbuja(pokemon))