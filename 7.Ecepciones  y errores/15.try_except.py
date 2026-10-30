## try / except: control de errores
## Concepto: try intenta ejecutar un codigo; si falla, except lo atrapa
## y el programa no se detiene de forma abrupta.
## Utilidad: validar entradas, archivos y operaciones que pueden fallar.

## Ejercicio 1: division segura (ValueError y ZeroDivisionError)
try:
    numero = int("0")  # simula una entrada; cambia a input() si quieres probarlo
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ValueError:
    print("Error: debes ingresar un numero valido.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
else:
    print("La division se hizo sin errores.")
finally:
    print("Fin del ejercicio 1.\n")


## Ejercicio 2: acceso a lista (IndexError) y conversion (ValueError)
notas = [4.5, 3.8, 5.0]
try:
    posicion = int("5")
    print("La nota es:", notas[posicion])
except ValueError:
    print("Error: la posicion debe ser un numero entero.")
except IndexError:
    print("Error: esa posicion no existe en la lista.")
finally:
    print("Fin del ejercicio 2.\n")


## Ejercicio 3: lectura de archivo (FileNotFoundError)
try:
    with open("archivo_que_no_existe.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: el archivo no existe.")
except PermissionError:
    print("Error: no hay permisos para abrir el archivo.")
except OSError as error:
    print("Error de entrada/salida:", error)
else:
    print("El archivo se leyo correctamente.")
finally:
    print("Operacion de archivo finalizada.")
