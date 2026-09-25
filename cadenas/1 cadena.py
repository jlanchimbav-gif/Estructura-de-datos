from importlib import import_module
from pickle import LONG_BINPUT

# ingreso de la cadena y longitud #
cadena=input("Ingrese una cadena: ")
longitud=len(cadena)
# conversion de la cadena a mayusculas y minusculas #
mayusculas=cadena.upper()
minusculas=cadena.lower()
print(f"En mayusculas: {mayusculas}")
print(f"En minusculas: {minusculas}")
# modificacion de la cadena #
modifica=cadena.replace(" ", "-")
print(f"La cadena modificada es: {modifica}")
# separacion de la cadena en palabras #
palabras=cadena.split("a")
print(f"Las palabras de la cadena son: {palabras}")

# verificacion de la longitud de la cadena #
if len(cadena) > 10:
    print("La cadena es larga")
else:
    print("La cadena es corta")

# verificacion de la presencia de la letra a #
if "a" in cadena:
    print("La cadena contiene la letra a")
else:
    print("La cadena no contiene la letra a")





