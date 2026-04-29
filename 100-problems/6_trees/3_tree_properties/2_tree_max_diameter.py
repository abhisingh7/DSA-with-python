# Diameter of a Binary Tree (LC #543 — Medium).
#         1
#        / \
#       2   3
#      / \
#     4   5

# longest path = 4-2-1-3 or 5-2-1-3

# Note - the tricky part of diameter. The longest path can be anywhere in the tree — not necessarily through the root.
#         1
#        /
#       2
#      / \
#     4   5
#    /
#   6
# Longesth path = 6-4-2-5 (Not including 1 i.e. root node)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pattern — Post-order decision making:
# check left → check right → decide at current node
def diameterOfBinaryTree(root):
    max_diameter = [0]  # using list so we can modify inside helper instead of int variable.
                        # bcoz list is mutable so easy to use same context throughout the program

    def height(node):  # Using max_depth of a tree logic
        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        # compute diameter at this node
        max_diameter[0] = max(max_diameter[0], left + right)

        return max(left, right) + 1  # still returns height

    height(root)
    return max_diameter[0]


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
print(diameterOfBinaryTree(root1))  # Expected: 3

# Test 2: Single node
print(diameterOfBinaryTree(TreeNode(1)))  # Expected: 0

# Test 3: Two nodes
root3 = TreeNode(1)
root3.left = TreeNode(2)
print(diameterOfBinaryTree(root3))  # Expected: 1