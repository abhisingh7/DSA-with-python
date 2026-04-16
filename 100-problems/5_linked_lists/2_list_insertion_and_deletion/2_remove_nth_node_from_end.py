# Remove N-th Node From End
# List:  1 -> 2 -> 3 -> 4 -> 5 -> None
#                       ↑
#               Remove 2nd node from END (which is node 4)

# Result: 1 -> 2 -> 3 -> 5 -> None

# Remember the golden rule —

# To delete a node at position X, you need to be at position X-1.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ─── BRUTE FORCE — Two Pass ───────────────────────────────
# TC - O(n), SC - O(1)
def removeNthFromEnd_brute(head, n):
    # ── Pass 1: calculate length ───────────────────────────
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # ── Edge case: remove head itself ─────────────────────
    if n == length:
        return head.next

    # ── Pass 2: walk to (length - n - 1) position ─────────
    target = length - n   # position of node to delete
    current = head
    for _ in range(target - 1):   # stop one before target
        current = current.next

    # ── Delete target node ────────────────────────────────
    current.next = current.next.next

    return head

# ─── OPTIMAL — One Pass ───────────────────────────────────

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    # Step 1: move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Step 2: move both until fast hits None
    while fast:
        slow = slow.next
        fast = fast.next

    # Step 3: delete target
    slow.next = slow.next.next

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

print("=" * 50)
print("BRUTE FORCE — Two Pass")
print("=" * 50)

# Test 1 — Remove 2nd from end (middle node)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd_brute(head, 2)
print("After: ", end=" "); print_list(head)
print()

# Test 2 — Remove 1st from end (tail)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd_brute(head, 1)
print("After: ", end=" "); print_list(head)
print()

# Test 3 — Remove head itself
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd_brute(head, 5)
print("After: ", end=" "); print_list(head)
print()

# Test 4 — Single node
head = build_list([1])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd_brute(head, 1)
print("After:  None")
print()

print("=" * 50)
print("OPTIMAL — One Pass")
print("=" * 50)

# Test 1 — Remove 2nd from end (middle node)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd(head, 2)
print("After: ", end=" "); print_list(head)
print()

# Test 2 — Remove 1st from end (tail)
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd(head, 1)
print("After: ", end=" "); print_list(head)
print()

# Test 3 — Remove head itself
head = build_list([1, 2, 3, 4, 5])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd(head, 5)
print("After: ", end=" "); print_list(head)
print()

# Test 4 — Single node
head = build_list([1])
print("Before:", end=" "); print_list(head)
head = removeNthFromEnd(head, 1)
print("After:  None")

# ─── OUTPUT ───────────────────────────────────────────────
# BRUTE FORCE — Two Pass
# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 3 -> 5 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 3 -> 4 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  2 -> 3 -> 4 -> 5 -> None

# Before: 1 -> None
# After:  None

# OPTIMAL — One Pass
# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 3 -> 5 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  1 -> 2 -> 3 -> 4 -> None

# Before: 1 -> 2 -> 3 -> 4 -> 5 -> None
# After:  2 -> 3 -> 4 -> 5 -> None

# Before: 1 -> None
# After:  None