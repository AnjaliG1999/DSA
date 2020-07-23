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
        
# Find transitive closure of the graph
def transitiveUtil(listKey, reachable, queue):
    for vertex in g.adjList[listKey]:
        if vertex not in queue:
            reachable[queue[0]][vertex] = 1
            queue.append(vertex)
            transitiveUtil(vertex, reachable, queue)
        
def transitive(reachable):
    for listKey in g.adjList:
        queue = [listKey]
        reachable[listKey][listKey] = 1
        transitiveUtil(listKey, reachable, queue)

g = Graph(5) 
g.addEdge(0, 1) 
g.addEdge(1, 4) 
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(3, 4)
g.addEdge(3, 0) 

print("Graph (adjacency list): ", g.adjList)
# Matrix showing reachability of each vertex in the graph
reachable = [[0 for i in range(g.V)] for j in range(g.V)]
transitive(reachable)
print("Transitive closure of the graph: ", reachable)
    