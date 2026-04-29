# BST - Binary Search Tree Delete
# Note BST-
# 1. Left child is always smaller than parent. Right child is always greater than parent.
# 2. all values in left subtree must be less than the parent node.

# LC #450 — Delete Node in a BST (Medium)

# 3 cases for BST delete are:
# Case                                Action
# 1. Node is a leaf               Return None
# 2. Node has one child           Return that child
# 3. Node has two children        Replace with inorder successor

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# To Get leftmost node in the right subtree.
# Just to get correct inorder successor create indorder traversal of BST.
# Then next node of the current node in the output will be consider as inorder successor
def inorder_successor(node):
    while node.left is not None:
        node = node.left
    return node

# Pattern — BST property guided traversal:
# if target < node.val → go left
# if target > node.val → go right
def deleteBST(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = deleteBST(root.left, key)
    elif key > root.val:
        root.right = deleteBST(root.right, key)
    else:
        # found the node to delete!
        # handle 3 cases here
        if root.left and root.right:
            successor = inorder_successor(root.right)  # find successor
            root.val = successor.val  # copy successor value
            root.right = deleteBST(root.right, successor.val) # delete successor from right subtree recursively
        elif root.left or root.right:
            return (root.left or root.right)
        else:
            return None

    return root


def inorder(root):
    if root is None:       # base case - empty node
        return
    inorder(root.left)    # Left first
    print(root.val, end=" ")        # then Root
    inorder(root.right)   # then Right


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

# Delete leaf node (1)
root = deleteBST(root, 1)
inorder(root)   # Expected: 3 4 5 8
print()

# Delete node with ONE child (3 has only right child 4 now)
root = deleteBST(root, 3)
inorder(root)   # Expected: 4 5 8
print()

# Delete root (5) - Two child
root = deleteBST(root, 5)
inorder(root)   # Expected: 4 8
print()


# Delete node with TWO children (3 has 1 and 4)
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(8)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(4)

root2 = deleteBST(root2, 3)
inorder(root2)   # Expected: 1 4 5 8
print()