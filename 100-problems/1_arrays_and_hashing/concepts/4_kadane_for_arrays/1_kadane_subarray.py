# find the subarray with the largest sum - 
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# answer: [4, -1, 2, 1] → sum = 6

# Approach - 
# [-2]          start=0, end=0
# [-2, 1]       start=0, end=1
# [1, -3, 4]    start=1, end=3
# [4, -1, 2, 1] start=3, end=6


# 1. Brute force Solution - TC - O(n^2)
def max_subarray_bruteforce(nums):
    n = len(nums)
    max_sum = float('-inf')
    
    start = 0
    end = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    return nums[start:end+1], max_sum


# 2. Kadane algorithm - TC - O(n), SC - O(1)
# At any index i, you have two choices:
# 	1.	Extend previous sum
# 	2.	Start new subarray from current element

def kadane_with_subarray(nums):
    # Initializing with 0th element so it can handle array with all negative value edge case.
    current_sum = nums[0]
    max_sum = nums[0]

    start = 0
    temp_start = 0
    end = 0

    for i in range(1, len(nums)):
        
        # Decide whether to start new subarray
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        # Whenever current_sum becomes harmful (negative):
        # 👉 Drop it. Start fresh.
        # That’s Kadane in one sentence.

        # Update global max
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return nums[start:end+1], max_sum

# 3. kadane - only max_sum calculation
def kadane_max_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# subarray, max_sum = max_subarray_bruteforce(nums)
# print("Subarray:", subarray)
# print("Max Sum:", max_sum)

subarray, max_sum = kadane_with_subarray(nums)
print("Subarray:", subarray)
print("Max Sum:", max_sum)