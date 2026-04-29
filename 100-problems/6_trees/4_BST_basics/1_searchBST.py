# BST - Binary Search Tree (Same Binary Tree but with this below special property)
# Note -
# 1. Left child is always smaller than parent. Right child is always greater than parent.
# 2. all values in left subtree must be less than the parent node.

# LC #700 (Easy) — just finding a node in BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pattern — BST property guided traversal:
# if target < node.val → go left
# if target > node.val → go right
def searchBST(root, target):
    if root is None:
        return False
    if target < root.val:
        return searchBST(root.left, target)
    if target > root.val:
        return searchBST(root.right, target)
    return True

# ─── Test Cases ───────────────────────────────────────

# Test 1: BST
#        5
#       / \
#      3   8
#     / \
#    1  4
target = 4  # find 4
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
print(searchBST(root1, target))  # Expected: True

target = 7 # find 7
print(searchBST(root1, target))  # Expected: False