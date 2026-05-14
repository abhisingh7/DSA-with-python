# Leetcode - 78 Medium - Subsets - leetcode.com/problems/subsets

# A subset means any combination of elements including empty set and the full set itself.
# For example => [1,2] ==> [], [1], [2], [1,2]

# NOTE => for n elements → 2ⁿ subsets always.
# Pattern => Include/Exclude

def subsets(nums):
    result = []

    def solve(index, current_subset):
        # base case
        if index == len(nums):
            result.append(current_subset)
            return

        # Include first - nums[index]
        solve(index+1, current_subset + [nums[index]])

        # Exclude Second nums[index]
        solve(index+1, current_subset)

    solve(0, [])
    return result

print(subsets([1,2]))

# Quick question — what happens to the output order if you swap include and exclude lines and put exclude first?
# Ans - Exclude first is just the exact reverse of include first.
# The order of recursive calls simply determines the order subsets get appended to result.
# Include first explores the "include" branch of the tree first,
# exclude first explores the "exclude" branch first.