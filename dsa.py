def dfs_traversal(graph, node, visited=None,path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    visited.add(node)
    path.append(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited, path)
    
    return path
NETWORK_GRAPH={
    'A':['B','C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],     
    'E': ['F'], 
    'F': []      # 
}

start_node = 'A'
print("---------------DFS Traversal--------------")
print(f"starting traversal from node:{start_node} \n")
traversal_path=dfs_traversal(NETWORK_GRAPH,start_node)
print(f"Traversal complete:{traversal_path}")