def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()         # Fresh set for each new traversal
    # Mark current node visited
    visited.add(node)
    # Print current node
    print(node)
    # Go through neighbors
    # If neighbor not visited, recurse
    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited)

# test
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
dfs(graph, 1)
