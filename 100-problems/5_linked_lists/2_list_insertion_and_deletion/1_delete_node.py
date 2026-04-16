# Delete node in a linked list.
# Limitation - you don't have access to head or prev node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ─── SOLUTION ─────────────────────────────────────────────

# TC - O(1), SC - O(1)
def deleteNode(node):
    node.val = node.next.val       # steal next node's value
    node.next = node.next.next     # skip next node

# Note for interview - This trick only works if the node to delete is not the tail. Why?
# Because if it's the tail, node.next is None and node.next.val crashes.

# ─── HELPER FUNCTIONS ─────────────────────────────────────

def build_list(values):
    """Build linked list from Python list"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def get_node_at(head, index):
    """Get node at specific index"""
    current = head
    for _ in range(index):
        current = current.next
    return current

def print_list(head):
    """Print linked list"""
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements) + " -> None")

# ─── TEST CASES ───────────────────────────────────────────

# Test 1 — Delete middle node (index 2, value 3)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" ")
print_list(head)
deleteNode(get_node_at(head, 2))
print("After: ", end=" ")
print_list(head)
print()

# Test 2 — Delete second node (index 1, value 2)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" ")
print_list(head)
deleteNode(get_node_at(head, 1))
print("After: ", end=" ")
print_list(head)
print()

# Test 3 — Delete second to last node (index 3, value 4)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" ")
print_list(head)
deleteNode(get_node_at(head, 3))
print("After: ", end=" ")
print_list(head)
print()

# Test 4 — Two node list, delete first node
head = build_list([1, 2])
print("Before:", end=" ")
print_list(head)
deleteNode(get_node_at(head, 0))
print("After: ", end=" ")
print_list(head)

# ─── OUTPUT ───────────────────────────────────────────────
# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 4 -> 5 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 3 -> 4 -> 5 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 3 -> 5 -> None

# Before: 1 -> 2 -> None
# After:  2 -> None


