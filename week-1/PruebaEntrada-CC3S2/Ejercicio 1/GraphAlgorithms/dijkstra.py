# Programa para hallar la ruta mínima entre dos nodos de un grafo

# Implementación de Djikstra con matriz de adyacencia
def dijkstra(graph, src):

    dist = [1e7] * graph.V
    dist[src] = 0
    sptSet = [False] * graph.V

    for cout in range(graph.V):

        u = graph.minDistance(dist, sptSet)

        sptSet[u] = True

        for v in range(graph.V):
            if (graph.graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + graph.graph[u][v]):
                dist[v] = dist[u] + graph.graph[u][v]

    graph.printSolution(dist)
