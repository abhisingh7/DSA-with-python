# Leetcode Problem 1: Two Sum
# Link - https://leetcode.com/problems/two-sum/description/


# 1 - Brute Force Solution -  Complexity - O(n^2)

def twoSum(nums, target):
    for i in range(len(nums)):
        complement = target - nums[i]
        for j in range(i+1, len(nums)):
            if complement == nums[j]:
                return [i,j]


# 2 - Most Optimized Solution -  Complexity - O(n)

def twoSum(nums, target):
    seen = {} # Values -> Index
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[nums[i]] = i
                

