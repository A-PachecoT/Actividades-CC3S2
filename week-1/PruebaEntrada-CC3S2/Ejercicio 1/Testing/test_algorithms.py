from Graph import *
from Graph.Graph import Graph
from GraphAlgorithms.bellman_ford import bellman_ford
from GraphAlgorithms.dijkstra import dijkstra

def test_algorithm(graph, algorithm, initial_vertice, name_algorithm):
    try:
       print("Trying ", name_algorithm)
       algorithm(graph, initial_vertice)

    except:
        print(name_algorithm, " failed")


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

init_v = 0
print("Vértice de inicio: ", init_v)
print("Empezando testing")
test_algorithm(g, dijkstra, init_v, name_algorithm="Dijkstra")
test_algorithm(g, bellman_ford, init_v, name_algorithm="Bellman-Ford")
