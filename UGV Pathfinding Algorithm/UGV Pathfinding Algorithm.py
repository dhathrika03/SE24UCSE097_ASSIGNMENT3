import numpy as np
import heapq
import random
import time

# Grid size
SIZE = 70

# Obstacle density levels
def generate_grid(density):
    grid = np.zeros((SIZE, SIZE))
    
    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < density:
                grid[i][j] = 1  # obstacle
                
    return grid

# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal):
    start_time = time.time()

    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()

            end_time = time.time()

            return path, len(path), end_time - start_time

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if (0 <= neighbor[0] < SIZE and 
                0 <= neighbor[1] < SIZE and 
                grid[neighbor] == 0):

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None, 0, 0

# MAIN PROGRAM
if __name__ == "__main__":
    
    # Choose density: 0.1 (low), 0.3 (medium), 0.5 (high)
    density = float(input("Enter obstacle density (0.1 / 0.3 / 0.5): "))
    
    grid = generate_grid(density)

    start = (0, 0)
    goal = (69, 69)

    grid[start] = 0
    grid[goal] = 0

    path, length, time_taken = astar(grid, start, goal)

    if path:
        print("\nPath found!")
        print("Path length:", length)
        print("Time taken:", time_taken, "seconds")

        # Show path on grid
        for (x, y) in path:
            grid[x][y] = 2

        print("\nGrid Representation:")
        print("0 = free, 1 = obstacle, 2 = path\n")
        print(grid)

    else:
        print("\nNo path found!")