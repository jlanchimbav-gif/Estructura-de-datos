## la busqueda binaria es un algoritmo de busqueda que se utiliza para encontrar un elemento en un arreglo ordenado##
## sirve para verificar que la funcion no se rompe cuando se le pasa un valor muy grande##
## ejemplo: busqueda_binaria(1000000)

def busqueda_binaria(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(busqueda_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

# Ejemplo 2: factorial
## factorial(1000000)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(1000000))

## Ejemplo 3: fibonacci
## fibonacci(1000000)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(1000000))