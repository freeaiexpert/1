# 1. Initialize graph with vertex names
vertices = ['A', 'B', 'C', 'D']
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

num_colors = 3
colors = {}  # Dictionary to hold color of each vertex

# 2. Function to check if it's safe to color a vertex
def is_safe(vertex, color):
    for neighbor in graph[vertex]:
        if colors.get(neighbor) == color:
            return False
    return True

# 3. Recursive function to solve coloring
def solve(index):
    if index == len(vertices):
        return True  # All vertices are colored

    vertex = vertices[index]
    for color in range(1, num_colors + 1):
        if is_safe(vertex, color):
            colors[vertex] = color  # Assign color
            if solve(index + 1):    # Recurse
                return True
            colors[vertex] = 0      # Backtrack

    return False

# 4. Start solving from the first vertex
for v in vertices:
    colors[v] = 0  # Initialize all colors to 0

if solve(0):
    print("Coloring is possible:")
    for v in vertices:
        print(f"{v}: Color {colors[v]}")
else:
    print("No valid coloring found.")
