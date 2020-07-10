# Graph object creation and methods
class Graph:
    def __init__(self, totalNodes):
        self.matrix = [[0 for x in range(totalNodes)] for y in range(totalNodes)]
        self.totalNodes = totalNodes
        
    def addUndirectedEdge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1
    
    def addDirectedEdge(self, v1, v2):
        self.matrix[v1][v2] = 1

    def removeUndirectedEdge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0
    
    def removeDirectedEdge(self, v1, v2):
        self.matrix[v1][v2] = 0

# Add new edges to the graph
def addEdges(directed):
    numEdges = int(input('Enter the total number of edges: '))
    print('Enter the vertices: ')
    for edge in range(numEdges):
        try:
            #input taken as 2 space-separated integers e.g. 3 4, or 1 5
            v1, v2 = map(int, input().split())
            if directed:                           
                if not g.matrix[v1-1][v2-1]:
                    g.addDirectedEdge(v1-1, v2-1)
                else:
                    print('Edge already exists.')
            else:
                if not g.matrix[v1-1][v2-1]:
                    g.addUndirectedEdge(v1-1, v2-1)
                else:
                    print('Edge already exists.')

        except IndexError:
            print("You are accessing an invalid node!")

# Remove edges from the graph
def removeEdges(directed):
    edges = int(input('Enter number of edges to remove: '))
    print('Enter the vertices: ')
    for edge in range(edges):
        #input taken as 2 space-separated integers e.g. 3 4, or 1 5
        v1, v2 = map(int, input().split())
        try:
            if directed:
                print('Enter the vertices: ')
                for edge in range(edges):
                    v1, v2 = map(int, input().split())
                    if g.matrix[v1-1][v2-1]:
                        g.removeDirectedEdge(v1-1, v2-1)
                    else:
                        print('No such edge.')
            else:   
                if g.matrix[v1-1][v2-1]:
                    g.removeUndirectedEdge(v1-1, v2-1)
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
        print(g.matrix)

except ValueError:
    addOrRemove = None
