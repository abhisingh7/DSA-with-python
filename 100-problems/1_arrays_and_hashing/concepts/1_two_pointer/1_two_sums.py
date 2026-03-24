# User will give SORTED ARAAY with positive element and a target. 
# Find out two numbers whose sum will be equal to target. -> Return Nums pair
# If not found -> Return empty list

# Solution 1 - Using two pointers
# TC - O(n)
def two_sums(nums, target):
    left = 0
    right = len(nums) - 1

    current_sum = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]
            
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return [] # no solution found


# Solution 2 -  using dictionary(hashmap) - TC - O(n)
def two_sumsX(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        
        diff = target - num
        
        if diff in seen:
            return[seen[diff], i]
        
        seen[num] = i
    return []


# test 1
nums = [1, 3, 5, 7, 9, 11]
target = 10
# print(two_sums(nums, target))

# test 2
nums = [2,7,11,15]
target = 22
print(two_sumsX(nums, target))
