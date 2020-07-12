#!usr/bin/env python3

# Graph object creation and methods
class Graph:
    def __init__(self):
        self.adjList = {}

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
            # input taken as 2 space-separated strings e.g. s w, or vertex1 vertex2
            v1, v2 = map(str, input().split())
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
            print("You are accessing an invalid vertex!")

# Remove edges from the graph
def removeEdges(directed):
    numEdges = int(input('Enter number of edges to remove: '))
    print('Enter the vertices: ')
    for edge in range(numEdges):
        try:
            # input taken as 2 space-separated strings e.g. s w, or vertex1 vertex2
            v1, v2 = map(str, input().split())
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
        	print("You are accessing an invalid vertex!")

# Breadth First Search tree traversal
def BFS(source):
    visited = []    # list used so that every vertex is traversed exactly once
    queue = []
    queue.append(source)
    visited.append(source)
    while queue:
        for vertex in g.adjList[queue.pop()]:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)
    print(visited)
 
# Recursive function to traverse vertices
def DFSvisit(vertex, visited):
    visited.append(vertex)
    for v in g.adjList[vertex]:
        if v not in visited:
            DFSvisit(v, visited)

# Depth First Search tree traversal 
def DFS(source):  
    visited = []    # list used so that every vertex is traversed exactly once
    DFSvisit(source, visited)  
    print(visited)   

# Runs the loop til the input is provided
try:
    g = Graph()
    totalVertices = int(input('Enter number of vertices: '))
    # populate the graph with isolated vertices
    print('Enter vertex names: ')
    for vertex in range(totalVertices):
        vertexName = input()
        if vertexName not in g.adjList: 
            g.adjList[vertexName] = []
        else:
            print('Vertex already exists.')
            
    directed = int(input('Directed: 1, Undirected: 0\n'))
    while True:
        addOrRemove = int(input('Remove edges:1, Add edges: 0\n'))
        removeEdges(directed) if addOrRemove else addEdges(directed)
        source = input('Enter source vertex for traversal: ')
        BFS(source)
        DFS(source)

except ValueError:
    print("Program Exit")
