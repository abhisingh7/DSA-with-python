# Find First and Last Position — LeetCode 34 (Medium)

# Given a sorted array with duplicates,
# find the first AND last position of a target.

# Input:  arr=[5,7,7,8,8,10], target=8
# Output: [3, 4]

# Input:  arr=[5,7,7,8,8,10], target=6
# Output: [-1, -1]

# TC - O(log n), SC - O(1)
def find_left(arr, target):
    low = 0              # left boundary
    high = len(arr) - 1  # right boundary
    record = -1

    while low <= high:
        mid = low + (high - low) // 2  # find middle - overflow-safe for all languages

        if arr[mid] == target:   # FOUND
            record = mid
            high = mid - 1 # # go LEFT for first position

        elif arr[mid] < target:  # too early → go RIGHT
            low = mid + 1
        else:                    # too late → go LEFT
            high = mid - 1

    return record


def find_right(arr, target):
    low = 0              # left boundary
    high = len(arr) - 1  # right boundary
    record = -1

    while low <= high:           # search space still exists
        mid = low + (high - low) // 2  # find middle - overflow-safe for all languages

        if arr[mid] == target:   # FOUND
            record = mid
            low = mid + 1        # # go RIGhT for first position

        elif arr[mid] < target:  # too early → go RIGHT
            low = mid + 1
        else:                    # too late → go LEFT
            high = mid - 1

    return record

def search_range(arr, target):
    return [find_left(arr, target), find_right(arr, target)]


# Normal case — multiple occurrences
print(search_range([5,7,7,8,8,10], 8))   # [3, 4] ✅

# Single occurrence
print(search_range([5,7,7,8,8,10], 10))  # [5, 5] ✅

# Target not found
print(search_range([5,7,7,8,8,10], 6))   # [-1, -1] ✅

# All elements same
print(search_range([8,8,8,8,8], 8))      # [0, 4] ✅

# Single element found
print(search_range([8], 8))              # [0, 0] ✅

# Single element not found
print(search_range([8], 5))              # [-1, -1] ✅