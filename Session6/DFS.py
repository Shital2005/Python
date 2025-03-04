


# Iterative DFS implementation using a stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  # Initialize stack with the start node

    while stack:
        node = stack.pop()  # Pop a node from the stack

        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process the node (e.g., print it)

            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):  # Reverse to explore neighbors in the right order
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Start DFS from node 0
dfs_iterative(graph, 0)
