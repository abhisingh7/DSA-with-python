class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ─── INSERT ───────────────────────────────────────────

    def append(self, value):
        """Add node at the END — O(1)"""
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add node at the BEGINNING — O(1)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

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
        next_node = current.next
        # wire new_node
        new_node.next = next_node
        new_node.prev = current
        # wire neighbors
        current.next = new_node
        next_node.prev = new_node
        self.length += 1

    # ─── DELETE ───────────────────────────────────────────

    def delete_by_value(self, value):
        """Delete first node with given VALUE — O(n)"""
        if self.head is None:
            return
        current = self.head
        while current:
            if current.value == value:
                self._unlink(current)
                return
            current = current.next

    def delete_at(self, index):
        """Delete node at a specific INDEX — O(n)"""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        self._unlink(current)

    def _unlink(self, node):
        """Internal helper — disconnects a node cleanly — O(1)"""
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node       # deleted node was head
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node       # deleted node was tail
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
        """Print list forward — O(n)"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements) + " -> None")

    def print_reverse(self):
        """Print list backward — O(n)"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev
        print(" <-> ".join(elements) + " -> None")

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

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.prepend(5)
dll.print_list()          # 5 <-> 10 <-> 20 <-> 30 <-> 40 -> None

dll.insert_at(2, 15)
dll.print_list()          # 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> 40 -> None

dll.delete_by_value(15)
dll.print_list()          # 5 <-> 10 <-> 20 <-> 30 <-> 40 -> None

dll.delete_at(0)
dll.print_list()          # 10 <-> 20 <-> 30 <-> 40 -> None

dll.print_reverse()       # 40 <-> 30 <-> 20 <-> 10 -> None
print(dll.search(30))     # 2
print(len(dll))           # 4
print(dll.to_list())      # [10, 20, 30, 40]