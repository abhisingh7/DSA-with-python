# LeetCode 200 — Number of Islands
# https://leetcode.com/problems/number-of-islands/

# problem -
# Given a 2D grid of 1s (land) and 0s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# Output = 3
# Island A — top left block of four 1s connected together
# Island B — single 1 in the middle, surrounded by water on all sides
# Island C — two 1s connected horizontally at bottom right


# Time Complexity - O(M x N)
# Space Complexity - O(M x N)
def numIslands(grid):
    count = 0

    def dfs(row, col):
        # Stop conditions
        # 1. out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        # 2. cell is "0"
        if grid[row][col] == '0':
            return

        # Mark as visited
        grid[row][col] = "0"  # Trick: just overwrite with "0"

        # Explore all 4 directions
        dfs(row + 1, col)  # down
        dfs(row - 1, col)      # up
        dfs(row, col + 1)      # right
        dfs(row, col - 1)      # left

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                count += 1        # increment count
                dfs(row, col)        # call dfs

    return count

# Test

grid = [
["1","1","0","0","0"],   #→ DFS from (0,0) floods A, count=1
["1","1","0","0","0"],   #→ all A's marked "0"
["0","0","1","0","0"],   #→ DFS from (2,2) floods B, count=2
["0","0","0","1","1"]    #→ DFS from (3,3) floods C, count=3
]

print(numIslands(grid))
