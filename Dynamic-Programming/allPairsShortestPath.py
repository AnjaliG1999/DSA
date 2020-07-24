INF  = float('inf')
  
# Floyd Warshall Algorithm
def floydWarshall(graph): 
    dist = graph
    
    for mid in range(V):
        for v1 in range(V):
            for v2 in range(V):
                dist[v1][v2] = min(dist[v1][v2], dist[v1][mid] + dist[mid][v2])
    print(dist)
    
graph = [
    [0,5,INF,10], 
    [INF,0,3,INF], 
    [INF, INF, 0,   1], 
    [INF, INF, INF, 0] 
] 

V = len(graph) 
floydWarshall(graph)
