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
pokemon = [7, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def burbuja(pokemon):
    n = len(pokemon)
    for i in range(n):
        for j in range(0, n-i-1):
            if pokemon[j] > pokemon[j+1]:
                pokemon[j], pokemon[j+1] = pokemon[j+1], pokemon[j]
    return pokemon
print(burbuja(pokemon))