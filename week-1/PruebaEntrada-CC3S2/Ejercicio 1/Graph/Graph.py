# Estructura de datos de Grafo
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] # matriz de adyacencia
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vértice \t Distancia desde la fuente")
        for node in range(self.V):
            print(node, "\t\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index