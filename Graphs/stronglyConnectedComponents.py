#!usr/bin/env python3

# Graph object creation and methods
class Graph:
    def __init__(self, nodes):
        self.adjList = {}
        self.V = nodes
        for v in range(nodes):
            self.addVertices(v)

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)
        
    def addVertices(self, v):
        self.adjList[v] = []
        
    def getTranspose(self):
        '''
        Get transpose of the original graph
        :param: self: Object
        :rtype: Object, transpose graph
        '''
        gt = Graph(self.V)
        for src in self.adjList:
            for dest in self.adjList[src]:
                gt.addEdge(dest, src)
        
        return gt
        
    def dfs(self, vertex, visited):
        '''
        Find DFS of the graph
        :param: self: Object
                vertex: int
                visited: List
        :rtype: None
        '''
        visited[vertex] = True
        print(vertex, end=' ')
        for v in self.adjList[vertex]:
            if visited[v] == False:
                self.dfs(v, visited)
    
    def fillStack(self, vertex, visited, stack):
        '''
        Find the order of traversal of vertices
        :param: self: Object
                vertex: int
                visited: List
                stack: List
        :rtype: None
        '''
        visited[vertex] = True        
        for v in self.adjList[vertex]:
            if visited[v] == False:
                self.fillStack(v, visited, stack)
        stack.append(vertex)

    def findSCC(self):
        '''
        Identify and print the strongly connected components of the graph
        :param: self: Object
                vertex: int
                visited: List
                stack: List
        :rtype: None
        '''
        visited = [False for i in range(self.V)]
        stack = []
        for v in self.adjList:
            if visited[v] == False:
                self.fillStack(v, visited, stack)
        
        gt = self.getTranspose()
        visited = [False for i in range(self.V)]

        print('Strongly Connected components:')
        while stack:
            v = stack.pop()
            if visited[v] == False:
                gt.dfs(v, visited)
                print()

g = Graph(8)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 0)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(6, 7)
print('Graph:', g.adjList)
g.findSCC()