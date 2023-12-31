from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            traversal_order.append(node)
            visited.add(node)
            neighbors = sorted(graph[node] - visited)
            print(neighbors)
            queue.extend(neighbors)
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
    print(bfs(graph, 'A'))
