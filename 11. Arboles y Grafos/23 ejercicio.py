# Ejercicio: arbol binario de busqueda y sus recorridos
# Regla del arbol: menores a la izquierda, mayores o iguales a la derecha.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        # Si no hay raiz, el primer valor se convierte en ella.
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        # Menor que el nodo actual: baja por la izquierda.
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        # Mayor o igual: baja por la derecha.
        # Hay que crear el nodo cuando ese lado esta vacio.
        # Si se llama _insertar con None, falla: None no tiene .valor
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)

    def preorden(self):
        # Raiz, izquierda, derecha
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

    def inorden(self):
        # Izquierda, raiz, derecha (queda ordenado de menor a mayor)
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden(nodo.derecha)

    def postorden(self):
        # Izquierda, derecha, raiz
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo is not None:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.valor, end=" ")


arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)

print("Preorden:  ", end="")
arbol.preorden()
print("Inorden:   ", end="")
arbol.inorden()
print("Postorden: ", end="")
arbol.postorden()

