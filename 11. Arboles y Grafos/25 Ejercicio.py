# Ejercicio: crea un grafo y usa recorridos #

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)

    def dfs(self, vertice, visitado):
        visitado.add(vertice)
        print(vertice, end=" ")
        for vecino in self.vertices[vertice]:
            if vecino not in visitado:
                self.dfs(vecino, visitado)

    def bfs(self, vertice):
        visitado = set()
        cola = [vertice]
        visitado.add(vertice)
        while cola:
            vertice = cola.pop(0)
            print(vertice, end=" ")
            for vecino in self.vertices[vertice]:
                if vecino not in visitado:
                    visitado.add(vecino)
                    cola.append(vecino)

grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "C")

print("Recorrido en profundidad:")
grafo.dfs("A", set())
print("\nRecorrido en anchura:")
grafo.bfs("A")
