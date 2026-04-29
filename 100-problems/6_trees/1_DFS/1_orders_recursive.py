class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root -> left -> right
def preorder(root):
    if root is None:       # base case - empty node
        return
    print(root.val, end=" ")         # Root first
    preorder(root.left)    # then Left
    preorder(root.right)   # then Right


# left -> root -> right
def inorder(root):
    if root is None:       # base case - empty node
        return
    inorder(root.left)    # Left first
    print(root.val, end=" ")        # then Root
    inorder(root.right)   # then Right

# left -> right -> root
def postorder(root):
    if root is None:       # base case - empty node
        return
    postorder(root.left)    # Left first
    postorder(root.right)   # then Right
    print(root.val, end=" ")         # then Root


# Test the order now
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:")
preorder(root)   # 1 2 4 5 3
print("\nInorder:")
inorder(root)     # 4 2 5 1 3
print("\nPostorder:")
postorder(root) # 4 5 2 3 1
print()  # Add final newline