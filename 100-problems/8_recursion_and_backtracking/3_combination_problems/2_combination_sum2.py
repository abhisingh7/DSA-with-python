# Leetcode - 40 Medium - Combination Sum 2 - leetcode.com/problems/combination-sum-ii

# Problem - Given [2, 3, 6, 7] and target 7, find all combinations that sum to 7.
# Answer: [2,2,3], [7]

# Note - In the standard Combination Sum problem — you can reuse the same element multiple times, like [2,2,3]
# Pattern -  Pruning check

# Algo -
# if current_sum > target → return immediately
# if current_sum == target → found answer, append
# otherwise → keep exploring


# But
# Combination Sum II has two differences from Combination Sum I.
# 1. First difference — No reuse
# In Combination Sum II each element can only be used once.

# 2. Duplicates in input
# a. Same recursion level = produces duplicate results = skip
# b. Deeper recursion level = produces new unique results = allow

# nums = [1, 1, 2, 5, 6, 7, 10], target = 8
# Output = [1,2,5], [1,7], [2,6]


def combination_sum(nums, target):
    result = []
    # 1. Sort the array first
    nums.sort()

    def solve(index, current, current_sum):
        # Pruning - overshoot
        if current_sum > target:
            return

        # Found valid combination
        if current_sum == target:
            result.append(current)
            return

        for i in range(index, len(nums)):
            # 3. Skip duplicates for same level recursion
            if i > index and nums[i] == nums[i-1]:
                continue
            # 2. Pass i+1 instead of i (no reuse)
            solve(i+1, current + [nums[i]], current_sum + nums[i])

    solve(0, [], 0)
    return result

# Test
nums = [1, 1, 2, 5, 6, 7, 10]
target = 8
print(combination_sum(nums, target))

# result = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]