# Validate BST — LC #98 (Medium) — checking if a tree is a valid BST

# Algo -
# for each node, pass down (min, max) range
# if node.val <= min or node.val >= max → invalid
# go left  → max becomes node.val
# go right → min becomes node.val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def validate(node, min_val, max_val):
        if node is None:
            return True  # empty tree is valid
        if node.val <= min_val or node.val >= max_val:
            return False
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))


# ─── Test Cases ───────────────────────────────────────

# Test 1: Valid BST
#        5
#       / \
#      3   8
#     / \
#    1   4
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
print(isValidBST(root1))  # Expected: True

# Test 2: Invalid BST
#        5
#       / \
#      3   8
#     / \
#    1   6
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(8)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(6)
print(isValidBST(root2))  # Expected: False

# Test 3: Single node
print(isValidBST(TreeNode(1)))  # Expected: True