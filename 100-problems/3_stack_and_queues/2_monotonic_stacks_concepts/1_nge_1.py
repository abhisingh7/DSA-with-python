# Next Greater Element I — given an array, return an array where each position contains the next greater element to the right. If none exists, put -1.

# Input:  [4, 2, 6, 1, 3]
# Output: [6, 6, -1, 3, -1]

# Interview Notes - When do you use monotonic stack?
# "I use a monotonic stack when I need to find the next greater or smaller element for each element in an array.
# The stack maintains elements in increasing or decreasing order — when a new element violates that order,
# it triggers pops, and each pop gives me the answer for that element.
# It's O(n) because every element is pushed and popped at most once, compared to O(n²) brute force."

class NGE_1:
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


stk = NGE_1()
input = [4, 2, 6, 1, 3]
# input = [1, 2, 3, 4, 5]
# input = [5,4,3,2,1]
# input = []
size = len(input)
output = [-1] * size

for i in range(size):
    while stk.peek() is not None and input[stk.peek()] < input[i]:
        output[stk.pop()] = input[i] # Value calculation
    stk.push(i)
print(output)