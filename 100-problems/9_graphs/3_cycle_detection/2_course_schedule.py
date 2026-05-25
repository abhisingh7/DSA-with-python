# LeetCode 207 — Course Schedule!
# https://leetcode.com/problems/course-schedule/

# Problem -
# You have n courses. Some courses have prerequisites. Can you finish all courses?
# courses = 2, prerequisites = [[1,0]]
# meaning: to take course 1, you must take course 0 first

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    # Build adjacency list first
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)  # b is prereq for a

    visited = set()
    rec_set = set()

    def dfs(node):
        # 1. If node in rec_set → cycle!
        if node in rec_set:
            return True

        # 2. If node in visited → no cycle, already processed
        if node in visited:
            return False

        # 3. Add to rec_set, add to visited
        rec_set.add(node)
        visited.add(node)

        # 4. Explore neighbors
        # Check neighbors
        for neighbor in graph[node]:
            if dfs(neighbor):  # Let dfs handle all checks
                return True

        # 5. Remove from rec_set before backtracking
        rec_set.remove(node)

        return False

    # Call DFS for every course
    for course in range(numCourses):
        if dfs(course):
            return False

    return True