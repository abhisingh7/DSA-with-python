# LC #103 — Zigzag Level Order Traversal.
# Input -
#       1
#      /  \
#     2   3
#    / \
#   4   5

# Output = [[1], [3,2], [4,5]]

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    if root is None:
        return []

    queue = deque([root])
    result = []
    # level_number = 0
    flag = False

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

        #  odd level, reverse it
        # if level_number % 2 == 1:  # odd level
        #     level = level[::-1]    # reverse it

        if flag:
            level = level[::-1]

        result.append(level)

        # level_number += 1
        flag = not flag

    return result

# ─── Test Cases ───────────────────────────────────────

# Test 1: Normal tree
#        1
#       / \
#      2   3
#     / \
#    4   5
# Test 1: Normal tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(zigzagLevelOrder(root1))  # [[1],[3,2],[4,5]]

# Test 2: Empty tree
print(zigzagLevelOrder(None))   # []

# Test 3: Single node
print(zigzagLevelOrder(TreeNode(1)))  # [[1]]