# Leetcode Problem 8: subarray-sum-equals-k
# Link - https://leetcode.com/problems/subarray-sum-equals-k/description/

# How many subarrays sum equals to k

# we are using - prefix sum technique with dict(or hashmap)
# prefix[right + 1] - prefix[left] == k
# Just like algebra — if a - b = k, then b = a-k
# So, prefix[left] = prefix[right+1] - k


# Most Optimized Solution - TC - O(n), SC - O(n)
def subarray_sum(nums, k):
    # return the count of subarrays that sum to k
    seen = {0:1} # Key = Prefix Sum Value, Value = Count of prefix sum value
    current_sum = 0
    result = 0
    
    for num in nums:
        current_sum += num
        if (current_sum-k) in seen:
            result += seen[current_sum-k]

        seen[current_sum] = seen.get(current_sum,0) + 1
        
    return result
    

nums = [1, 2, 3, 1, 2]
k = 3
print(subarray_sum(nums, k))
# answer: 3
# why? [1,2], [3], [1,2] all sum to 3