"""
Statement - Remove Duplicate from SORTED ARRAY

Constraints - 

    1. modify array in place
    2. Return Count of unique elements
    3. O(1) extra space only.
    4. O(n) TC
"""

def remove_duplicates(nums):
    slow = 0
    fast = 1

    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            if slow + 1 != fast:  # only write if not already adjacent
                nums[slow + 1] = nums[fast]
            slow += 1

    return slow + 1

nums = [1, 1, 2, 2, 3, 4, 4, 5]

k = remove_duplicates(nums)
print(nums[:k])

# nums = [1,2,3,4,5] # Best TC- O(0) bcoz of if condition in else

# nums = [1,1,1,1,2] # Best TC- O(1) bcoz of if condition in else
