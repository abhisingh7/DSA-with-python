# Reverse Nodes in k-Group  - This is a Hard problem and one of the most frequently asked in MAANG interviews.
# It combines everything you've learned — reversal, pointer manipulation, and recursion.

# Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, k = 2
# Output: 2 -> 1 -> 4 -> 3 -> 5 -> None

# Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, k = 3
# Output: 3 -> 2 -> 1 -> 4 -> 5 -> None
#                        ↑
#                only 2 nodes left, k=3
#                so leave them as is


# Overall TC - O(n), SC - O(1) — optimal! 🎯

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# check next k node exists or not?
# TC - O(k) per call, SC - O(1)
def k_nodes_exist(current, k):
    for _ in range(k):
        if current:
            current = current.next
        else:
            return False
    return True

# reverse the group of k nodes
# TC - O(k) per call, SC - O(1)
def reverse_group(start, end):
    prev = None
    current = start
    while current != end:    # stop at next_group
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev              # new head of reversed group

# Main function
# TC - O(n), SC - O(1)
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while k_nodes_exist(prev.next, k):           # check k nodes exist
        group_start = prev.next
        next_group = group_start # where does next group start?
        for _ in range(k):
            next_group = next_group.next

        # reverse k nodes starting from group_start
        new_head = reverse_group(group_start, next_group)
        # attach reversed group back
        prev.next = new_head  # connect prev to new head
        group_start.next = next_group # connect tail to next group
        prev = group_start       # move prev forward

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

# Test 1 — Normal case, k = 2
input = build_list([1, 2, 3, 4, 5, 6])
k = 2
print("Test 1 — ")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))
print()

# Test 2 — k=3
input = build_list([1, 2, 3, 4, 5])
k = 3
print("Test 2 — k=3, incomplete last group:")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))
print()

# Test 3 — k=1 (no change)
input = build_list([1, 2, 3, 4, 5])
k = 1
print("Test 3 — k=1, no change:")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))
print()

# Test 4 — k equals list length
input = build_list([1, 2, 3, 4, 5])
k = 5
print("Test 4 — k equals list length:")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))
print()

# Test 5 — Single node
input = build_list([1])
k = 2
print("Test 5 — Single node:")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))

# Test 6 — k greater than list length
input = build_list([1, 2, 3])
k = 5
print("Test 6 — k greater than list length:")
print("Input:  ", end=""); print_list(input)
print("Output: ", end=""); print_list(reverseKGroup(input, k))

# ─── OUTPUT ───────────────────────────────────────────────
# Test 1: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> None
# Test 2: 3 -> 2 -> 1 -> 4 -> 5 -> None  (4,5 unchanged)
# Test 3: 1 -> 2 -> 3 -> 4 -> 5 -> None  (no change)
# Test 4: 5 -> 4 -> 3 -> 2 -> 1 -> None  (full reversal)
# Test 5: 1 -> None                       (no change)
# Test 6: 1 -> 2 -> 3 -> None (No Change)