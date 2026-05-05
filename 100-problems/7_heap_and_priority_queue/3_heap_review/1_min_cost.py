# LeetCode → Problem 1167 (Medium) - Min Cost to Connect Sticks
# Problem Statement
# You have n sticks with given lengths. Every time you connect two sticks,
# the cost is equal to the sum of their lengths. You want to connect all sticks into one stick.
# Return the minimum total cost.

# Example -
# Input:  sticks = [2, 4, 3]
# Output: 14

import heapq

# TC - O(n logn)
# SC - O(1) heapify in place
def connect_sticks(sticks):
    cost = 0
    heapq.heapify(sticks)
    for _ in range(len(sticks) - 1):
        pop1 = heapq.heappop(sticks)
        pop2 = heapq.heappop(sticks)
        cost += pop1 + pop2
        heapq.heappush(sticks, pop1 + pop2)
    return cost

# Test
sticks = [2,4,3]
print(connect_sticks(sticks))
