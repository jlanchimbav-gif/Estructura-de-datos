"""
Base esencial de estructuras de datos.

Cada estructura incluye:
  - Concepto: que es
  - Utilidad: para que sirve
  - 2 ejemplos ejecutables
"""


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. LISTA / ARREGLO UNIDIMENSIONAL
# Concepto: coleccion ordenada de elementos accesibles por indice (0, 1, 2...).
# Utilidad: guardar secuencias de datos, recorrer, insertar y modificar valores.
# ---------------------------------------------------------------------------
def listas():
    titulo("1. LISTA / ARREGLO")
    print("Concepto: secuencia ordenada de elementos con acceso por indice.")
    print("Utilidad: notas, inventario, colas de espera simples, vectores.\n")

    # Ejemplo 1: notas de un estudiante y promedio
    notas = [4.5, 3.8, 5.0, 4.2]
    promedio = sum(notas) / len(notas)
    print("Ejemplo 1 - Promedio de notas:", notas, "->", round(promedio, 2))

    # Ejemplo 2: buscar el mayor y cambiar un valor
    edades = [18, 21, 19, 25, 22]
    print("Ejemplo 2 - Edad mayor:", max(edades))
    edades[1] = 23
    print("         Lista modificada:", edades)


# ---------------------------------------------------------------------------
# 2. TUPLA
# Concepto: secuencia ordenada e INMUTABLE (no se puede cambiar despues de crearla).
# Utilidad: datos fijos (coordenadas, RGB, registros que no deben alterarse).
# ---------------------------------------------------------------------------
def tuplas():
    titulo("2. TUPLA")
    print("Concepto: coleccion ordenada e inmutable.")
    print("Utilidad: puntos, fechas, claves de diccionario, datos de solo lectura.\n")

    # Ejemplo 1: coordenada (x, y)
    punto = (10, 25)
    print("Ejemplo 1 - Punto (x, y):", punto, "-> x =", punto[0], "y =", punto[1])

    # Ejemplo 2: desempaquetar un registro
    estudiante = ("Ana Perez", 20, "Ingenieria")
    nombre, edad, carrera = estudiante
    print("Ejemplo 2 -", nombre, "tiene", edad, "anos y estudia", carrera)


# ---------------------------------------------------------------------------
# 3. CADENA (STRING)
# Concepto: secuencia inmutable de caracteres.
# Utilidad: textos, nombres, busqueda y transformacion de palabras.
# ---------------------------------------------------------------------------
def cadenas():
    titulo("3. CADENA")
    print("Concepto: texto formado por caracteres.")
    print("Utilidad: nombres, mensajes, validaciones y recorte de texto.\n")

    # Ejemplo 1: normalizar un nombre
    nombre = "  juan  perez  "
    limpio = " ".join(nombre.split()).title()
    print("Ejemplo 1 - Nombre limpio:", repr(nombre), "->", limpio)

    # Ejemplo 2: saber si un correo es institucional
    correo = "estudiante@universidad.edu"
    es_institucional = correo.endswith(".edu")
    print("Ejemplo 2 -", correo, "es institucional?", es_institucional)


# ---------------------------------------------------------------------------
# 4. CONJUNTO (SET)
# Concepto: coleccion SIN orden y SIN duplicados.
# Utilidad: eliminar repetidos, uniones, intersecciones y diferencias.
# ---------------------------------------------------------------------------
def conjuntos():
    titulo("4. CONJUNTO")
    print("Concepto: elementos unicos, sin orden garantizado.")
    print("Utilidad: quitar duplicados, comparar grupos, pertenencia rapida.\n")

    # Ejemplo 1: quitar materias repetidas
    materias = ["Calculo", "Fisica", "Calculo", "Programacion", "Fisica"]
    unicas = set(materias)
    print("Ejemplo 1 - Materias unicas:", unicas)

    # Ejemplo 2: estudiantes que estan en ambos grupos
    grupo_a = {"Ana", "Luis", "Marta"}
    grupo_b = {"Luis", "Pedro", "Marta"}
    comunes = grupo_a & grupo_b
    print("Ejemplo 2 - En ambos grupos:", comunes)


# ---------------------------------------------------------------------------
# 5. DICCIONARIO / TABLA HASH
# Concepto: pares clave-valor. La clave identifica; el valor es el dato.
# Utilidad: busquedas rapidas por nombre, ID, codigo (como un directorio).
# ---------------------------------------------------------------------------
def diccionarios():
    titulo("5. DICCIONARIO / TABLA HASH")
    print("Concepto: mapeo clave -> valor con acceso promedio O(1).")
    print("Utilidad: padrones, inventario por codigo, contadores, indices.\n")

    # Ejemplo 1: nota por estudiante
    notas = {"Ana": 4.5, "Luis": 3.8, "Marta": 5.0}
    print("Ejemplo 1 - Nota de Marta:", notas["Marta"])
    notas["Luis"] = 4.0
    print("         Notas actualizadas:", notas)

    # Ejemplo 2: contar frecuencia de palabras
    frase = "casa sol casa mar sol casa"
    frecuencia = {}
    for palabra in frase.split():
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    print("Ejemplo 2 - Frecuencia:", frecuencia)


