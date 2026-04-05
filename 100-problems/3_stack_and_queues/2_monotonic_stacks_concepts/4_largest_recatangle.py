# hard problem - Largest Rectangle in Histogram

# Input:  [2, 1, 5, 6, 2, 3]
# Output: 10

# for Histogram, for each bar you need:

# How far right until you hit a shorter bar
# How far left until you hit a shorter bar
# That's "next smaller element" — same monotonic stack pattern, just flipped from greater to smaller!


def largest_rectangle(heights):
    stack = []
    max_area = 0

    # main loop
    for j in range(len(heights)):
        while stack and heights[stack[-1]] > heights[j]:
            i = stack.pop()
            right = j
            left = stack[-1] if stack else -1
            width = right - left - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        stack.append(j)
    # handle remaining bars in stack
    while stack:
        i = stack.pop()
        right = len(heights)
        left = stack[-1] if stack else -1
        width = right - left - 1
        area = heights[i] * width
        max_area = max(max_area, area)
    return max_area

test0 = [2, 1, 5, 6, 2, 3] # 10
test1 = []          # empty array - 0
test2 = [5]         # single bar - 5
test3 = [5, 5, 5]  # all equal - 15
test4 = [1, 2, 3, 4, 5]  # strictly increasing - 9
test5 = [5, 4, 3, 2, 1]  # strictly decreasing - 9


print(largest_rectangle(test5))