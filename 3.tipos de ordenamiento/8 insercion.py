# insercion
# se toma el primer elemento y se compara con el siguiente, si es mayor se intercambia, si es menor se deja en su lugar 
# se repite el proceso con el siguiente elemento, hasta que se ordene la lista
# se puede usar un array o una lista enlazada

# elemplo con uma lista 

def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

lista = [5, 3, 8, 4, 2]
print(insercion(lista))

