#!usr/bin/env python3

# Graph object creation and methods
class Graph:
	def __init__(self, nodes):
		self.adjList = {}
		self.V = nodes
		for v in range(nodes):
			self.addVertices(v)

	def addEdge(self, v1, v2):
		'''
		Add directed edge to the graph

		:param: v1, v2: int, vertices- edge added v1 -> v2
		:rtype: None
		'''

		self.adjList[v1].append(v2)
		
	def addVertices(self, v):
		'''
		Initialize empty graph with v vertices

		:param: v: int, total no. of vertices in the graph
		:rtype: None
		'''

		self.adjList[v] = []
		
	def dfs(self, vertex, visited, stack):
		'''
		Depth First Search approach for the given vertex

		:param: v: int, total no. of vertices in the graph
		:rtype: None
		'''
		
		visited[vertex] = True
		for v in self.adjList[vertex]:
			if visited[v] == False:
				self.dfs(v, visited, stack)
		stack.insert(0, vertex)

	def topologicalSort(self):
		'''
		Traverse the graph by tropological sort

		:param: None
		:rtype: List
		'''
		
		visited = [False for i in self.adjList]
		stack = []
		for v in range(self.V):
			if visited[v] == False:
				self.dfs(v, visited, stack)
		return stack
		

g = Graph(6)

g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0) 
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.adjList)
print(g.topologicalSort())