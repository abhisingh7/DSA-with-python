# LC #226 — Invert Binary Tree (Easy)

# Analogy - mirror image around y axis of current tree
# For Example -
#         1               ||         1
#        / \              ||        / \
#       2   3             ||       3   2
#      / \                ||          / \
#     4   5               ||         5   4


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_bt(root):
    # 1. base case
    if root is None:
        return None

    # 2. Swap the nodes
    root.left, root.right = root.right, root.left

    # 3. Recursion on both side
    invert_bt(root.left)
    invert_bt(root.right)

    return root


def inorder(root):
    if root is None:       # base case - empty node
        return
    inorder(root.left)    # Left first
    print(root.val, end=" ")        # then Root
    inorder(root.right)   # then Right

# ─── Test Cases ───────────────────────────────────────

# Test 1:
#        1
#       / \
#      2   3
#     / \
#    4  5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Before invert: ", end="")
inorder(root)          # Expected: 4 2 5 1 3

root = invert_bt(root)

print("\nAfter invert: ", end="")
inorder(root)          # Expected: 3 1 5 2 4
print()