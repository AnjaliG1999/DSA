#!usr/bin/env python3

# Graph object creation and methods
class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, v1, v2):
        
        if v1 in self.adjList:
            self.adjList[v1].append(v2)
        else:
            print('No such vertex')
    
    def addVertices(self, v):
        self.adjList[v] = []

# Recursive function for DFS
def DFSvisit(vertex, visited):
    visited.append(vertex)
    for v in g.adjList[vertex]:
        if v not in visited:
            DFSvisit(v, visited)
  
# Find the mother vertex of the graph if present
def findMother():
    visited = []
    last = 0
    # find the vertex that calls DFS last (possible mother vertex)
    for vertex in g.adjList:
        if vertex not in visited:
            DFSvisit(vertex, visited)
            last = vertex

    # check if the last vertex can reach all the vertices in the graph
    visited = []
    DFSvisit(last, visited)
    
    if len(visited) == len(g.adjList):
        print('Mother Vertex: ' + str(last))
    else:
        print('No mother vertex present')

g = Graph()
for v in range(7):
    g.addVertices(v)

g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0) 
print(g.adjList)
findMother()
