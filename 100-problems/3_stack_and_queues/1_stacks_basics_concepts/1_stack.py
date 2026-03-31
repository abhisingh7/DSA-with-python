class Stack:
    def __init__(self):
        self.__stack = []
        
    def is_empty(self):
        return len(self.__stack) == 0
    
    def size(self):
        return len(self.__stack)
    
    def push(self, val):
        self.__stack.append(val)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.__stack.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]
        return None
    
    def __repr__(self):
        return f"Stack({self.__stack})"
    
    
if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())   
    print(stack.size())
    print(stack)
    print(stack.pop())
    # stack.push(4)
    # stack.push(3)
    # stack.push(2)
    # stack.push(1)

    # print(stack)

    # print(stack.peek())
    # print(stack.pop())
    # print(stack)