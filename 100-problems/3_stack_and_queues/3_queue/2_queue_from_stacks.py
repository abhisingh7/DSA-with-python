class Queue:
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def is_empty(self):
        return not self.__stack1 and not self.__stack2

    def enqueue(self, val):
        self.__stack1.append(val)

    def __transfer(self):
        while self.__stack1:
            self.__stack2.append(self.__stack1.pop())

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        if not self.__stack2:
            self.__transfer()
        return self.__stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        if not self.__stack2:
            self.__transfer()
        return self.__stack2[-1]

    def __repr__(self):
        return f"Queue({list(reversed(self.__stack2)) + self.__stack1})"


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())  # should return 1
print(q.peek())     # should return 2
q.enqueue(4)
print(q.dequeue())  # should return 2
print(q.dequeue())  # should return 3