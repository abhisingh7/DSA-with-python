"""
Problem -  Max sum of any k consecutive elements in an ARRAY.

Example - 
          nums = [1,4,2,9,7,3,8,6]
          k = 3
"""
# TC - O(n)
def max_consecutive_sum(nums, k):
    if len(nums) < k:
        return 0
    
    current_sum = sum(nums[:k]) 
    max_sum = current_sum
    
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k] # Assume i = fast, i-k = slow pointer
        max_sum = max(max_sum, current_sum)
    return max_sum

nums = [1, 4, 2, 9, 7, 3, 8, 6]
k = 3  # window size
print(max_consecutive_sum(nums, k))