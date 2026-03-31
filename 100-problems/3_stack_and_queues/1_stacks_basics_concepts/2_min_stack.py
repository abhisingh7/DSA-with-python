class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def get_min(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

    def __repr__(self):
        return f"Stack: {self.stack}, MinStack: {self.min_stack}"

if __name__ == "__main__":
    min_stack  = MinStack()

    # print(min_stack)
    # print(min_stack.is_empty())
    min_stack.push(5)
    # print(min_stack)
    min_stack.push(3)
    # print(min_stack)
    min_stack.push(7)
    # print(min_stack)
    min_stack.push(3)
    print(min_stack)
    print(min_stack.get_min())  # should return 3
    print(min_stack.pop())
    print(min_stack.get_min())   # should still return 3
    print(min_stack.pop())
    print(min_stack.get_min())   # should still return 3
    print(min_stack.pop())
    print(min_stack.get_min())   # should return 5