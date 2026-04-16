class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ─── SOLUTION ─────────────────────────────────────────────
# TC - O(n+m) — traverse both lists once
# SC - O(1)   — no extra space, just rewiring existing nodes

def mergeLists(list1, list2):
    l1 = list1 # list1 pointing to head of the list1
    l2 = list2 # list2 pointing to head of the list2

    # dummy node acts as fake head so we always have
    # something to attach to from the very beginning
    dummy = ListNode(0)
    current = dummy

    # compare both lists node by node
    # pick the smaller one and attach it to current
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1   # attach l1 node
            l1 = l1.next        # move l1 forward
        else:
            current.next = l2   # attach l2 node
            l2 = l2.next        # move l2 forward
        current = current.next  # move current forward

    # attach remaining nodes of whichever list is not exhausted
    # if l1 is exhausted, l2 remaining gets attached (even if None)
    if l1:
        current.next = l1
    else:
        current.next = l2

    # dummy.next is the real head of merged list
    return dummy.next

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

# Test 1 — Normal case, alternating values
list1 = build_list([1, 3, 5])
list2 = build_list([2, 4, 6])
print("Test 1 — Alternating values:")
print("List1:  ", end=""); print_list(list1)
print("List2:  ", end=""); print_list(list2)
print("Merged: ", end=""); print_list(mergeLists(list1, list2))
print()

# Test 2 — One list has all smaller values
list1 = build_list([1, 2, 3])
list2 = build_list([4, 5, 6])
print("Test 2 — One list smaller than other:")
print("List1:  ", end=""); print_list(list1)
print("List2:  ", end=""); print_list(list2)
print("Merged: ", end=""); print_list(mergeLists(list1, list2))
print()

# Test 3 — Lists of different lengths
list1 = build_list([1, 5])
list2 = build_list([2, 3, 4, 6])
print("Test 3 — Different lengths:")
print("List1:  ", end=""); print_list(list1)
print("List2:  ", end=""); print_list(list2)
print("Merged: ", end=""); print_list(mergeLists(list1, list2))
print()

# Test 4 — One empty list
list1 = build_list([])
list2 = build_list([1, 2, 3])
print("Test 4 — One empty list:")
print("List1:  None")
print("List2:  ", end=""); print_list(list2)
print("Merged: ", end=""); print_list(mergeLists(list1, list2))
print()

# Test 5 — Both empty lists
list1 = build_list([])
list2 = build_list([])
print("Test 5 — Both empty lists:")
print("List1:  None")
print("List2:  None")
print("Merged: ", end=""); print_list(mergeLists(list1, list2))
print()

# Test 6 — Duplicate values
list1 = build_list([1, 3, 3, 5])
list2 = build_list([2, 3, 4, 6])
print("Test 6 — Duplicate values:")
print("List1:  ", end=""); print_list(list1)
print("List2:  ", end=""); print_list(list2)
print("Merged: ", end=""); print_list(mergeLists(list1, list2))

# ─── OUTPUT ───────────────────────────────────────────────
# Test 1 — Alternating values:
# List1:  1 -> 3 -> 5 -> None
# List2:  2 -> 4 -> 6 -> None
# Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Test 2 — One list smaller than other:
# List1:  1 -> 2 -> 3 -> None
# List2:  4 -> 5 -> 6 -> None
# Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Test 3 — Different lengths:
# List1:  1 -> 5 -> None
# List2:  2 -> 3 -> 4 -> 6 -> None
# Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Test 4 — One empty list:
# List1:  None
# List2:  1 -> 2 -> 3 -> None
# Merged: 1 -> 2 -> 3 -> None

# Test 5 — Both empty lists:
# List1:  None
# List2:  None
# Merged: None

# Test 6 — Duplicate values:
# List1:  1 -> 3 -> 3 -> 5 -> None
# List2:  2 -> 3 -> 4 -> 6 -> None
# Merged: 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5 -> 6 -> None