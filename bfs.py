# Function for BFS traversal
def bfs(graph, start_node):
    visited = []  # List to keep track of visited nodes
    queue = [start_node]  # Start with the first node in the queue

    while queue:
        node = queue.pop(0)  # Get the first node from the queue
        if node not in visited:
            print(node, end=" ")  # Print the node
            visited.append(node)  # Mark the node as visited
            queue.extend(graph[node])  # Add neighbors to the queue

# Get user input for the graph
graph = {}
n = int(input("Enter number of nodes: "))  # Number of nodes
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# Get the starting node
print(graph)
start_node = input("Enter starting node: ")


# Perform BFS
print("Breadth-First Search:")
bfs(graph, start_node)

