def hasCycle(graph, node, visited, rec_set):
    # Add to both sets
    visited.add(node)
    rec_set.add(node)

    # Check neighbors
    for neighbor in graph[node]:
        # If in rec_set → cycle!
        if neighbor in rec_set:
            return True
        # If not visited → recurse
        if neighbor not in visited:
            if hasCycle(graph, neighbor, visited, rec_set):
                return True

    # Remove from rec_set before backtracking
    rec_set.remove(node)

    return False

# Test

graph = {
    1: [2],
    2: [3],
    3: [1],  # Cycle: 1→2→3→1
    4: []
}

visited = set()
rec_set = set()

for node in graph:
    if node not in visited:
        if hasCycle(graph, node, visited, rec_set):
            print("Cycle detected!")
            break