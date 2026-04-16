# Problem - A cycle in a linked list means some node's next pointer points back to a previous node instead of None.
# 1 -> 2 -> 3 -> 4 -> 5
#           ↑         |
#           └─────────┘


# 1. Brute Force - using set
# TC -  O(n), SC - O(n)
def isCycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# 2. Floyd's Cycle Detection Algorithm —
# TC - O(n), SC - O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ─── SOLUTION ─────────────────────────────────────────────

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

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

def build_cycle_list(values, cycle_index):
    """Build linked list with a cycle at cycle_index"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_entry = None
    if cycle_index == 0:
        cycle_entry = head
    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == cycle_index:
            cycle_entry = current
    current.next = cycle_entry  # create the cycle
    return head

# ─── TEST CASES ───────────────────────────────────────────

# Test 1 — Cycle exists (tail connects back to index 2)
head = build_cycle_list([1, 2, 3, 4, 5], cycle_index=2)
print(f"Test 1 — Cycle at index 2:     {hasCycle(head)}")  # True

# Test 2 — No cycle
head = build_list([1, 2, 3, 4, 5])
print(f"Test 2 — No cycle:             {hasCycle(head)}")  # False

# Test 3 — Single node, no cycle
head = build_list([1])
print(f"Test 3 — Single node:          {hasCycle(head)}")  # False

# Test 4 — Single node, self loop
head = ListNode(1)
head.next = head
print(f"Test 4 — Self loop:            {hasCycle(head)}")  # True

# Test 5 — Empty list
head = build_list([])
print(f"Test 5 — Empty list:           {hasCycle(head)}")  # False

# Test 6 — Two nodes with cycle
head = build_cycle_list([1, 2], cycle_index=0)
print(f"Test 6 — Two nodes with cycle: {hasCycle(head)}")  # True

# ─── OUTPUT ───────────────────────────────────────────────
# Test 1 — Cycle at index 2:     True
# Test 2 — No cycle:             False
# Test 3 — Single node:          False
# Test 4 — Self loop:            True
# Test 5 — Empty list:           False
# Test 6 — Two nodes with cycle: True