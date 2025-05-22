# Граф в виде словаря смежности
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS с вычислением длины пути
def dfs_with_path_length(graph, start, visited=None, path_lengths=None, depth=0):
    if visited is None:
        visited = set()
    if path_lengths is None:
        path_lengths = {}

    visited.add(start)
    path_lengths[start] = depth
    print(f"{start} (длина пути: {depth})")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_with_path_length(graph, neighbor, visited, path_lengths, depth + 1)

    return path_lengths

# Запуск
path_lengths = dfs_with_path_length(graph, 'A')
print("\nДлины путей до вершин:", path_lengths)

