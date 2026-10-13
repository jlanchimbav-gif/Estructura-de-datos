# ejercicios de recursividad
## Ejercicio 1: contar elementos de una lista##
## ejemplo: contar_elementos([1, 2, 3, 4, 5])
def contar_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])
print(contar_elementos([1, 2, 3, 4, 5]))

## Ejercicio 2: sumar elementos de una lista##
## ejemplo: sumar_elementos([1, 2, 3, 4, 5])
def sumar_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar_elementos(lista[1:])
print(sumar_elementos([1, 2, 3, 4, 5]))

## Ejercicio 3: encontrar el maximo elemento de una lista##
## ejemplo: encontrar_maximo([1, 2, 3, 4, 5])
def encontrar_maximo(lista):
    if len(lista) == 0:
        return 0
    else:
        return max(lista[0], encontrar_maximo(lista[1:]))
print(encontrar_maximo([1, 2, 3, 4, 5]))

## Ejercicio 4: encontrar el minimo elemento de una lista##
## ejemplo: encontrar_minimo([1, 2, 3, 4, 5])
def encontrar_minimo(lista):
    if len(lista) == 0:
        return 0
    else:
        return min(lista[0], encontrar_minimo(lista[1:]))
print(encontrar_minimo([1, 2, 3, 4, 5]))

## Ejercicio 5: encontrar el promedio de una lista##
## ejemplo: encontrar_promedio([1, 2, 3, 4, 5])
def encontrar_promedio(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)
print(encontrar_promedio([1, 2, 3, 4, 5]))

## Ejercicio 6: encontrar el numero de elementos de una lista##
## ejemplo: encontrar_numero_elementos([1, 2, 3, 4, 5])
def encontrar_numero_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + encontrar_numero_elementos(lista[1:])
print(encontrar_numero_elementos([1, 2, 3, 4, 5]))

## Ejercicio 7: encontrar el numero de elementos de una lista##
## ejemplo: encontrar_numero_elementos([1, 2, 3, 4, 5])
def encontrar_numero_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + encontrar_numero_elementos(lista[1:])
print(encontrar_numero_elementos([1, 2, 3, 4, 5]))

## Ejercicio 8: encontrar si una cadena es palindroma##
## ejemplo: es_palindroma("radar")
def es_palindroma(cadena):
    if len(cadena) <= 1:
        return True
    else:
        return cadena[0] == cadena[-1] and es_palindroma(cadena[1:-1])
print(es_palindroma("radar"))

