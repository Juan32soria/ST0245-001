import pandas as pd
import sys
from heapq import heapify, heappop, heappush

file = pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=';')


def createGraph():
    graph = {}
    for index, row in file.iterrows():
        if row['origin'] not in graph:
            graph[row['origin']] = {row['destination']: row['length']}
        else:
            graph[row['origin']][row['destination']] = row['length']
        if row['destination'] not in graph:
            graph[row['destination']] = {row['origin']: row['length']}
        else:
            graph[row['destination']][row['origin']] = row['length']
    return graph


def createGraphHarassment():
    graph = {}
    for index, row in file.iterrows():
        if row['origin'] not in graph:
            graph[row['origin']] = {row['destination']: row['harassmentRisk']}
        else:
            graph[row['origin']][row['destination']] = row['harassmentRisk']
        if row['destination'] not in graph:
            graph[row['destination']] = {row['origin']: row['harassmentRisk']}
        else:
            graph[row['destination']][row['origin']] = row['harassmentRisk']
    return graph


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float('inf')
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        return 'El camino es: ' + ''.join(path)


def ask(graph):
    while True:
        initial = input('Ingrese inicial ')
        if initial == 'no':
            break
        print('La coordenada conecta con los puntos: ')
        print(graph[initial])

def main():
    print('1. Consultar camino más corto')
    print('2. Consultar camino más seguro')
    n = int(input('Ingrese la opción que desea consultar: '))
    if n == 1:
        graph = createGraph()
        start = input('Ingrese coordenada inicial')
        goal = input('Ingrese coordenada final')
        print(dijkstra(graph, start, goal))
    elif n == 2:
        graph = createGraphHarassment()
        start = input('Ingrese coordenada inicial')
        goal = input('Ingrese coordenada final')
        print(dijkstra(graph, start, goal))


main()
