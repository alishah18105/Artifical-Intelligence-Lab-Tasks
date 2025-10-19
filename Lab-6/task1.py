from itertools import permutations

# Function to calculate the minimum route
def traveling_salesman(graph, start):
    # List of all cities except the starting city
    cities = list(range(len(graph)))
    cities.remove(start)

    min_path = float('inf')  # Initialize minimum path length
    best_route = []          # To store the best route

    # Try every possible order of visiting cities
    for perm in permutations(cities):
        current_cost = 0
        current_city = start

        # Go through all cities in this permutation
        for next_city in perm:
            current_cost += graph[current_city][next_city]
            current_city = next_city

        # Return to the start city
        current_cost += graph[current_city][start]

        # Check if this route is better
        if current_cost < min_path:
            min_path = current_cost
            best_route = [start] + list(perm) + [start]

    print("Best Route:", ' → '.join(map(str, best_route)))
    print("Minimum cost:", min_path)


# Example Graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Start from city 0
traveling_salesman(graph, 0)
