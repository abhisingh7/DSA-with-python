# LeetCode 210 — Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

# Same as Course Schedule I — but instead of returning True/False, return the actual order of courses!

# This is literally Kahn's Algorithm you just built. The only differences are:

# Build graph from prerequisites
# Return result if no cycle, else return []

from collections import deque, defaultdict


def calculate_in_degree(graph):
    in_degree = {node: 0 for node in graph}  # Start everyone at 0

    for _, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    return in_degree


def findOrder(numCourses, prerequisites):
    # Step 1: Build graph
    graph = defaultdict(list)

    # Initialize ALL courses first
    for i in range(numCourses):
        graph[i]  # Creates empty list for every course

    for a, b in prerequisites:
        graph[b].append(a)  # b is prereq for a

    # Step 2: Calculate in-degrees
    in_degree = calculate_in_degree(graph)

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    # Step 3: Kahn's BFS
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            # Reduce their in-degree by 1
            in_degree[neighbor] -= 1
            # If in-degree becomes 0 → add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Return result or []
    return result if len(result) == numCourses else []


# Test
numCourses = 4
prerequisites = [[1,0], [2,1], [3,2]]
print(findOrder(numCourses, prerequisites))

numCourses = 3
prerequisites = [[1,0], [0,2], [2,1]]
print(findOrder(numCourses, prerequisites))