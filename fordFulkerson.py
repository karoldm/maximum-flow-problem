from collections import defaultdict
 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  
        self.row = len(graph)
 
    # Algoritmo de busca para achar um caminho do nó inicial até o final
    def BFS(self, s, t, parent):
        # Array para controlar os vértices visitados
        visited = [False]*(self.row)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
            u = queue.pop(0)
            # Iterando sobre todos os vértices adjacentes do vértice u
            for i, value in enumerate(self.graph[u]):
                # Verifica se o vértice não foi visitado e tem capacidade residual > 0 
                # Ou seja, ainda pode ter dados passando por esse vértice
                if visited[i] == False and value > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u
                    if i == t:
                        return True
 
        return False
             
     
    def FordFulkerson(self, source, dest):
 
        parent = [-1]*(self.row)
 
        # Fluxo máximo inicial é zero
        max_flow = 0
 
        # Enquanto existirem caminhos do nó inicial até o final
        while self.BFS(source, dest, parent):
 
            path_flow = float("Inf")
            s = dest
            while(s !=  source):
                # Achando a capacidade residual mínima
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Somando ao fluxo final a capacidade residual mínima encontrada
            max_flow += path_flow
 
            v = dest
            # Atualizando o fluxo e a capacidade residual mínima de cada aresta do caminho atual
            while(v != source):
                u = parent[v]
                # Subtraindo da capacidade residual mínima
                self.graph[u][v] -= path_flow
                # Somando ao fluxo atual passando pela aresta
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow