# Leetcode Problem 9: maximum-subarray
# Link - https://leetcode.com/problems/maximum-subarray/description/

# Using kadane algorithm
# At any index i, you have two choices:
# 	1.	Extend previous sum
# 	2.	Start new subarray from current element
from typing import List


def maxSubArray(nums: List[int]) -> int:
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))