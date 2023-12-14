def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            traversal_order.append(node)
            visited.add(node)
            neighbors = sorted(graph[node] - visited, reverse=True)
            stack.extend(neighbors)
    return traversal_order

if __name__ == '__main__':
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F', 'G'},
        'D': {'B'},
        'E': {'B', 'H'},
        'F': {'C'},
        'G': {'C'},
        'H': {'E'}
    }

    print(dfs(graph, 'A'))


