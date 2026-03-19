# Leetcode Problem 4: Intersection of two arrays
# Link - https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

# 1. Brute Force Solution - Complexity- O(n^2)
def productExceptSelf(nums: List[int]) -> List[int]:
    output = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i!=j:
                product = nums[j]*product
        output.append(product)        
    return output

# 2. Optimized Solution - Time Complexity, Space Complexity - O(n)
def left(nums, n):
    left = []
    for i in range(n):
        if left == []:
            left.append(1)
        else:
            left.append(left[i-1] * nums[i-1])
    return left

def right(nums, n):
    right = []
    for i in range(n-1,-1,-1):
        if i == n-1:
            right.append(1)
        else:
            right.append(right[-1] * nums[i+1])
    return right[::-1]


def productExceptSelfX(nums):
    n = len(nums)
    
    # left_arr = left(nums, n)
    # right_arr = right(nums, n)
    
    return [(left(nums, n)[i]*right(nums, n)[i]) for i in range(n)]


# 3. Most Optimized Solution - TC - O(n), SC - O(1)
def productExceptSelfY(nums):
    n = len(nums)
    output = [1] * n

    # Pass 1: store left products
    for i in range(1, n):
        output[i] = output[i-1] * nums[i-1]

    # Pass 2: multiply right products on the fly
    right = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * right
        right = right * nums[i]

    return output

# Example 1:

# Input: 
# left    = [ 1,  1,  2,  6]   # product of everything to the LEFT of i
# right   = [24, 12,  4,  1]   # product of everything to the RIGHT of i
# output = [24, 12, 8, 6]
nums = [1,2,3,4]
# Output: [24,12,8,6]
print(productExceptSelfY(nums))

# Example 2:

# Input: 
nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# print(productExceptSelf(nums))

# Example 3:
# nums = [0,0]
# Output: [0,0]
# print(productExceptSelf(nums))