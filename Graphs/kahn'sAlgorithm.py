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
		
def countDegree():
	'''
	Count the in degree and out degree of each vertex of the graph

	:param: None
	:rtype: List
	'''

	outDegree = [0 for i in range(g.V)]
	inDegree = [0 for i in range(g.V)]
	for v in g.adjList:
		outDegree[v] = len(g.adjList[v])
		for u in g.adjList[v]:
			inDegree[u] += 1
	# print('inDegree: {}'.format(inDegree))
	# print('outDegree: {}'.format(outDegree))
	return inDegree

def topSort():
	'''
	Topological sort of the graph using Kahn's algorithm

	:param: None
	:rtype: None
	'''

	inDegree = countDegree()
	queue = []

	# add all vertices with indegree=0 to the queue
	for v in g.adjList:
		if inDegree[v] == 0:
			queue.append(v)

	topOrder = []
	count = 0
	while queue:
		vertex = queue.pop(0)
		topOrder.append(vertex)

		# decrement indegree of vertices, when 0: add them to queue
		for v in g.adjList[vertex]:
			inDegree[v] -= 1
			if inDegree[v] == 0:
				queue.append(v)
		count += 1
	
	# no topological sort possible in a cyclic graph
	if count != g.V:
		print("Cycle present in the graph")
	else:
		print('Traversal order: {}'.format(topOrder))

g = Graph(6)

g.addEdge(5, 2)
# g.addEdge(1, 1)
g.addEdge(5, 0)
g.addEdge(4, 0) 
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print('Graph: {}'.format(g.adjList))
topSort()