def dijkstra(graph, V, source):
    # Step 1: Initialize distances and visited array
    dist = [float('inf')] * V
    visited = [False] * V

    dist[source] = 0

    # Step 2: Repeat V times
    for _ in range(V):
        
        # Find vertex with minimum distance not visited
        u = -1
        min_dist = float('inf')
        
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        # If no reachable vertex remains
        if u == -1:
            break

        # Mark u as visited
        visited[u] = True

        # Step 3: Relax neighbors
        for neighbor in graph[u]:
            v = neighbor[0]
            weight = neighbor[1]

            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist


# Example graph (adjacency list as dictionary)
graph_dict = {
    0: [(1,1), (2,4)],
    1: [(2,2), (3,5)],
    2: [(3,1)],
    3: []
}

# Number of vertices
V = len(graph_dict)

# Convert dictionary → list of lists
graph = []
for i in range(V):
    graph.append(graph_dict[i])

# Source node
source = 0

# Run Dijkstra
result = dijkstra(graph, V, source)

# Output
print("Shortest distances from source:", result)