class ValidParenthesis:
    def __init__(self):
        self.__stack = []
        
    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.__stack)
    
    def push(self, val):
        self.__stack.append(val)
        
    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]
        return None
    
    def __repr__(self):
        return f"The size of stack is - {self.size()}"
    
test_str = "([)]" 
# "({[]})"   # valid
# "((("      # invalid
# "())"      # invalid  
# "([)]"     # invalid
# ")("       # invalid

vp = ValidParenthesis()
res = "Valid"

matches = {")": "(", "}": "{", "]": "["}


for i in test_str:
    if i in ["(", "{", "["]:
        vp.push(i)
    else:
        temp = vp.pop()
        if matches[i] != temp:
            res = "Invalid"
            break

if not vp.is_empty():  # unmatched openers remaining
    res = "Invalid"
print(res)        


# Loop finds a mismatch → res = "Invalid", break → final if is False → stays Invalid ✓
# Loop finishes with unmatched openers → if not vp.is_empty() is True → becomes Invalid ✓
# Everything matches, stack empty → final if is False → stays Valid ✓
