# LC #101 — Symmetric Tree (Easy)

# Analogy - mirror image around y axis of current tree should be equal
# For Example -
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric_bt(root):
    def is_mirror(left, right):
        # Case 1: both None
        if left is None and right is None:
            return True

        # Case 2: one is None, other is not
        if left is None or right is None:
            return False

        # Case 3: values don't match
        if left.val != right.val:
            return False

        # Case 4: values match, recurse on mirror pairs
        # Left child of left node matches with right child of right node
        # Right child of left node matches with left child of right node
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)


def inorder(root):
    if root is None:       # base case - empty node
        return
    inorder(root.left)    # Left first
    print(root.val, end=" ")        # then Root
    inorder(root.right)   # then Right

# ─── Test Cases ───────────────────────────────────────

# Test 1: Symmetric tree
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
print(symmetric_bt(root1))  # Expected: True

# Test 2: Non-symmetric tree
#        1
#       / \
#      2   2
#       \   \
#        3   3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)
print(symmetric_bt(root2))  # Expected: False

# Test 3: Single node
print(symmetric_bt(TreeNode(1)))  # Expected: True