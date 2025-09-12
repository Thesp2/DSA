def graphColoring(V, edges, m):
    
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * V 

    def is_safe(node, col):
        for nei in graph[node]:
            if colors[nei] == col: 
                return False
        return True

    def backtrack(node):
        
        if node == V:
            return True

        for col in range(1, m + 1):
            if is_safe(node, col):
                colors[node] = col
                if backtrack(node + 1):
                    return True
                colors[node] = 0  

        return False

    return backtrack(0)
V = 4 
edges = [[0, 1], [1, 3], [2, 3], [3, 0], [0, 2]] 
m = 3
print(graphColoring(V, edges, m))