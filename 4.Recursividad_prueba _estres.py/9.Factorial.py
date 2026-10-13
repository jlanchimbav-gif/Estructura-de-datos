# La recursividad es una funcion que se llama a si misma.
# Sirve para resolver problemas que se pueden dividir en problemas mas pequeños.
# Ejemplo: factorial de 5 = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Ejemplo 2: Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# fibonacci(0) = 0
# fibonacci(1) = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)