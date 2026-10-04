## el ordenamiento por selección es un algoritmo de ordenamiento que selecciona el elemento más pequeño de la lista 
# y lo coloca en la primera posición, luego el segundo más pequeño y lo coloca en la segunda posición, y así sucesivamente #
# es un algoritmo de ordenamiento inestable, es decir, que no mantiene el orden de los elementos iguales #
# es un algoritmo de ordenamiento in situ, es decir, que no requiere espacio adicional #


def ordenamiento_por_seleccion(lista):
    for i in range(len(lista)):
        
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista_desordenada = [64, 25, 12, 22, 11]
print("Lista desordenada:", lista_desordenada)
lista_ordenada = ordenamiento_por_seleccion(lista_desordenada)
print("Lista ordenada:", lista_ordenada)


                
