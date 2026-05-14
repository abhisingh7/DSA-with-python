# Leetcode - 46 Medium - Permutations - leetcode.com/problems/permutations

# Permutations means — arrange all elements in every possible order.
# For example - [1,2,3] permutations are -

# [1,2,3] and [1,3,2]
# [2,1,3] and [2,3,1]
# [3,1,2] and [3,2,1]
# Total 6 combinations

# NOTE => for n elements, total permutations = n!
# Pattern => Pick and Recurse

def permutations(nums):
    result = []

    def solve(current, remaining):
        if len(remaining) == 0:
            # 3. When no elements left → you have one complete permutation
            result.append(current)

        for element in remaining:
            # 1. At each step, pick one element to place at current position
            # 2. # Recurse on remaining elements
            solve(current + [element], [x for x in remaining if x != element])

    solve([], nums)
    return result

# Test
print(permutations([1,2]))

# solve([], [1,2])
# ├── pick 1 → solve([1], [2])
# │   └── pick 2 → solve([1,2], []) → ✅ append [1,2]
# └── pick 2 → solve([2], [1])
#     └── pick 1 → solve([2,1], []) → ✅ append [2,1]

# Result: [[1,2], [2,1]] ✅