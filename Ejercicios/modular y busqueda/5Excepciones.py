## Las excepciones son errores que ocurren durante la ejecución de un programa.
## Son un mecanismo para manejar errores y continuar la ejecución del programa.


## ejercicio 1 
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")

## ejercicio 2 

try:
    # Intentar abrir un archivo
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:\n", contenido)

except FileNotFoundError:
    print("Error: El archivo no existe.")

except PermissionError:
    print("Error: No tienes permisos para abrir este archivo.")

finally:
    print("Operación finalizada.")