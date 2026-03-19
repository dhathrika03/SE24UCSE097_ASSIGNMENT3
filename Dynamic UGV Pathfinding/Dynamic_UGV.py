import heapq
import random

# Directions (up, down, left, right)
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0, start))
    
    came_from = {}
    cost = {start: 0}
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            break
        
        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost[current] + 1
                
                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    came_from[(nx, ny)] = current
    
    # Reconstruct path
    path = []
    node = goal
    while node != start:
        if node not in came_from:
            return None
        path.append(node)
        node = came_from[node]
    
    path.append(start)
    path.reverse()
    return path

# Add dynamic obstacles randomly
def update_obstacles(grid, prob=0.1):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if random.random() < prob:
                grid[i][j] = 1  # obstacle

# Print grid
def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Main simulation
def dynamic_pathfinding():
    size = 10
    grid = [[0]*size for _ in range(size)]
    
    start = (0, 0)
    goal = (9, 9)
    
    current = start
    
    while current != goal:
        print("Replanning from:", current)
        
        path = astar(grid, current, goal)
        
        if not path:
            print("No path available!")
            return
        
        # Move one step
        next_step = path[1]
        current = next_step
        
        # Update environment (dynamic obstacles)
        update_obstacles(grid, prob=0.2)
        
        # Ensure start/goal not blocked
        grid[start[0]][start[1]] = 0
        grid[goal[0]][goal[1]] = 0
        
        print_grid(grid, path)
    
    print("Reached Goal!")

# Run
dynamic_pathfinding()