# Binary Tree Inorder Traversal (Easy) — LC #94
#         1
#          \
#           2
#          /
#         3

# output = [1,3,2]

def inorderTraversalRec(root):
    result = []

    def helper(node): # using helper function so on each recursive call, new result list not get created.
        if node is None:       # base case - empty node
            return
        helper(node.left)    # Left first
        result.append(node.val)        # then Root
        helper(node.right)   # then Right
    helper(root)
    return result

def inorderTraversalIter(root):
    stack = []
    current = root
    result = []
    while current or stack:
        while current:
            stack.append(current)   # keep going left
            current = current.left

        current = stack.pop()       # no more left, print
        result.append(current.val)

        current = current.right     # now go right
    return result