# LC #236 — Lowest Common Ancestor of a Binary Tree (Medium)
# Note - Special Rule - A node can be a descendant(Ancestor) of itself.
# For Example -

#         1
#        / \
#       2   3
#      / \
#     4   5

# LCA of 4 and 5 is 2 (Same Subtree)
# LCA of 4 and 3 is 1 (Different Subtree)
# LCA of 4 and 2 is 2 (Special Case)

# Algo -
# if node is None → return None
# if node is p or q → return node
# check left subtree
# check right subtree
# if both left and right returned something → return current node
# if only left returned something → return left
# if only right returned something → return right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pattern — Post-order decision making:
# check left → check right → decide at current node
def LCA(root, p, q):
    if root is None:
        return None
    if root is p or root is q:
        return root


    left = LCA(root.left, p, q)
    right = LCA(root.right, p ,q)

    if left and right:
        return root
    return left or right


# ─── Test Cases ───────────────────────────────────────
#        1
#       / \
#      2   3
#     / \
#    4   5

# Test 1: LCA(4,5) = 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
p = root.left.left
q = root.left.right
print(LCA(root, p, q).val) # Expected 2

# Test 2: LCA(4, 3) = 1
print(LCA(root, root.left.left, root.right).val)  # Expected: 1

# Test 3: LCA(2, 4) = 2
print(LCA(root, root.left, root.left.left).val)  # Expected: 2

