import pandas as pd
import sys
from heapq import heapify, heappop, heappush
file = pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=';')


def crearGrafo():
    grafo = {}
    for index, row in file.iterrows():
        if row['origin'] not in grafo:
            grafo[row['origin']] = {row['destination']: row['length']}
        else:
            grafo[row['origin']][row['destination']] = row['length']
        if row['destination'] not in grafo:
            grafo[row['destination']] = {row['origin']: row['length']}
        else:
            grafo[row['destination']][row['origin']] = row['length']
    return grafo


def crearRiesgo():
    grafo = {}
    for index, row in file.iterrows():
        if row['origin'] not in grafo:
            grafo[row['origin']] = {row['destination']: row['harassmentRisk']}
        else:
            grafo[row['origin']][row['destination']] = row['harassmentRisk']
        if row['destination'] not in grafo:
            grafo[row['destination']] = {row['origin']: row['harassmentRisk']}
        else:
            grafo[row['destination']][row['origin']] = row['harassmentRisk']
    return grafo


def algoritmoDijkstra(grafo, inicio, final):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = grafo
    infinity = float('inf')
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[inicio] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for childNode, weight in grafo[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = final
    while currentNode != inicio:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, inicio)
    if shortest_distance[final] != infinity:
        return 'El camino es: ' + ''.join(path)

def main():
    print('Bienvenido, qué es lo que desea hacer?')
    print('Ingrese "A" si desea consultar camino más corto')
    print('Ingrese "B" si desea consultar camino más seguro')
    x = input()
    if x == "A":
        grafo = crearGrafo()
        inicio = input('Ingrese la coordenada de inicio: ')
        final = input('Ingrese la coordenada de finalización: ')
        print(algoritmoDijkstra(grafo, inicio, final))
    elif x == "B":
        grafo = crearRiesgo()
        inicio = input('Ingrese la coordenada de inicio: ')
        final = input('Ingrese la coordenada de finalización: ')
        print(algoritmoDijkstra(grafo, inicio, final))


main()