from os import path
from collections import deque
def bfs_shortest_path(graph,start_node,end_node):
  queue=deque([[start_node]])
  visited={start_node}
  while queue:
    path=queue.popleft()
    current_node=path[-1]
    if current_node==end_node:
      return path
    for neighbor in graph.get(current_node,[]):
      if neighbor not in visited:
        visited.add(neighbor)
        new_path=list(path)
        new_path.append(neighbor)
        queue.append(new_path)
  return None
NETWORK_GRAPH={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':['H','G'],
    'G':['I'],
    'H':[],
}
start='A'
target='I'
shortest_path=bfs_shortest_path(NETWORK_GRAPH,start,target)
if(shortest_path):
  print(f"path:{'->'.join(shortest_path)}")
else:
  print(f"Target{target} unreachable")