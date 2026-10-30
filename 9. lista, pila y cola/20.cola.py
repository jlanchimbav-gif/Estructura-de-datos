# una cola es una estructura de datos dinamica#
# sigue el principio FIFO primero en entrar y primero en salir#

# programa de atencion al cliente# 
from collections import deque

class AtencionCliente:
    def __init__(self):
        self.cola = deque()

    def nuevo_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"Cliente agregado: {nombre}")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"✅ Cliente atendido: {cliente}")
        else:
            print("No hay clientes en espera.")

    def mostrar_cola(self):
        if self.cola:
            print("📋 Clientes en espera:")
            for i, cliente in enumerate(self.cola, start=1):
                print(f"{i}. {cliente}")
        else:
            print("La cola está vacía.")

# Ejemplo de uso
if __name__ == "__main__":
    atencion = AtencionCliente()

    # Llegan clientes
    atencion.nuevo_cliente("Ana")
    atencion.nuevo_cliente("Luis")
    atencion.nuevo_cliente("María")

    atencion.mostrar_cola()

    # Se atienden clientes
    atencion.atender_cliente()
    atencion.mostrar_cola()

    atencion.atender_cliente()
    atencion.atender_cliente()
    atencion.atender_cliente()  # Intento cuando ya no hay clientes

# programa de cajero automatico , cola circular#

from collections import deque

class CajeroAutomatico:
    def __init__(self, capacidad=3):
        self.capacidad = capacidad
        self.cajeros = [None] * capacidad  # tres posiciones
        self.cola_espera = deque()

    def nuevo_cliente(self, nombre):
        # Buscar un cajero libre
        for i in range(self.capacidad):
            if self.cajeros[i] is None:
                self.cajeros[i] = nombre
                print(f"Cliente {nombre} atendido en cajero {i+1}")
                return
        # Si no hay cajero libre, va a la cola
        self.cola_espera.append(nombre)
        print(f"Cliente {nombre} en espera.")

    def liberar_cajero(self, posicion):
        if 0 <= posicion < self.capacidad and self.cajeros[posicion] is not None:
            print(f"Cliente {self.cajeros[posicion]} terminó en cajero {posicion+1}")
            self.cajeros[posicion] = None
            # Si hay clientes en espera, ocupar el lugar
            if self.cola_espera:
                siguiente = self.cola_espera.popleft()
                self.cajeros[posicion] = siguiente
                print(f"Cliente {siguiente} pasa al cajero {posicion+1}")
        else:
            print("Ese cajero ya está libre o la posición no existe.")

    def mostrar_estado(self):
        print("\n📋 Estado de los cajeros:")
        for i, cliente in enumerate(self.cajeros, start=1):
            if cliente:
                print(f"Cajero {i}: {cliente}")
            else:
                print(f"Cajero {i}: libre")
        print("Cola de espera:", list(self.cola_espera))
        print()
        

# Ejemplo de uso
if __name__ == "__main__":
    banco = CajeroAutomatico()

    banco.nuevo_cliente("Ana")
    banco.nuevo_cliente("Luis")
    banco.nuevo_cliente("María")
    banco.nuevo_cliente("Pedro")  # este va a la cola

    banco.mostrar_estado()

    banco.liberar_cajero(1)  # se libera cajero 2
    banco.mostrar_estado()

    banco.liberar_cajero(0)  # se libera cajero 1
    banco.mostrar_estado()
    
# cola de doble estremo#
from collections import deque

class ColaDoble:
    def __init__(self):
        self.cola = deque()

    def agregar_final(self, elemento):
        self.cola.append(elemento)
        print(f"Elemento agregado al final: {elemento}")

    def agregar_inicio(self, elemento):
        self.cola.appendleft(elemento)
        print(f"Elemento agregado al inicio: {elemento}")

    def eliminar_final(self):
        if self.cola:
            elemento = self.cola.pop()
            print(f"Elemento eliminado del final: {elemento}")
        else:
            print("La cola está vacía.")

    def eliminar_inicio(self):
        if self.cola:
            elemento = self.cola.popleft()
            print(f"Elemento eliminado del inicio: {elemento}")
        else:
            print("La cola está vacía.")

    def mostrar_cola(self):
        print("📋 Estado actual de la cola:", list(self.cola))


# Ejemplo de uso
if __name__ == "__main__":
    cola = ColaDoble()

    cola.agregar_final("Cliente A")
    cola.agregar_final("Cliente B")
    cola.agregar_inicio("Cliente VIP")
    cola.mostrar_cola()

    cola.eliminar_inicio()
    cola.mostrar_cola()

    cola.eliminar_final()
    cola.mostrar_cola()

