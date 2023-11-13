def bfs(n, m, e, s):
    # Initialize an empty graph representation
    graph = {}

    # Build the graph from provided edges
    for edge in e:
        # Handling nodes with no connections
        if len(edge) == 1:
            node = edge[0]
            if node not in graph:
                graph[node] = []
            continue

        # Extract nodes from the edge
        node1, node2 = edge

        # Initialize nodes if not already present in the graph
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []

        # Add edges between nodes
        graph[node1].append(node2)
        graph[node2].append(node1)

    print("Graph's adjacent nodes: ", graph)

    # Initialize distances and set starting node's distance to 0
    distances = {node: 0 if node == s else -1 for node in graph}
    queue = [s]

    while queue:
        current_node = queue.pop(0)

        # Explore neighboring nodes
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:
                # Update distances and queue for unvisited neighbors
                distances[neighbor] = distances[current_node] + 4
                queue.append(neighbor)

    # Remove the starting node from the distances
    distances.pop(s)

    result = sorted(list(distances.values()), key=lambda x: (float('inf') if x == -1 else x))
    return result


result = bfs(6, 4, [['a', 'b'], ['a', 'c'], ['b', 'd'], ['d', 'e'], ['f']], 'a')
print('result', result)