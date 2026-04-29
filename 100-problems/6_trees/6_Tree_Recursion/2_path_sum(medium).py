# LC #113 — Path Sum II (Medium)

# Problem -  Given the root of a binary tree and an integer target,
# Return all root-to-leaf paths where the path sum equals target.

# Example -
#         5
#        / \
#       4   8
#      /   / \
#     11  13   4
#    /  \     /  \
#   7    2   5    1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf_node(node):
    if node.left is None and node.right is None:
            return True # Leaf Node
    return False


# Pattern — Backtracking (append → explore → pop):
def pathSum2(root, target):
    result = []
    path = []

    # append → explore → pop
    def dfs(node, remaining):
        if node is None:
            return

        path.append(node.val)  # add to path

        remaining -= node.val  # subtract current node value

        if is_leaf_node(node) and remaining == 0:
            result.append(path.copy())

        # Recursion calls
        dfs(node.left, remaining)
        dfs(node.right, remaining)

        path.pop()  # remove from path (backtrack)
    dfs(root, target)
    return result




# ─── Test Cases ───────────────────────────────────────
#         5
#        / \
#       4   8
#      /   / \
#     11  13   4
#    /  \     / \
#   7    2   5   1


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
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)


print(pathSum2(root, 22))   # Expected: [[5,4,11,2], [5,8,4,5]]
print(pathSum2(root, 26))   # Expected: [[5, 8, 13]]
print(pathSum2(root, 100))  # Expected: False
print(pathSum2(None, 0))    # Expected: False
