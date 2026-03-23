# User will give SORTED ARAAY with positive element and a target. 
# Find out two numbers whose sum will be equal to target. -> Return Nums pair
# If not found -> Return empty list

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

nums = [1, 3, 5, 7, 9, 11]

target = 10

print(two_sums(nums, target))