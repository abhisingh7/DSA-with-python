# LeetCode 733 (Easy) - https://leetcode.com/problems/flood-fill/

# Given a 2D grid, a starting cell (sr, sc) and a new color — flood fill all connected cells that share the same original color.

# image = [
#   [1,1,1],
#   [1,1,0],
#   [1,0,1]
# ]
# sr=1, sc=1, color=2
# sr = starting row, sc = starting column
# Output:
# [
#   [2,2,2],
#   [2,2,0],
#   [2,0,1]
# ]

def floodFill(image, sr, sc, color):
    original = image[sr][sc]  # Color we're replacing

    if original == color:
        return image

    def dfs(row, col):
        # Stop conditions
        # 1. out of bounds
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
            return
        # 2. cell is same as original
        if image[row][col] != original:
            return

        # Mark as visited
        image[row][col] = color  # Trick: just overwrite with color

        # Explore all 4 directions
        dfs(row + 1, col)  # down
        dfs(row - 1, col)      # up
        dfs(row, col + 1)      # right
        dfs(row, col - 1)      # left

    dfs(sr, sc)

    return image

# Test

image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))