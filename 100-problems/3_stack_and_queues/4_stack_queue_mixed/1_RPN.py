# Reverse polished notation
# ["2", "3", "+", "4", "*"]

# TC - O(n), SC-O(n)

def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            pop1 = stack.pop()
            pop2 = stack.pop()
            if token == "+":
                temp = pop2 + pop1
            elif token == "-":
                temp = pop2 - pop1
            elif token == "*":
                temp = pop2 * pop1
            elif token == "/":
                temp = int(pop2 / pop1)
            stack.append(temp)

    return stack[0]

# Clean solution
def evaluate_rpnX(tokens):
    stack = []

    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))

    return stack[0]


# data_list = ["2", "3", "+", "4", "*"]
# data_list = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]  # expected 14
# data_list = ["2", "1", "+", "3", "*"]          # expected: 9
# data_list = ["4", "13", "5", "/", "+"]         # expected: 6
# data_list = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # expected: 22
data_list = ["3", "-4", "+"]   # negative numbers in input
print(evaluate_rpnX(data_list))