from collections import deque
from datetime import datetime

# =============================================
# DATOS DEL PROYECTO
# =============================================

GRUPO = "X"
INTEGRANTES = "Nombre 1, Nombre 2, Nombre 3"

# =============================================
# ENCABEZADO
# =============================================

def mostrar_encabezado(proyecto):
    print("\n=============================================")
    print(f"GRUPO NRO: {GRUPO} | INTEGRANTES: {INTEGRANTES}")
    print(f"PROYECTO: {proyecto}")
    print("=============================================")


# =============================================
# PROGRAMA 1 - LISTA DE COMPRAS
# =============================================

def programa_lista_compras():

    mostrar_encabezado("Lista de Compras")

    lista_compras = []

    while True:

        print("\n===== MENÚ DE LISTA DE COMPRAS =====")
        print("1. Agregar producto")
        print("2. Insertar producto en una posición")
        print("3. Eliminar producto")
        print("4. Mostrar lista")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            producto = input(
                "Ingrese el nombre del producto: "
            )

            lista_compras.append(producto)

            print("Producto agregado correctamente.")

        elif opcion == "2":

            producto = input(
                "Ingrese el nombre del producto: "
            )

            try:

                posicion = int(
                    input(
                        "Ingrese la posición donde desea insertar: "
                    )
                )

                if (
                    posicion < 1
                    or posicion > len(lista_compras) + 1
                ):

                    print(
                        "Error: La posición no es válida."
                    )

                else:

                    lista_compras.insert(
                        posicion - 1,
                        producto
                    )

                    print(
                        "Producto insertado correctamente."
                    )

            except ValueError:

                print(
                    "Error: Debe ingresar un número entero."
                )

        elif opcion == "3":

            producto = input(
                "Ingrese el producto que desea eliminar: "
            )

            try:

                lista_compras.remove(producto)

                print(
                    "Producto eliminado correctamente."
                )

            except ValueError:

                print(
                    "Error: El producto no existe en la lista."
                )

        elif opcion == "4":

            print("\n===== LISTA DE COMPRAS =====")

            if len(lista_compras) == 0:

                print(
                    "La lista de compras está vacía."
                )

            else:

                for i, producto in enumerate(
                    lista_compras,
                    start=1
                ):

                    print(f"{i}. {producto}")

                print(
                    "Total de productos:",
                    len(lista_compras)
                )

        elif opcion == "5":

            print(
                "Regresando al Menú Principal..."
            )

            break

        else:

            print(
                "Opción no válida. Intente nuevamente."
            )


# =============================================
# PROGRAMA 2 - HISTORIAL DE NAVEGACIÓN
# =============================================

def visitar_pagina(pila):

    pagina = input(
        "Ingrese la dirección de la página: "
    ).strip()

    if pagina == "":

        print(
            "La dirección no puede estar vacía."
        )

        return

    pila.append(pagina)

    print(f"Página visitada: {pagina}")


def regresar_pagina(pila):

    try:

        cerrada = pila.pop()

        print(f"Página cerrada: {cerrada}")

        if pila:

            print(
                f"Página actual: {pila[-1]}"
            )

        else:

            print(
                "Ya no hay más páginas en el historial."
            )

    except IndexError:

        print(
            "Error: el historial está vacío, no hay página a la cual regresar."
        )


def ver_pagina_actual(pila):

    if pila:

        print(
            f"Página actual: {pila[-1]}"
        )

    else:

        print(
            "La pila está vacía, no hay página actual."
        )


def mostrar_historial(pila):

    if not pila:

        print("El historial está vacío.")

    else:

        print(
            "Historial (del tope a la base):"
        )

        for i in range(
            len(pila) - 1,
            -1,
            -1
        ):

            marca = (
                " <- TOPE"
                if i == len(pila) - 1
                else ""
            )

            if (
                i == 0
                and len(pila) > 1
            ):
                marca = " <- BASE"

            print(
                f"{i + 1}. {pila[i]}{marca}"
            )

        print(
            f"Tamaño de la pila: {len(pila)}"
        )


def programa_historial():

    mostrar_encabezado(
        "Historial de Navegación (Pilas)"
    )

    historial = []

    while True:

        print(
            "\n===== HISTORIAL DE NAVEGACIÓN ====="
        )

        print("1. Visitar página (push)")
        print(
            "2. Regresar a la página anterior (pop)"
        )
        print("3. Ver página actual (peek)")
        print("4. Mostrar historial")
        print("5. Volver al Menú Principal")

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":

            visitar_pagina(historial)

        elif opcion == "2":

            regresar_pagina(historial)

        elif opcion == "3":

            ver_pagina_actual(historial)

        elif opcion == "4":

            mostrar_historial(historial)

        elif opcion == "5":

            print(
                "Regresando al Menú Principal..."
            )

            break

        else:

            print(
                "Opción no válida. Intente de nuevo."
            )