# ---------------------------------------------------------------------------
# 6. PILA (STACK) - LIFO
# Concepto: el ultimo en entrar es el primero en salir (Last In, First Out).
# Utilidad: deshacer (Ctrl+Z), llamadas a funciones, validar parentesis.
# ---------------------------------------------------------------------------
def pilas():
    titulo("6. PILA (LIFO)")
    print("Concepto: se inserta y se saca por el mismo extremo (cima).")
    print("Utilidad: historial de acciones, evaluacion de expresiones, recursion.\n")

    # Ejemplo 1: deshacer acciones
    pila = []
    pila.append("escribir hola")   # push
    pila.append("borrar palabra")
    pila.append("cambiar color")
    ultima = pila.pop()            # pop: deshace lo ultimo
    print("Ejemplo 1 - Se deshace:", ultima, "| queda:", pila)

    # Ejemplo 2: validar parentesis balanceados
    def parentesis_ok(expresion):
        pila_local = []
        for caracter in expresion:
            if caracter == "(":
                pila_local.append(caracter)
            elif caracter == ")":
                if not pila_local:
                    return False
                pila_local.pop()
        return len(pila_local) == 0

    print("Ejemplo 2 - (a+b)*c  balanceada?", parentesis_ok("(a+b)*c"))
    print("         - (a+b*c   balanceada?", parentesis_ok("(a+b*c"))


# ---------------------------------------------------------------------------
# 7. COLA (QUEUE) - FIFO
# Concepto: el primero en entrar es el primero en salir (First In, First Out).
# Utilidad: turnos, impresion, atencion al cliente, procesos en espera.
# ---------------------------------------------------------------------------
def colas():
    titulo("7. COLA (FIFO)")
    print("Concepto: se encola al final y se atiende por el frente.")
    print("Utilidad: filas de banco, colas de impresion, BFS en grafos.\n")

    from collections import deque

    # Ejemplo 1: turnos de atencion
    cola = deque()
    cola.append("Ana")     # enqueue
    cola.append("Luis")
    cola.append("Marta")
    atendido = cola.popleft()  # dequeue
    print("Ejemplo 1 - Atendido:", atendido, "| esperan:", list(cola))

    # Ejemplo 2: cola de impresion
    impresion = deque(["tarea1.pdf", "foto.png", "informe.docx"])
    print("Ejemplo 2 - Orden de impresion:")
    while impresion:
        print("         Imprimiendo", impresion.popleft())


# ---------------------------------------------------------------------------
# 8. COLA DE PRIORIDAD / MONTICULO (HEAP)
# Concepto: siempre sale primero el elemento de mayor (o menor) prioridad.
# Utilidad: urgencias medicas, tareas del sistema, Dijkstra.
# ---------------------------------------------------------------------------
def colas_prioridad():
    titulo("8. COLA DE PRIORIDAD / HEAP")
    print("Concepto: cola donde el orden lo define la prioridad, no la llegada.")
    print("Utilidad: emergencias, planificacion de CPU, caminos minimos.\n")

    import heapq

    # Ejemplo 1: menor numero = mayor urgencia
    urgencias = []
    heapq.heappush(urgencias, (1, "infarto"))
    heapq.heappush(urgencias, (3, "gripe"))
    heapq.heappush(urgencias, (2, "fractura"))
    print("Ejemplo 1 - Primero a atender:", heapq.heappop(urgencias))

    # Ejemplo 2: las 2 notas mas bajas
    notas = [4.5, 2.0, 3.8, 1.5, 5.0]
    peores = heapq.nsmallest(2, notas)
    print("Ejemplo 2 - Dos notas mas bajas:", peores)


# ---------------------------------------------------------------------------
# 9. LISTA ENLAZADA
# Concepto: nodos encadenados: cada uno guarda un dato y un enlace al siguiente.
# Utilidad: insertar/borrar sin mover el resto; tamano dinamico.
# ---------------------------------------------------------------------------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def a_lista(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.dato)
            actual = actual.siguiente
        return valores

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1


