# los arreglos bidimensionales son los que tienen dos indices #
#Sirven para representar matrices y tablas #

# Mostrar una matriz #

matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# Sumar los elementos de la matriz #

suma=0
for fila in matriz:
    for elemento in fila:
        suma+=elemento
print(f"La suma de los elementos de la matriz es: {suma}")

# Encontrar el maximo y minimo de la matriz #

maximo=max(matriz)