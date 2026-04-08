from random import randint

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr, low, high):
    while low < high:
        # Use insertion sort for small partitions
        if high - low < 10:
            insertion_sort(arr, low, high)
            return

        pi = partition(arr, low, high) # pi = partition index — pivot is now at its FINAL position

        # Tail Recursion Optimization - Always recurse on smaller half first, loop on larger half
        # Reduces recursion depth to O(log n)
        # Prevents stack overflow
        # Recursion on smaller side
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)   # sort left of pivot
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)  # sort right of pivot
            high  = pi -1

# use random pivot for better performance.
# Keeps average TC - O(nlogn)
# avoids worst case scenario

def partition(arr, low, high):
    pivot_index = randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1        # i tracks the boundary of "smaller than pivot" zone
                        # ( i represents index of last confirmed element smaller than pivot)

    for j in range(low, high):               # j scans every element except pivot
        if arr[j] <= pivot:
            i += 1                           # grow the "smaller" zone
            arr[i], arr[j] = arr[j], arr[i]  # swap element into smaller zone

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # return pivot's final index


# --- Test it ---
arr = [38, 27, 43, 3, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [3, 9, 27, 38, 43]