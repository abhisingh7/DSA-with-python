# Kahn's Algo

# 1. Calculate in-degree for every node
# 2. Add all nodes with in-degree 0 to queue
# 3. While queue is not empty:
#    a. Pop node from queue
#    b. Add to result
#    c. For each neighbor:
#       - Reduce their in-degree by 1
#       - If in-degree becomes 0 → add to queue
# 4. If result contains all nodes → valid topo sort
#    If not → cycle exists!

# Pattern for Kahn's algo
# You naturally followed this process:

# 1. Pick nodes with no incoming edges first
# 2. Remove them from graph
# 3. See which nodes become "free" next
# 4. Repeat

# Note - Topological sort is not unique. Multiple valid orderings can exist for the same graph.

# Kahn's Algorithm is essentially BFS on a directed graph where:

# 1. Queue starts with all nodes whose in-degree = 0
# 2. Process node → reduce neighbors' in-degree by 1
# 3. If neighbor's in-degree becomes 0 → add to queue

# Key Lesson -
# A node becomes "free" only when all its incoming edges are removed.
# This is tracked using something called in-degree — the count of incoming edges for each node.

# original graph -
# 5 → 0 ← 4
# ↓       ↓
# 2 → 3 → 1

# Topological order -
# 5 → 4 → 0 → 2 → 3 → 1

# Node 0 → in-degree = 2 (from 5 and 4)
# Node 2 → in-degree = 1 (from 5)
# Node 1 → in-degree = 2 (from 3 and 4)

from collections import deque


def calculate_in_degree(graph):
    in_degree = {node: 0 for node in graph}  # Start everyone at 0

    for _, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    return in_degree


def topological_sort(graph):
    # Step 1: Calculate in-degrees
    in_degree = calculate_in_degree(graph)

    # Step 2: Add all nodes with in-degree 0 to queue
    queue = deque([node for node in graph if in_degree[node] == 0])

    result = []

    # Step 3: BFS
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            # Reduce their in-degree by 1
            in_degree[neighbor] -= 1
            # If in-degree becomes 0 → add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else "cycle detected!"


# Test
graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}

# print(calculate_in_degree(graph))
print(topological_sort(graph))
