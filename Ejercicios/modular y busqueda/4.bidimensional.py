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

##ejercicio 2 
# Crear un arreglo bidimensional (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos
print("Elemento en fila 0, columna 1:", matriz[0][1])  # 2
print("Elemento en fila 2, columna 0:", matriz[2][0])  # 7

# Recorrer filas y columnas
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # salto de línea

# Modificar un elemento
matriz[1][2] = 99
print("Matriz modificada:", matriz)
