from collections import defaultdict


def all_topological_sorts(graph):
    def dfs(node):
        nonlocal visited, result
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        visited[node] = False
        result.append(node)

    def is_valid_topo_order(order):
        visited = set()
        for node in order:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    return False
        return True

    result = []
    visited = defaultdict(bool)

    for node in graph:
        if not visited[node]:
            dfs(node)

    all_orders = [result[::-1] for result in result]

    valid_orders = [
        order for order in all_orders if is_valid_topo_order(order)]

    return valid_orders


# Given directed edges
edges = [(1, 2), (2, 3), (1, 4), (4, 5), (5, 3), (4, 6), (6, 5)]

# Build graph
graph = defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])

# Find all possible topological orders
possible_orders = all_topological_sorts(graph)

# Print all possible topological orders
for order in possible_orders:
    print(" -> ".join(map(str, order)))
