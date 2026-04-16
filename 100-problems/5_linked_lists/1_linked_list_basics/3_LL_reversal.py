# Problem - Linked List reversal
# Original => 1->2->3->4->5->None
# Reversed => 5->4->3->2->1->None

# TC - O(n), SC - O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Step 1 — save
        current.next = prev       # Step 2 — flip
        prev = current            # Step 3 — move prev
        current = next_node       # Step 4 — move current
    return prev                   # new head

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

def print_list(head):
    """Print linked list"""
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements) + " -> None")

# ─── TEST CASES ───────────────────────────────────────────

# Test 1 — Normal case
head = build_list([1, 2, 3, 4, 5])
print("Original: ", end="")
print_list(head)
head = reverseList(head)
print("Reversed: ", end="")
print_list(head)
print()

# Test 2 — Single node
head = build_list([1])
print("Original: ", end="")
print_list(head)
head = reverseList(head)
print("Reversed: ", end="")
print_list(head)
print()

# Test 3 — Two nodes
head = build_list([1, 2])
print("Original: ", end="")
print_list(head)
head = reverseList(head)
print("Reversed: ", end="")
print_list(head)
print()

# Test 4 — Empty list
head = build_list([])
print("Original: None")
head = reverseList(head)
print("Reversed: None")

# ─── OUTPUT ───────────────────────────────────────────────
# Original:  1 -> 2 -> 3 -> 4 -> 5 -> None
# Reversed:  5 -> 4 -> 3 -> 2 -> 1 -> None

# Original:  1 -> None
# Reversed:  1 -> None

# Original:  1 -> 2 -> None
# Reversed:  2 -> 1 -> None

# Original: None
# Reversed: None