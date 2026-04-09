# Sort Colors — LeetCode 75 (Medium)
# This is the famous Dutch National Flag problem by Edsger Dijkstra. It directly uses the partitioning thinking you just mastered — but with a twist.

# Given array with only 3 values: 0, 1, 2
# Sort it IN-PLACE in one pass.

# Input:  [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]

# Constraint that makes it interesting: You cannot use Python's built-in sort. One pass only. O(1) space.


# TC - O(n), SC - O(1)
def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:    # mid sees 0 → swap with low,  low++,  mid++
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:  #  mid sees 1 → do nothing, mid++
            mid += 1
        elif arr[mid] == 2:  #  mid sees 2 → swap with high, high--  (mid stays!)
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

arr = [2, 0, 2, 1, 1, 0]
print(sort_colors(arr))

# Edge case 1: Already sorted
arr = [0, 0, 1, 1, 2, 2]
print(sort_colors(arr))  # [0, 0, 1, 1, 2, 2] ✅

# Edge case 2: Reverse sorted
arr = [2, 2, 1, 1, 0, 0]
print(sort_colors(arr))  # [0, 0, 1, 1, 2, 2] ✅

# Edge case 3: Single element
arr = [1]
print(sort_colors(arr))  # [1] ✅

# Edge case 4: All same elements
arr = [2, 2, 2]
print(sort_colors(arr))  # [2, 2, 2] ✅

# Edge case 5: Only two colors
arr = [2, 0, 2, 0]
print(sort_colors(arr))  # [0, 0, 2, 2] ✅

# Edge case 6: Empty array
arr = []
print(sort_colors(arr))  # [] ✅