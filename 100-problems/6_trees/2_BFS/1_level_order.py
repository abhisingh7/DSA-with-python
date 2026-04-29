# LC #102 — Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values — level by level.

#       1
#      /  \
#     2   3
#     / \
#     4   5

# Output: [[1], [2,3], [4,5]]

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Output = [1,2,3,4,5]
def levelOrder(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()      # process front node
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# Output = [[1],[2,3],[4,5]]
def levelOrder2(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for i in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# ─── Test Cases ───────────────────────────────────────

# Test 1: Normal tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(levelOrder(root1))  # Expected: [1,2,3,4,5]
print(levelOrder2(root1))  # Expected: [[1],[2,3],[4,5]]

# Test 2: Empty tree
print(levelOrder2(None))   # Expected: []

# Test 3: Single node
root3 = TreeNode(1)
print(levelOrder2(root3))  # Expected: [[1]]

# Test 4: Left skewed tree
#    1
#   /
#  2
# /
#3
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)
print(levelOrder2(root4))  # Expected: [[1],[2],[3]]