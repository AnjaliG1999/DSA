#!usr/bin/env python3

# Graph object creation and methods
class Graph:
    def __init__(self, totalNodes):
        self.totalNodes = totalNodes
        self.adjList = [[] for x in range(totalNodes + 1)]

    def addDirectedEdge(self, v1, v2):
        if v2 not in self.adjList[v1]:
            self.adjList[v1].append(v2)

    def addUndirectedEdge(self, v1, v2):
        self.addDirectedEdge(v1, v2)
        self.addDirectedEdge(v2, v1)

    def removeDirectedEdge(self, v1, v2):
        if v2 in self.adjList[v1]:
        	self.adjList[v1].remove(v2)

    def removeUndirectedEdge(self, v1, v2):
        self.removeDirectedEdge(v1, v2)
        self.removeDirectedEdge(v2, v1)

# Add new edges to the graph
def addEdges(directed):
    numEdges = int(input('Enter the total number of edges: '))
    print('Enter the vertices: ')
    for edge in range(numEdges):
        try:
            #input taken as 2 space-separated integers e.g. 3 4, or 1 5
            v1, v2 = map(int, input().split())
            if directed:                           
                if v2 not in g.adjList[v1]:
                    g.addDirectedEdge(v1, v2)
                else:
                    print('Edge already exists.')
            else:
                if v2 not in g.adjList[v1]:
                    g.addUndirectedEdge(v1, v2)
                else:
                    print('Edge already exists.')
        except IndexError:
            print("You are accessing an invalid node!")

# Remove edges from the graph
def removeEdges(directed):
    numEdges = int(input('Enter number of edges to remove: '))
    print('Enter the vertices: ')
    for edge in range(numEdges):
        try:
            #input taken as 2 space-separated integers e.g. 3 4, or 1 5
            v1, v2 = map(int, input().split())
            if directed:
                if v2 in g.adjList[v1]:
                    g.removeDirectedEdge(v1, v2)
                else:
                    print('No such edge.')
            else:  
                if v2 in g.adjList[v1]:
                    g.removeUndirectedEdge(v1, v2)
                else:
                    print('No such edge.')

        except IndexError:
        	print("You are accessing an invalid node!")

g = Graph(int(input('Enter number of nodes: ')))
directed = int(input('Directed: 1, Undirected: 0\n'))

# Runs the loop til the input is provided
try:
    while True:
        addOrRemove = int(input('Remove edges:1, Add edges: 0\n'))
        removeEdges(directed) if addOrRemove else addEdges(directed)
        print(g.adjList[1:])

except ValueError:
    addOrRemove = None