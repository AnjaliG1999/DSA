#!usr/bin/env python3
from collections import defaultdict
def addEdge(v1, v2):    
        adjList[v1].append(v2)
        # comment the following line to find the number of vertices
        # that are unreachable by any single vertex
        adjList[v2].append(v1)

# Recursive function for DFS
def DFSvisit(vertex, visited):
    visited.append(vertex)
    for v in adjList[vertex]:
        if v not in visited:
            DFSvisit(v, visited)
  
# Count the number of trees present in the given forest
def countTrees():
    visited = []
    count = 0
    for vertex in adjList:
        if vertex not in visited:
            DFSvisit(vertex, visited)
            count += 1
    print(count)

adjList = defaultdict(list)

addEdge(0, 1) 
addEdge(0, 2) 
addEdge(3, 4) 
addEdge(4, 1) 
addEdge(6, 4) 
addEdge(5, 6) 
addEdge(5, 2) 
addEdge(6, 0) 

print(adjList)
countTrees()