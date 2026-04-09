# LeetCode (Easy) - Search Insert Position

# Given a sorted array and a target:
# → If target EXISTS → return its index
# → If target DOES NOT EXIST → return the index
#   where it WOULD be inserted to keep array sorted

# Input:  arr=[1, 3, 5, 6], target=5  → Output: 2
# Input:  arr=[1, 3, 5, 6], target=2  → Output: 1
# Input:  arr=[1, 3, 5, 6], target=7  → Output: 4
# Input:  arr=[1, 3, 5, 6], target=0  → Output: 0

def search_insert_position(arr, target):
    low = 0              # left boundary
    high = len(arr) - 1  # right boundary

    while low <= high:           # search space still exists
        mid = (low + high) // 2  # find middle

        if arr[mid] == target:   # FOUND
            return mid
        elif arr[mid] < target:  # too early → go RIGHT
            low = mid + 1
        else:                    # too late → go LEFT
            high = mid - 1

    return low   # index for inserting.

arr = [1,3,5,6]

print(search_insert_position(arr, 5))
print(search_insert_position(arr, 2))
print(search_insert_position(arr, 7))
print(search_insert_position(arr, 0))