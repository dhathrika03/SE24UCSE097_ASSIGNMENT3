import heapq

# Graph: City -> [(Neighbor, Distance)]
graph = {
    "Delhi": [("Agra", 233), ("Jaipur", 280), ("Chandigarh", 250)],
    "Agra": [("Delhi", 233), ("Jaipur", 240), ("Lucknow", 335)],
    "Jaipur": [("Delhi", 280), ("Agra", 240), ("Mumbai", 1150)],
    "Chandigarh": [("Delhi", 250), ("Shimla", 120)],
    "Shimla": [("Chandigarh", 120)],
    "Lucknow": [("Agra", 335), ("Varanasi", 320)],
    "Varanasi": [("Lucknow", 320), ("Kolkata", 680)],
    "Kolkata": [("Varanasi", 680), ("Bhubaneswar", 440)],
    "Bhubaneswar": [("Kolkata", 440), ("Hyderabad", 1050)],
    "Hyderabad": [("Bhubaneswar", 1050), ("Bangalore", 570), ("Mumbai", 710)],
    "Mumbai": [("Jaipur", 1150), ("Hyderabad", 710), ("Pune", 150)],
    "Pune": [("Mumbai", 150), ("Bangalore", 840)],
    "Bangalore": [("Hyderabad", 570), ("Pune", 840), ("Chennai", 350)],
    "Chennai": [("Bangalore", 350)]
}

def dijkstra(graph, start):
    # Priority queue: (cost, city)
    pq = [(0, start)]
    
    # Distance dictionary
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    
    # Previous nodes (for path reconstruction)
    previous = {city: None for city in graph}
    
    while pq:
        current_cost, current_city = heapq.heappop(pq)
        
        # Skip if we already found a better path
        if current_cost > distances[current_city]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_city]:
            distance = current_cost + weight
            
            # If shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous


def get_path(previous, start, end):
    path = []
    current = end
    
    while current:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    if path[0] == start:
        return path
    return []


# 🔹 Run the algorithm
start_city = "Delhi"
distances, previous = dijkstra(graph, start_city)

# 🔹 Print results
print(f"Shortest distances from {start_city}:\n")
for city in distances:
    print(f"{city}: {distances[city]} km")

# 🔹 Example path
end_city = "Chennai"
path = get_path(previous, start_city, end_city)

print(f"\nShortest path from {start_city} to {end_city}:")
print(" -> ".join(path))
print(f"Total distance: {distances[end_city]} km")