# BST - Binary Search Tree Insert
# Note BST-
# 1. Left child is always smaller than parent. Right child is always greater than parent.
# 2. all values in left subtree must be less than the parent node.

# LC #701 — Insert into a Binary Search Tree (Medium).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left -> root -> right
def inorder(root):
    if root is None:       # base case - empty node
        return
    inorder(root.left)    # Left first
    print(root.val, end=" ")        # then Root
    inorder(root.right)   # then Right

# Pattern — BST property guided traversal:
# if target < node.val → go left
# if target > node.val → go right
def insertBST(root, target):
    if root is None:
        return TreeNode(target)
    if target < root.val:
        root.left =  insertBST(root.left, target)
    if target > root.val:
        root.right = insertBST(root.right, target)
    return root


# ─── Test Cases ───────────────────────────────────────

# Test 1: BST
#        5
#       / \
#      3   8
#     / \
#    1  4
target = 4  # find 4
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
# Insert 6
root = insertBST(root, 6)
inorder(root)  # Expected: [1,3,4,5,6,8] (sorted!)
print()

# Insert 2
root = insertBST(root, 2)
inorder(root)  # Expected: [1,2,3,4,5,6,8]
print()