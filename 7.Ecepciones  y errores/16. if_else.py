## if / elif / else: decisiones
## Concepto: if pregunta una condicion; elif suma otras opciones; else cubre el resto.
## Utilidad: validar datos, clasificar valores y evitar errores antes de que ocurran.

## Ejercicio 1: clasificar un numero
numero = -3
if numero > 0:
    print("El numero es positivo.")
elif numero < 0:
    print("El numero es negativo.")
else:
    print("El numero es cero.")


## Ejercicio 2: validar una nota (0 a 5)
nota = 4.2
if nota < 0 or nota > 5:
    print("Error: la nota debe estar entre 0 y 5.")
elif nota >= 3.0:
    print("Aprobado. Nota:", nota)
else:
    print("Reprobado. Nota:", nota)


## Ejercicio 3: validar entrada antes de convertir (evita ValueError)
texto = "12a"
if texto.isdigit():
    valor = int(texto)
    if valor == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        print("10 /", valor, "=", round(10 / valor, 2))
else:
    print("Error: debes ingresar un numero entero valido.")
