#         1
#        / \
#       2   3
#      / \
#     4   5

# Note - Some definitions count edges (connections between nodes), some count nodes (number of nodes in the path).
# 1. Counting edges (connections between nodes):
# 1 → 2  (edge 1)
# 2 → 4  (edge 2)

# Height = 2

# 2. Counting nodes (number of nodes in path):
# 1, 2, 4  (3 nodes)

# Height = 3

# LeetCode calls this problem Maximum Depth and counts nodes. So their answer for our tree would be 3.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node):
    if node is None:
        return 0

    left = max_depth(node.left)    # height of left subtree
    right = max_depth(node.right)  # height of right subtree

    return max(left, right) + 1

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
print(max_depth(root1))  # Expected: 3 # counting nodes

# Tracing -
# max_depth(4) = 1
# max_depth(5) = 1
# max_depth(2) = max(1,1) + 1 = 2
# max_depth(3) = 1
# max_depth(1) = max(2,1) + 1 = 3

