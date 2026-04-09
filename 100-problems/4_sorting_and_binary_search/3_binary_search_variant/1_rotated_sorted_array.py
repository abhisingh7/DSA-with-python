# Medium -  Rotated Sorted Array
# ex - [7, 9, 11, 13, 1, 3, 5]
    #   ↑                  ↑
    #  idx 0             idx 6
# If we know the left half is sorted between arr[low] and arr[mid] — and our target falls within that range — target MUST be in the left half. Throw away the right.
# If target is NOT in that range — it MUST be in the right half. Throw away the left.


def search_rotated(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        # check which half is sorted
        if arr[low] <= arr[mid]:  # LEFT half is sorted
            if arr[low] <= target < arr[mid]:  # is target in left half?
                high = mid - 1
            else:
                low = mid + 1
        else:                      # RIGHT half is sorted
            if arr[mid] < target <= arr[high]:  # is target in right half?
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Normal rotation
print(search_rotated([7,9,11,13,1,3,5], 1))   # 4 ✅
print(search_rotated([7,9,11,13,1,3,5], 11))  # 2 ✅

# Target not in array
print(search_rotated([7,9,11,13,1,3,5], 6))   # -1 ✅

# No rotation at all
print(search_rotated([1,3,5,7,9,11,13], 7))   # 3 ✅

# Single element
print(search_rotated([1], 1))                  # 0 ✅

# Target at boundaries
print(search_rotated([7,9,11,13,1,3,5], 7))   # 0 ✅
print(search_rotated([7,9,11,13,1,3,5], 5))   # 6 ✅