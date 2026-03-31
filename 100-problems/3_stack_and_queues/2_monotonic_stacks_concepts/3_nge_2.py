# NGE II — single circular array. If no greater element exists to the right, you can wrap around and continue searching from the beginning.
# Input:  [3, 1, 2, 4, 2]
# Output: [4, 2, 4, -1, 3]

# Range for circular array -> 0 to 2n -1, where n = size of input array


class NGE_2:
    def __init__(self):
        self.__stack = []
        
    def is_empty(self):
        return len(self.__stack) == 0
    
    def n(self):
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
    
    
stk = NGE_2()
# input = [3, 1, 2, 4, 2]
# input = [1,1,1]
input = []
n = len(input)
output = [-1] * n
        
for i in range(2*n): # 0 to 2n-1
    while stk.peek() is not None and input[stk.peek()] < input[i%n]:
        temp = stk.pop()
        output[temp % n] = input[i%n] # Value calculation
    if i < n:
        stk.push(i)
print(output)