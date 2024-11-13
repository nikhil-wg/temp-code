# Function for DFS traversal
def dfs(graph, start, visited):
    visited.add(start)  # Mark the current node as visited
    print(start)  # Process the current node (e.g., print it)

    # Recursively visit all unvisited neighbors in sorted order (optional)
    for neighbor in sorted(graph[start]):  # Sort ensures consistent order
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Dynamically input the graph
graph = {}
n = int(input("Enter number of nodes: "))  # Number of nodes

# Input for graph structure
for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors  # Use a list to maintain order

# Perform DFS for the entire graph
visited = set()  # Global visited set
print("Depth-First Search:")
for node in graph:
    if node not in visited:
        dfs(graph, node, visited)