def listas_enlazadas():
    titulo("9. LISTA ENLAZADA")
    print("Concepto: cadena de nodos (dato + puntero al siguiente).")
    print("Utilidad: historiales, editores, cuando hay muchas inserciones.\n")

    lista = ListaEnlazada()
    lista.insertar_inicio("C")
    lista.insertar_inicio("B")
    lista.insertar_inicio("A")
    print("Ejemplo 1 - Recorrido:", lista.a_lista())
    print("Ejemplo 2 - Posicion de 'B':", lista.buscar("B"))


# ---------------------------------------------------------------------------
# 10. MATRIZ / ARREGLO BIDIMENSIONAL
# Concepto: tabla de filas y columnas; se accede con dos indices [i][j].
# Utilidad: tableros, imagenes, notas por estudiante/materia, grafos.
# ---------------------------------------------------------------------------
def matrices():
    titulo("10. MATRIZ (BIDIMENSIONAL)")
    print("Concepto: arreglo de arreglos (filas x columnas).")
    print("Utilidad: calendarios, mapas, sistemas de ecuaciones, pixeles.\n")

    # Ejemplo 1: notas de 3 estudiantes en 2 materias
    notas = [
        [4.5, 3.8],
        [5.0, 4.2],
        [3.0, 4.0],
    ]
    print("Ejemplo 1 - Nota estudiante 2, materia 1:", notas[1][0])

    # Ejemplo 2: suma por fila (promedio de cada estudiante)
    print("Ejemplo 2 - Promedio por estudiante:")
    for i, fila in enumerate(notas, start=1):
        print("         Estudiante", i, "->", round(sum(fila) / len(fila), 2))


# ---------------------------------------------------------------------------
# 11. ARBOL BINARIO
# Concepto: nodos con un padre y hasta dos hijos (izquierdo y derecho).
# Utilidad: busquedas, jerarquias, expresiones, bases de datos (BST).
# ---------------------------------------------------------------------------
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


def insertar_bst(raiz, dato):
    if raiz is None:
        return NodoArbol(dato)
    if dato < raiz.dato:
        raiz.izq = insertar_bst(raiz.izq, dato)
    elif dato > raiz.dato:
        raiz.der = insertar_bst(raiz.der, dato)
    return raiz


def inorden(raiz, recorrido):
    if raiz:
        inorden(raiz.izq, recorrido)
        recorrido.append(raiz.dato)
        inorden(raiz.der, recorrido)


def buscar_bst(raiz, dato):
    if raiz is None:
        return False
    if dato == raiz.dato:
        return True
    if dato < raiz.dato:
        return buscar_bst(raiz.izq, dato)
    return buscar_bst(raiz.der, dato)


def arboles():
    titulo("11. ARBOL BINARIO DE BUSQUEDA")
    print("Concepto: jerarquia; en un BST izq < raiz < der.")
    print("Utilidad: directorios, organigramas, busqueda ordenada rapida.\n")

    valores = [8, 3, 10, 1, 6]
    raiz = None
    for valor in valores:
        raiz = insertar_bst(raiz, valor)

    recorrido = []
    inorden(raiz, recorrido)
    print("Ejemplo 1 - Inorden (queda ordenado):", recorrido)
    print("Ejemplo 2 - Esta el 6?", buscar_bst(raiz, 6), "| Esta el 9?", buscar_bst(raiz, 9))


# ---------------------------------------------------------------------------
# 12. GRAFO
# Concepto: vertices (nodos) unidos por aristas (conexiones).
# Utilidad: redes sociales, mapas, internet, dependencias de materias.
# ---------------------------------------------------------------------------
def grafos():
    titulo("12. GRAFO")
    print("Concepto: conjunto de nodos y conexiones entre ellos.")
    print("Utilidad: rutas, amistades, circuitos, flujos de trabajo.\n")

    # Lista de adyacencia: cada ciudad y a quienes llega
    ciudad = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    print("Ejemplo 1 - Vecinos de A:", ciudad["A"])

    # Ejemplo 2: recorrido en amplitud (BFS) desde A
    from collections import deque

    def bfs(inicio):
        visitados = []
        cola = deque([inicio])
        vistos = {inicio}
        while cola:
            actual = cola.popleft()
            visitados.append(actual)
            for vecino in ciudad[actual]:
                if vecino not in vistos:
                    vistos.add(vecino)
                    cola.append(vecino)
        return visitados

    print("Ejemplo 2 - BFS desde A:", bfs("A"))


def main():
    print("BASE ESENCIAL DE ESTRUCTURAS DE DATOS")
    print("Concepto + utilidad + 2 ejemplos por estructura")
    listas()
    tuplas()
    cadenas()
    conjuntos()
    diccionarios()
    pilas()
    colas()
    colas_prioridad()
    listas_enlazadas()
    matrices()
    arboles()
    grafos()
    print("\n" + "=" * 60)
    print("Fin de la base esencial.")
    print("=" * 60)


if __name__ == "__main__":
    main()
