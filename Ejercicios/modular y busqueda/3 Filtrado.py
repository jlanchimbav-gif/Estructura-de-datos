## el filtrado es el proceso de seleccionar elementos de una lista basados en una condición #
## Sirven para seleccionar elementos de una lista basados en una condición #

# Filtar los numeros pares de la lista #

numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=[]
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"Los numeros pares son: {pares}")
