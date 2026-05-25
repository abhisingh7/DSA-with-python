from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])    # Start with initial node
    visited.add(start)        # Mark it visited immediately

    while queue:
        node = queue.popleft()  # Process first in queue
        print(node)

        for neighbor in graph[node]:
            # Your job: what goes here?
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# test
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
bfs(graph, 1)
