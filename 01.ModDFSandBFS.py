# -------------------------------
# Tree Structure:
#         A
#       /   \
#      B     C
#    /  \   /  \
#   D    E F    G
#  / \   | / \   \
# H   I  A J  K   L
#         ↑
#       (Cycle back to A from E)
# -------------------------------

# Representing the tree using a dictionary (adjacency list)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['A'],      # Creates a cycle: E → A
    'F': ['J', 'K'],
    'G': ['L']
}

# ------------------------------------------
# Depth-First Search (DFS) - Recursive
# ------------------------------------------
def dfs(tree, node, visited=None):
    """
    Performs a Depth-First Search (DFS) traversal on the tree.
    It visits children deeply before siblings (LIFO).
    Uses recursion and a set to track visited nodes and avoid infinite loops in cycles.
    """
    if visited is None:
        visited = set()
    
    # If node already visited, return to prevent infinite cycle
    if node in visited:
        return

    # Mark node as visited and process it
    visited.add(node)
    print(node, end=' ')

    # Recurse through all the children of the current node
    for child in tree.get(node, []):
        dfs(tree, child, visited)

# Run DFS
print("DFS Traversal (Recursive):")
dfs(tree, 'A')
print()  # Newline after DFS output

# ------------------------------------------
# Breadth-First Search (BFS) - Iterative
# ------------------------------------------
def bfs(tree, start):
    """
    Performs a Breadth-First Search (BFS) traversal on the tree.
    It visits all siblings (same level) before going deeper (FIFO).
    Uses a queue to keep track of the next node to visit.
    """
    visited = {start}     # Start node is marked as visited
    queue = [start]       # Initialize the queue

    while queue:
        node = queue.pop(0)   # Remove the first element
        print(node, end=' ')  # Process the node

        # Visit and enqueue all unvisited children
        for child in tree.get(node, []):
            if child not in visited:
                visited.add(child)
                queue.append(child)

# Run BFS
print("BFS Traversal (Iterative):")
bfs(tree, 'A')
print()  # Newline after BFS output

# ------------------------------------------
# 🧪 Expected Output
# ------------------------------------------
# DFS Traversal (Recursive):
# A B D H I E C F J K G L
#
# BFS Traversal (Iterative):
# A B C D E F G H I J K L
