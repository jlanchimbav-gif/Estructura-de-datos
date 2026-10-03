# calculo de la suma de los elementos #

numeros=[1, 2, 3, 4, 5]
suma=0
for numero in numeros:
    suma+=numero
print(f"La suma de los elementos es: {suma}")

# calculo de la media de los elementos #

media=suma/len(numeros)
print(f"La media de los elementos es: {media}")

# carga de datos# 

## ejercicio 2 

# Crear un arreglo unidimensional (lista)
numeros = [10, 20, 30, 40, 50]

# Acceder a elementos
print("Primer elemento:", numeros[0])   # 10
print("Último elemento:", numeros[-1])  # 50

# Recorrer el arreglo
for n in numeros:
    print("Valor:", n)

# Modificar un elemento
numeros[2] = 99
print("Arreglo modificado:", numeros)