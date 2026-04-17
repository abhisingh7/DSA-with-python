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


# ─── HELPER: Find next group start ────────────────────────
# Returns next_group start if k nodes exist, else None
# TC - O(k), SC - O(1)
def get_next_group(current, k):
    for _ in range(k):
        if current:
            current = current.next
        else:
            return None
    return current


# ─── SOLUTION ─────────────────────────────────────────────
# TC - O(n), SC - O(1)
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while True:
        # Step 1: check k nodes exist + get next group start
        next_group = get_next_group(prev.next, k)
        if next_group is None:
            break

        # Step 2: reverse k nodes inline
        group_start = prev.next
        curr = group_start
        p = None
        while curr != next_group:
            nxt = curr.next
            curr.next = p
            p = curr
            curr = nxt

        # Step 3: rewire pointers
        prev.next = p              # p is new head of reversed group
        group_start.next = next_group  # group_start is now tail
        prev = group_start         # move prev forward

    return dummy.next


# ─── HELPER FUNCTIONS ─────────────────────────────────────

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements) + " -> None")


# ─── TEST CASES ───────────────────────────────────────────

# Test 1 — k=2, even split
inp = build_list([1, 2, 3, 4, 5, 6])
print("Test 1 — k=2, even split:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 2))
print()

# Test 2 — k=3, incomplete last group
inp = build_list([1, 2, 3, 4, 5])
print("Test 2 — k=3, incomplete last group:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 3))
print()

# Test 3 — k=1, no change
inp = build_list([1, 2, 3, 4, 5])
print("Test 3 — k=1, no change:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 1))
print()

# Test 4 — k equals list length
inp = build_list([1, 2, 3, 4, 5])
print("Test 4 — k equals list length:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 5))
print()

# Test 5 — k greater than list length
inp = build_list([1, 2, 3])
print("Test 5 — k greater than list length:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 5))
print()

# Test 6 — Single node
inp = build_list([1])
print("Test 6 — Single node:")
print("Input:  ", end=""); print_list(inp)
print("Output: ", end=""); print_list(reverseKGroup(inp, 2))

# ─── OUTPUT ───────────────────────────────────────────────
# Test 1: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> None
# Test 2: 3 -> 2 -> 1 -> 4 -> 5 -> None
# Test 3: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Test 4: 5 -> 4 -> 3 -> 2 -> 1 -> None
# Test 5: 1 -> 2 -> 3 -> None
# Test 6: 1 -> None