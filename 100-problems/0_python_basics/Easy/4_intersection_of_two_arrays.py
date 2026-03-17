# Leetcode Problem 4: Intersection of two arrays
# Link - https://leetcode.com/problems/intersection-of-two-arrays/description/

from typing import List

# 1. MY Brute Force solution - Time Complexity - O(n+m) ,  Space Complexity - O(n+m)
# Most Optimized as well for interviews also.
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        res = []
        
        small, big = (n1, n2) if len(n1) < len(n2) else (n2, n1)
        
        for i in small:
            if i in big:
                res.append(i)
        return res

# 2. Cleanest Python Solution - Same complexity: O(n + m)
def intersectionX(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))

# Example - 

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersectionX(nums1, nums2))