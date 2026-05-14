# Leetcode - 39 Medium - Combination Sum 1 - leetcode.com/problems/combination-sum

# Problem - Given [2, 3, 6, 7] and target 7, find all combinations that sum to 7.
# Answer: [2,2,3], [7]

# Note - In the standard Combination Sum problem — you can reuse the same element multiple times, like [2,2,3]
# Pattern -  Pruning check

# Algo -
# if current_sum > target → return immediately
# if current_sum == target → found answer, append
# otherwise → keep exploring

def combination_sum(nums, target):
    result = []

    def solve(index, current, current_sum):
        # Pruning - overshoot
        if current_sum > target:
            return

        # Found valid combination
        if current_sum == target:
            result.append(current)
            return

        for i in range(index, len(nums)):
            # include nums[i] and stay at same index (reuse allowed)
            solve(i, current + [nums[i]], current_sum + nums[i])

    solve(0, [], 0)
    return result

# Test
nums = [2,3,6,7]
target = 7
print(combination_sum(nums, target))

# solve(0, [], 0)
# → pick 2 → solve(0, [2], 2)
# → pick 2 → solve(0, [2,2], 4)
# → pick 2 → solve(0, [2,2,2], 6)
# → pick 2 → solve(0, [2,2,2,2], 8) → PRUNED ✅
# → pick 3 → solve(1, [2,2,3], 9) → PRUNED ✅
# → back to [2,2] pick 3 → solve(1, [2,2,3], 7) → ✅ FOUND!
# ...
# → pick 7- solve(3, [7], 7)        → ✅ FOUND!

# Answer [[2,2,3], [7]]