# Problem: Given an array of daily temperatures, for each day return how many days you have to wait until a warmer temperature. If no warmer day exists, return 0.

# Input:  [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,   1,   4,  2,  1,  1,  0,   0]

# Notice — instead of storing the next greater value, you're storing the distance to it.

# Next Greater Element I — given an array, return an array where each position contains the next greater element to the right. If none exists, put -1.

# Input:  [4, 2, 6, 1, 3]
# Output: [6, 6, -1, 3, -1]

class DailyTemperature:
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
    
    
stk = DailyTemperature()
input = [73, 74, 75, 71, 69, 72, 76, 73]
# input = []
size = len(input)
output = [0] * size
        
for i in range(size):
    while stk.peek() is not None and input[stk.peek()] < input[i]:
        temp = stk.pop()
        output[temp] = i - temp # Distance calculation
    stk.push(i)
print(output)