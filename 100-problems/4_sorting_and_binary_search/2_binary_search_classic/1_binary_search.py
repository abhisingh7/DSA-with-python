# Binary Search only works on SORTED arrays.
# TC - O(logn), SC - O(1)

def binary_search(arr, target):
    low = 0              # left boundary
    high = len(arr) - 1  # right boundary

    while low <= high:           # search space still exists
        mid = (low + high) // 2  # find middle - (mid = low + (high - low) // 2 ) # overflow-safe for all languages

        if arr[mid] == target:   # FOUND
            return mid
        elif arr[mid] < target:  # too early → go RIGHT
            low = mid + 1
        else:                    # too late → go LEFT
            high = mid - 1

    return -1   # not found

arr    = [3, 9, 15, 27, 38, 43, 82]
target = 27
print(binary_search(arr, target))