# LC #112 — Path Sum (Easy)

# Problem -  Given the root of a binary tree and an integer target, return True if there exists a root-to-leaf path whose sum equals target.

# Example -
#         5
#        / \
#       4   8
#      /   / \
#     11  13   4
#    /  \       \
#   7    2       1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf_node(node):
    if node.left is None and node.right is None:
            return True # Leaf Node
    return False

# Pattern — Post-order decision making:
# check left → check right → decide at current node
def pathSum(root, target):
    if root is None:
        return False  # what should empty node return?

    target -= root.val  # subtract current node value

    if is_leaf_node(root):
        return target == 0  # what should we check here?

    return pathSum(root.left, target) or pathSum(root.right, target)




# ─── Test Cases ───────────────────────────────────────
#         5
#        / \
#       4   8
#      /   / \
#     11  13   4
#    /  \       \
#   7    2       1


root = TreeNode(5)
# left path
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
# right path
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


print(pathSum(root, 22))   # Expected: True
print(pathSum(root, 26))   # Expected: True  (5→8→13)
print(pathSum(root, 100))  # Expected: False
print(pathSum(None, 0))    # Expected: False
