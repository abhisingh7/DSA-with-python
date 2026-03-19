# Leetcode Problem 7: Longest consecutive sequence
# Link - https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List

# 1. Brute Force - TC - O(n^2), SC - O(1)
def longestConsecutive(nums: List[int]) -> int:
    longest = 0

    for n in nums:
        length = 1
        # keep checking if the next consecutive number exists in nums
        while (n+1) in nums:
            length += 1
            n+= 1
        longest = max(longest, length)

    return longest

# 2. Most Optimized Solution - TC - O(n), SC- O(n) bcoz of storing in set.

def longestConsecutiveX(nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if (n - 1) not in nums_set:  # n is a true sequence start
                length = 1
                while (n + length) in nums_set:
                    length += 1
                longest = max(longest, length)

        return longest


# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,0,1,2]
print(longestConsecutiveX(nums))