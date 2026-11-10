from collections import deque
from datetime import datetime

# Cola de atención
cola = deque()

# Historial de atendidos
historial = []

# Contador de turnos
contador_turnos = 1


def registrar_cliente():
    global contador_turnos

    nombre = input("Ingrese el nombre del cliente: ").strip()

    if not nombre:
        print(" El nombre no puede estar vacío.")
        return

    turno = f"T{contador_turnos:03d}"
    hora_llegada = datetime.now().strftime("%H:%M:%S")

    cola.append((turno, nombre, hora_llegada))
    contador_turnos += 1

    print("\n Cliente registrado correctamente")
    print(f"Turno asignado: {turno}")
    print(f"Cliente: {nombre}")
    print(f"Hora de llegada: {hora_llegada}")
    print(f"Clientes en espera: {len(cola)}")


def atender_cliente():
    try:
        turno, nombre, hora_llegada = cola.popleft()

        historial.append((turno, nombre))

        print("\n Atendiendo cliente")
        print(f"Turno: {turno}")
        print(f"Nombre: {nombre}")
        print(f"Hora llegada: {hora_llegada}")
        print(f"Clientes restantes: {len(cola)}")

    except IndexError:
        print(" No hay clientes en espera.")


def ver_siguiente_cliente():
    if cola:
        turno, nombre, hora_llegada = cola[0]

        print("\n🔎 Siguiente cliente")
        print(f"Turno: {turno}")
        print(f"Nombre: {nombre}")
        print(f"Hora llegada: {hora_llegada}")
    else:
        print(" La cola está vacía.")


def mostrar_cola():
    if not cola:
        print(" No hay clientes en espera.")
        return

    print("\n========== COLA DE ESPERA ==========")

    for posicion, (turno, nombre, hora) in enumerate(cola, start=1):
        print(f"{posicion}. {turno} - {nombre} ({hora})")

    print(f"\nTotal en espera: {len(cola)}")


def mostrar_estadisticas():
    print("\n========== ESTADÍSTICAS ==========")

    print(f"Clientes atendidos: {len(historial)}")
    print(f"Clientes pendientes: {len(cola)}")

    if historial:
        primer_turno, primer_cliente = historial[0]
        ultimo_turno, ultimo_cliente = historial[-1]

        print(
            f"Primer cliente atendido: {primer_turno} - {primer_cliente}"
        )
        print(
            f"Último cliente atendido: {ultimo_turno} - {ultimo_cliente}"
        )


# Programa principal
while True:
    print("\n===================================")
    print(" SISTEMA DE TURNOS DE ATENCIÓN")
    print("===================================")
    print("1. Registrar cliente")
    print("2. Atender cliente")
    print("3. Ver siguiente cliente")
    print("4. Mostrar cola")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        registrar_cliente()

    elif opcion == "2":
        atender_cliente()

    elif opcion == "3":
        ver_siguiente_cliente()

    elif opcion == "4":
        mostrar_cola()

    elif opcion == "5":
        mostrar_estadisticas()
        print("\n Programa finalizado.")
        break

    else:
        print(" Opción no válida. Intente nuevamente.")

