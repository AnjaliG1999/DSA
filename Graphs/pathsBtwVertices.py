#!usr/bin/env python3

# Graph object creation and methods
class Graph(): 
    def __init__(self, nodes):
        self.adjList = {}
        self.V = nodes
        for v in range(nodes):
            self.addVertices(v)

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)
        
    def addVertices(self, v):
        self.adjList[v] = []
    
# Find all the possible paths between the given
# source and destination vertices
def findPaths(src, dest, visited, paths, curr):
    visited[src] = True
    curr.append(src)
    if src == dest:
        paths.append(list(curr))
        curr.pop()
        
    else:
        for v in g.adjList[src]:
            if visited[v] == False:
                findPaths(v, dest, visited, paths, curr)
        curr.pop()
    visited[src] = False
    
g = Graph(4) 
g.addEdge(0, 1)  
g.addEdge(0, 2)  
g.addEdge(0, 3)  
g.addEdge(2, 0)  
g.addEdge(2, 1)  
g.addEdge(1, 3)

visited = [False for i in range(4)]
# final list which will contain all possible the paths
paths = []
curr = []
print("Graph:", g.adjList)
findPaths(2, 3, visited, paths, curr)

print("Paths(" + str(len(paths)) + ") :", paths)
