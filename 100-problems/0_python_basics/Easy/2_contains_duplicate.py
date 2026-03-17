# Leetcode Problem 2: Contains Duplicate
# Link - https://leetcode.com/problems/contains-duplicate/description/

from typing import List
from collections import defaultdict
from collections import Counter


# 1 - Brute Force Solution -  Complexity - O(n)

def containsDuplicate(nums: List[int]) -> bool:
        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1
                return True
        return False


# 2 - Optimized Solution -  Complexity - O(n)
# Using collections -  defaultdict

def containsDuplicateX(nums: List[int]) -> bool:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            
            if freq[num] > 1:
                return True
        return False

# 3 -  Optimized Solution -  Complexity - O(n)
# Using collections -  Counter

def containsDuplicateY(nums: List[int]) -> bool:
        freq = Counter(nums)
        occurence = freq.most_common(1)[0][1]
        if occurence > 1:
            return True
        return False
    

# 4 - Fastest Solution - Complexity - O(n)
# Using set

def containsDuplicateZ(nums: List[int]) -> bool:
    seen = set(nums)
    
    # if len(seen) != len(nums):
    #     return True

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(containsDuplicateZ(nums=[1,2,3,1]))

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true


# Example 2:

# Input: nums = [1,2,3,4]

# Output: false


# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true