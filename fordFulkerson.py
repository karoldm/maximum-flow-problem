from collections import defaultdict
 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  
        self.row = len(graph)
 
    def BFS(self, s, t, parent):
 
        visited = [False]*(self.row)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:

            u = queue.pop(0)

            for i, value in enumerate(self.graph[u]):
                if visited[i] == False and value > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u
                    if i == t:
                        return True
 
        return False
             
     
    def FordFulkerson(self, source, dest):
 
        parent = [-1]*(self.row)
 
        max_flow = 0
 
        while self.BFS(source, dest, parent) :
 
            path_flow = float("Inf")
            s = dest
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            max_flow +=  path_flow
 
            v = dest
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow