# Sliding Window Maximum.
# This is a classic hard/medium problem and uses a deque in a clever way.

# Input: [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]

# Solution - 1- Brute Force - TC - O(n*k)
def sliding_window_maximum(input, k):
    i = 0
    output = []

    for j in range(k, len(input)+1): # (n - k + 1)
        output.append(max(input[i:j]))
        i+=1
    return output


# Solution 2 -
from collections import deque

def sliding_window_maximumX(input, k):
    dq = deque()
    output = []

    for i in range(len(input)):
        # Step 1: remove out-of-window elements from front
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Step 2: remove useless elements from back
        while dq and input[dq[-1]] < input[i]:
            dq.pop()
        # Step 3: push current index
        dq.append(i)
        # Step 4: if window is complete, record maximum
        if i >= k - 1:
            output.append(input[dq[0]])

    return output


Input =  [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximumX(Input, k))