def bfs(graph, start):
    visited = set()
    queue = [start]  
    visited.add(start)

    while queue:
        node = queue.pop(0) 
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
        'A': ['C', 'B'],  
        'B': ['D', 'A'],  
        'C': ['F', 'A'],  
        'D': ['B', 'E'],  
        'E': ['D'],       
        'F': ['C', 'G'],  
        'G': ['F'],       
        'H': []           
}
 
bfs(graph, 'A')