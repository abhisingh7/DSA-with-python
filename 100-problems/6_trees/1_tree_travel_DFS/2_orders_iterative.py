# In Interview -> iterative exists to avoid stack overflow on very deep trees.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root -> left -> right
def preorder_iterative(root):
    if root is None:
        return

    stack = [root]         # start with root in stack

    while stack:
        node = stack.pop()         # visit the top node
        print(node.val, end=" ")            # Root first

        if node.right:
            stack.append(node.right)   # push right first
        if node.left:
            stack.append(node.left)    # push left second

# left -> root -> right
def inorder_iterative(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)   # keep going left
            current = current.left

        current = stack.pop()       # no more left, print
        print(current.val, end=" ")

        current = current.right     # now go right

# left -> right -> root
def postorder_iterative(root):
    if root is None:
        return

    stack = [root]         # start with root in stack
    result = []
    while stack:
        node = stack.pop()         # visit the top node
        result.append(node.val)            # Append the value

        if node.left:
            stack.append(node.left)    # push left first
        if node.right:
            stack.append(node.right)   # push right second
    print(result[::-1])


# Test the order now
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:")
preorder_iterative(root)   # 1 2 4 5 3
print("\nInorder:")
inorder_iterative(root)     # 4 2 5 1 3
print("\nPostorder:")
postorder_iterative(root) # 4 5 2 3 1
print()  # Add final newline