class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # ─── INSERT ───────────────────────────────────────────

    def append(self, value):
        """Add node at the END — O(n)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def prepend(self, value):
        """Add node at the BEGINNING — O(1)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # The golden rule of linked lists:
    # To do anything at position X, you need to be at position X-1.
    def insert_at(self, index, value):
        """Add node at a specific INDEX — O(n)"""
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        # The Golden Rule 🎯

        # Always save the connection BEFORE breaking it.
        new_node.next = current.next    # FIRST  — save the existing chain into new_node
        current.next = new_node         # SECOND — now safely rewire
        self.length += 1

    # ─── DELETE ───────────────────────────────────────────

    def delete_by_value(self, value):
        """Delete first node with given VALUE — O(n)"""
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    # The golden rule of linked lists:
    # To do anything at position X, you need to be at position X-1.
    def delete_at(self, index):
        """Delete node at a specific INDEX — O(n)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1

    # ─── SEARCH ───────────────────────────────────────────

    def search(self, value):
        """Returns index of value, -1 if not found — O(n)"""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # ─── DISPLAY ──────────────────────────────────────────

    def print_list(self):
        """Print list in readable format — O(n)"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def to_list(self):
        """Convert to Python list — O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self.length


# ─── TEST IT ──────────────────────────────────────────────

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.prepend(5)
ll.print_list()        # 5 -> 10 -> 20 -> 30 -> 40 -> None

ll.insert_at(2, 15)
ll.print_list()        # 5 -> 10 -> 15 -> 20 -> 30 -> 40 -> None

ll.delete_by_value(15)
ll.print_list()        # 5 -> 10 -> 20 -> 30 -> 40 -> None

ll.delete_at(0)
ll.print_list()        # 10 -> 20 -> 30 -> 40 -> None

print(ll.search(30))   # 2
print(len(ll))         # 4
print(ll.to_list())    # [10, 20, 30, 40]