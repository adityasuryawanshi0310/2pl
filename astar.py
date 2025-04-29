import heapq

# Heuristic function: Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, heuristic(start, goal), start))
    came_from = {}
    closed_list = set()

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while open_list:
        _, g, _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        closed_list.add(current)

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor in closed_list:
                    continue
                tentative_g = g + 1
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f, tentative_g, heuristic(neighbor, goal), neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return None

# -------- User Input Section --------
# Get grid size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create the grid
print("Enter the grid row by row (0 = walkable, 1 = obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    grid.append(row)

# Get start and goal positions
start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

# Run A* algorithm
path = astar(grid, start, goal)

# Output result
if path:
    print("Path found:", path)
else:
    print("No path found.")