# =============================================
# PROGRAMA 3 - TURNOS DE ATENCIÓN
# =============================================

cola = deque()
historial_clientes = []
contador_turnos = 1


def registrar_cliente():

    global contador_turnos

    nombre = input(
        "Ingrese el nombre del cliente: "
    ).strip()

    if not nombre:

        print(
            "El nombre no puede estar vacío."
        )

        return

    turno = f"T{contador_turnos:03d}"

    hora_llegada = datetime.now().strftime(
        "%H:%M:%S"
    )

    cola.append(
        (
            turno,
            nombre,
            hora_llegada
        )
    )

    contador_turnos += 1

    print(
        "\nCliente registrado correctamente"
    )

    print(f"Turno asignado: {turno}")
    print(f"Cliente: {nombre}")
    print(
        f"Hora de llegada: {hora_llegada}"
    )
    print(
        f"Clientes en espera: {len(cola)}"
    )


def atender_cliente():

    try:

        turno, nombre, hora_llegada = (
            cola.popleft()
        )

        historial_clientes.append(
            (
                turno,
                nombre
            )
        )

        print(
            "\nAtendiendo cliente"
        )

        print(f"Turno: {turno}")
        print(f"Nombre: {nombre}")
        print(
            f"Hora llegada: {hora_llegada}"
        )

        print(
            f"Clientes restantes: {len(cola)}"
        )

    except IndexError:

        print(
            "No hay clientes en espera."
        )


def ver_siguiente_cliente():

    if cola:

        turno, nombre, hora_llegada = cola[0]

        print(
            "\nSiguiente cliente"
        )

        print(f"Turno: {turno}")
        print(f"Nombre: {nombre}")
        print(
            f"Hora llegada: {hora_llegada}"
        )

    else:

        print(
            "La cola está vacía."
        )


def mostrar_cola():

    if not cola:

        print(
            "No hay clientes en espera."
        )

        return

    print(
        "\n========== COLA DE ESPERA =========="
    )

    for posicion, (
        turno,
        nombre,
        hora
    ) in enumerate(
        cola,
        start=1
    ):

        print(
            f"{posicion}. {turno} - {nombre} ({hora})"
        )

    print(
        f"\nTotal en espera: {len(cola)}"
    )


def mostrar_estadisticas():

    print(
        "\n========== ESTADÍSTICAS =========="
    )

    print(
        f"Clientes atendidos: {len(historial_clientes)}"
    )

    print(
        f"Clientes pendientes: {len(cola)}"
    )

    if historial_clientes:

        primer_turno, primer_cliente = (
            historial_clientes[0]
        )

        ultimo_turno, ultimo_cliente = (
            historial_clientes[-1]
        )

        print(
            f"Primer cliente atendido: {primer_turno} - {primer_cliente}"
        )

        print(
            f"Último cliente atendido: {ultimo_turno} - {ultimo_cliente}"
        )


def programa_turnos():

    mostrar_encabezado(
        "Turnos de Atención en Ventanilla"
    )

    while True:

        print(
            "\n==================================="
        )
        print(
            " SISTEMA DE TURNOS DE ATENCIÓN"
        )
        print(
            "==================================="
        )
        print("1. Registrar cliente")
        print("2. Atender cliente")
        print("3. Ver siguiente cliente")
        print("4. Mostrar cola")
        print(
            "5. Volver al Menú Principal"
        )

        opcion = input(
            "\nSeleccione una opción: "
        )

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

            print(
                "\nRegresando al Menú Principal..."
            )

            break

        else:

            print(
                "Opción no válida. Intente nuevamente."
            )


# =============================================
# MENÚ PRINCIPAL
# =============================================

def menu_principal():

    while True:

        mostrar_encabezado(
            "MENÚ PRINCIPAL"
        )

        print(
            "1. Lista de Compras"
        )
        print(
            "2. Historial de Navegación"
        )
        print(
            "3. Turnos de Atención"
        )
        print("4. Salir")

        try:

            opcion = int(
                input(
                    "\nSeleccione una opción: "
                )
            )

            if opcion == 1:

                programa_lista_compras()

            elif opcion == 2:

                programa_historial()

            elif opcion == 3:

                programa_turnos()

            elif opcion == 4:

                print(
                    "\nGracias por utilizar el sistema."
                )

                break

            else:

                print(
                    "Error: opción fuera de rango."
                )

        except ValueError:

            print(
                "Error: Debe ingresar un número."
            )


# =============================================
# EJECUCIÓN
# =============================================

menu_principal()