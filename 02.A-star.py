# Function to print the 3x3 puzzle board
def print_board(state):
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            print("_" if value == -1 else value, end=" ")
        print()
    print()

# Manhattan distance heuristic function
def manhattan_distance(current, goal):
    distance = 0
    for num in range(1, 9):  # Skip -1 (blank tile)
        curr_index = current.index(num)
        goal_index = goal.index(num)
        x1, y1 = curr_index // 3, curr_index % 3
        x2, y2 = goal_index // 3, goal_index % 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate all possible next states
def get_neighbors(state):
    neighbors = []
    idx = state.index(-1)
    row, col = idx // 3, idx % 3

    # Left, Right, Up, Down directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(new_state)
    return neighbors

# A* Search Algorithm
def a_star(start, goal):
    from heapq import heappush, heappop

    open_list = []
    heappush(open_list, (manhattan_distance(start, goal), 0, start, []))  # (f, g, state, path)

    visited = set()

    while open_list:
        f, g, current, path = heappop(open_list)

        if tuple(current) in visited:
            continue
        visited.add(tuple(current))

        if current == goal:
            print(f"\n🎉 Puzzle solved in {g} moves!\n")
            for i, step in enumerate(path + [current]):
                print(f"Step {i}:")
                print_board(step)
            return

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                heappush(open_list, (
                    g + 1 + manhattan_distance(neighbor, goal),
                    g + 1,
                    neighbor,
                    path + [current]
                ))

    print("❌ No solution found.")

# Helper function for safe integer input
def safe_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number (e.g., 1, 2, -1).")

# Main driver function
def main():
    print("Enter start state (-1 for empty tile):")
    start = [safe_input(f"Enter tile {i+1}/9: ") for i in range(9)]

    print("\nEnter goal state (-1 for empty tile):")
    goal = [safe_input(f"Enter tile {i+1}/9: ") for i in range(9)]

    print("\n🟢 Start State:")
    print_board(start)

    print("🏁 Goal State:")
    print_board(goal)

    a_star(start, goal)

if __name__ == "__main__":
    main()


# ---------------------------------------------
# 📥 Sample Input:
# (You will be prompted to enter one value at a time)

# Enter start state (-1 for empty tile):
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# -1
# 8

# Enter goal state (-1 for empty tile):
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# -1

# ---------------------------------------------
# 📤 Expected Output:

# 🟢 Start State:
# 1 2 3 
# 4 5 6 
# 7 _ 8 

# 🏁 Goal State:
# 1 2 3 
# 4 5 6 
# 7 8 _ 

# 🎉 Puzzle solved in 1 moves!

# Step 0:
# 1 2 3 
# 4 5 6 
# 7 _ 8 

# Step 1:
# 1 2 3 
# 4 5 6 
# 7 8 _ 
