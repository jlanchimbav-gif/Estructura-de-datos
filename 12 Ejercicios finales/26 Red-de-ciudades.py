# Ejercicio 26: Red de ciudades
# Una red de ciudades es un grafo dirigido donde cada arco tiene un peso que representa la distancia entre las ciudades.

#Mejoras añadidas:
#Uso de sets para evitar duplicados
#Monstrar el total de ciudades y carreteras
#Eliminar ciudaes y carreteras
#Verificar las conexiones de las ciudades


from collections import deque

grafo = {}


def agregar_ciudad():
    ciudad = input("Nombre de la ciudad: ").strip().title()

    if ciudad in grafo:
        print(" La ciudad ya existe.")
    else:
        grafo[ciudad] = set()
        print(f" Ciudad '{ciudad}' agregada.")


def conectar_ciudades():
    try:
        origen = input("Ciudad origen: ").strip().title()
        destino = input("Ciudad destino: ").strip().title()

        if origen == destino:
            print(" No se puede conectar una ciudad consigo misma.")
            return

        if destino in grafo[origen]:
            print(" Las ciudades ya están conectadas.")
            return

        grafo[origen].add(destino)
        grafo[destino].add(origen)

        print(f" {origen} conectado con {destino}.")

    except KeyError:
        print(" Una o ambas ciudades no existen.")


def eliminar_ciudad():
    try:
        ciudad = input("Ciudad a eliminar: ").strip().title()

        for vecina in grafo[ciudad]:
            grafo[vecina].remove(ciudad)

        del grafo[ciudad]

        print(f" Ciudad '{ciudad}' eliminada.")

    except KeyError:
        print(" La ciudad no existe.")

def eliminar_carretera():
    try:
        origen = input("Ciudad origen: ").strip().title()
        destino = input("Ciudad destino: ").strip().title()

        if destino not in grafo[origen]:
            print(" No existe esa carretera.")
            return

        grafo[origen].remove(destino)
        grafo[destino].remove(origen)

        print(f" Carretera eliminada entre {origen} y {destino}.")

    except KeyError:
        print(" Una o ambas ciudades no existen.")


def mostrar_lista_adyacencia():
    if not grafo:
        print(" No hay ciudades registradas.")
        return

    print("\n===== RED DE CIUDADES =====")

    for ciudad in sorted(grafo):
        vecinos = sorted(grafo[ciudad])

        print(
            f"{ciudad} → "
            f"{', '.join(vecinos) if vecinos else 'Sin conexiones'}"
        )

    total_carreteras = sum(len(v) for v in grafo.values()) // 2

    print("\n===== ESTADÍSTICAS =====")
    print(f"Ciudades: {len(grafo)}")
    print(f"Carreteras: {total_carreteras}")


def ver_vecinas():
    try:
        ciudad = input("Ingrese una ciudad: ").strip().title()

        vecinos = sorted(grafo[ciudad])

        print(f"\nCiudad: {ciudad}")
        print(
            f"Vecinas: {', '.join(vecinos) if vecinos else 'Ninguna'}"
        )
        print(f"Grado: {len(vecinos)}")

    except KeyError:
        print(" La ciudad no existe.")


def bfs():
    try:
        inicio = input("Ciudad inicial: ").strip().title()

        visitados = []
        cola = deque([inicio])

        while cola:
            actual = cola.popleft()

            if actual not in visitados:
                visitados.append(actual)

                for vecino in sorted(grafo[actual]):
                    if vecino not in visitados:
                        cola.append(vecino)

        print("\nRecorrido BFS:")
        print(" → ".join(visitados))

    except KeyError:
        print(" La ciudad no existe.")


def buscar_ruta():
    try:
        origen = input("Ciudad origen: ").strip().title()
        destino = input("Ciudad destino: ").strip().title()

        cola = deque([origen])
        visitados = set()

        while cola:
            actual = cola.popleft()

            if actual == destino:
                print(
                    f" Existe una ruta entre "
                    f"{origen} y {destino}."
                )
                return

            if actual not in visitados:
                visitados.add(actual)

                for vecino in grafo[actual]:
                    if vecino not in visitados:
                        cola.append(vecino)

        print(
            f" No existe una ruta entre "
            f"{origen} y {destino}."
        )

    except KeyError:
        print(" Una o ambas ciudades no existen.")


# Programa principal
while True:

    print("\n=================================")
    print("   RED DE CIUDADES (GRAFO)")
    print("=================================")
    print("1. Agregar ciudad")
    print("2. Conectar ciudades")
    print("3. Mostrar lista de adyacencia")
    print("4. Ver ciudades vecinas")
    print("5. Recorrido en anchura (BFS)")
    print("6. Buscar ruta entre ciudades")
    print("7. Eliminar carretera")
    print("8. Eliminar ciudad")
    print("9. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        agregar_ciudad()

    elif opcion == "2":
        conectar_ciudades()

    elif opcion == "3":
        mostrar_lista_adyacencia()

    elif opcion == "4":
        ver_vecinas()

    elif opcion == "5":
        bfs()

    elif opcion == "6":
        buscar_ruta()

    elif opcion == "7":
        eliminar_carretera()

    elif opcion == "8":
        eliminar_ciudad()

    elif opcion == "9":
        print(" Programa finalizado.")
        break

    else:
        print(" Opción no válida.")