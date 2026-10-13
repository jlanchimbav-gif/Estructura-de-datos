## el with es un contexto que se utiliza para abrir un archivo y se cierra automaticamente##
## ejemplo: with open('archivo.txt', 'r') as archivo:
## archivo.read()

with open('archivo.txt', 'r') as archivo:
    print(archivo.read())

## Ejemplo 2: with open('archivo.txt', 'w') as archivo:
## archivo.write('Hola, mundo!')

with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!')
    
 ## tell es una funcion que se utiliza para saber la posicion del cursor en el archivo##
 ## ejemplo: archivo.tell()

with open('archivo.txt', 'r') as archivo:
    print(archivo.tell())

## Ejemplo 3: with open('archivo.txt', 'r') as archivo:
## archivo.seek(0)

with open('archivo.txt', 'r') as archivo:
    archivo.seek(0)
    print(archivo.read())
    
    
## read es una funcion que se utiliza para leer el archivo##
## ejemplo: archivo.read()

with open('archivo.txt', 'r') as archivo:
    print(archivo.read())
    
## write es una funcion que se utiliza para escribir en el archivo##
## ejemplo: archivo.write('Hola, mundo!')

with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!')
    