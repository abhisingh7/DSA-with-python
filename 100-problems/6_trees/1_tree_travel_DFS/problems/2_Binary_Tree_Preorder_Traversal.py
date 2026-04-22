# Binary Tree Preorder Traversal (Easy) — LC #144
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#         1
#          \
#           2
#          /
#         3

# Output: [1, 2, 3]

def preorderTraversalRec(root):
    result = []

    def helper(node):
        if node is None:       # base case - empty node
            return
        result.append(node.val)         # Root first
        helper(node.left)    # then Left
        helper(node.right)   # then Right
    helper(root)
    return result


def preorderTraversalIter(root):
    if root is None:
        return

    stack = [root]         # start with root in stack
    result = []

    while stack:
        node = stack.pop()         # visit the top node
        result.append(node.val)            # Root first

        if node.right:
            stack.append(node.right)   # push right first
        if node.left:
            stack.append(node.left)    # push left second
    return result