# Una pila es una estructura de datos dinamica y lineal#
#sigue el principio LIFO ultimo elemento en entrar y primero en salir#

#Ejemplo con funciones basicas#
from collections import deque

# Crear una pila vacía
pila = deque()

# Apilar elementos (push)
pila.append("A")
pila.append("B")
pila.append("C")

print("Pila después de apilar:", pila)

# Desapilar elementos (pop)
elemento = pila.pop()
print("Elemento desapilado:", elemento)
print("Pila después de desapilar:", pila)

# Ver el elemento en la cima sin quitarlo
cima = pila[-1]
print("Elemento en la cima:", cima)

# Verificar si la pila está vacía
if not pila:
    print("La pila está vacía")
else:
    print("La pila tiene elementos")

# ejemplo de programa que administra tareas#

from collections import deque

class AdministradorTareas:
    def __init__(self):
        self.tareas = deque()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def eliminar_tarea(self):
        if self.tareas:
            tarea = self.tareas.pop()
            print(f"Tarea eliminada: {tarea}")
        else:
            print("No hay tareas para eliminar.")

    def ver_tarea_actual(self):
        if self.tareas:
            print(f"Tarea en la cima: {self.tareas[-1]}")
        else:
            print("No hay tareas en la pila.")

    def listar_tareas(self):
        if self.tareas:
            print(" Lista de tareas:")
            for i, tarea in enumerate(reversed(self.tareas), start=1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas registradas.")

# Ejemplo de uso
if __name__ == "__main__":
    admin = AdministradorTareas()
    admin.agregar_tarea("Estudiar Python")
    admin.agregar_tarea("Hacer ejercicio")
    admin.agregar_tarea("Leer un libro")

    admin.listar_tareas()
    admin.ver_tarea_actual()

    admin.eliminar_tarea()
    admin.listar_tareas()

# calculadora con operaciones basicas# 

from collections import deque

class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.historial = deque()  # pila para deshacer

    def sumar(self, valor):
        self.historial.append(self.resultado)
        self.resultado += valor
        print(f"Suma: {valor} → Resultado = {self.resultado}")

    def restar(self, valor):
        self.historial.append(self.resultado)
        self.resultado -= valor
        print(f"Resta: {valor} → Resultado = {self.resultado}")

    def multiplicar(self, valor):
        self.historial.append(self.resultado)
        self.resultado *= valor
        print(f"Multiplicación: {valor} → Resultado = {self.resultado}")

    def dividir(self, valor):
        if valor == 0:
            print("Error: División por cero no permitida.")
            return
        self.historial.append(self.resultado)
        self.resultado /= valor
        print(f"División: {valor} → Resultado = {self.resultado}")

    def deshacer(self):
        if self.historial:
            self.resultado = self.historial.pop()
            print(f"🔄 Deshacer → Resultado = {self.resultado}")
        else:
            print("No hay operaciones para deshacer.")

    def mostrar_resultado(self):
        print(f"Resultado actual = {self.resultado}")


# Ejemplo de uso
if __name__ == "__main__":
    calc = Calculadora()

    calc.sumar(10)
    calc.multiplicar(2)
    calc.restar(5)
    calc.dividir(3)

    calc.mostrar_resultado()

    # Deshacer últimas operaciones
    calc.deshacer()
    calc.deshacer()
    calc.mostrar_resultado()
