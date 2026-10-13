## las pruebas de estres son para verificar que la funcion funciona correctamente##
## sirve para verificar que la funcion no se rompe cuando se le pasa un valor muy grande##
## ejemplo: suma(1000000)

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
print(suma(1000000))

## Ejemplo 2: factorial
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