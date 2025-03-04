from collections import deque

def bfs(graph, start):
    # Create a set to keep track of visited nodes
    visited = set()
    
    # Create a queue for BFS
    queue = deque([start])
    
    # Mark the starting node as visited
    visited.add(start)
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(vertex, end=" ")  # You can process the node here (e.g., print it)
        
        # Visit all the neighbors of the current node
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Starting BFS from node 0
bfs(graph, 0)
