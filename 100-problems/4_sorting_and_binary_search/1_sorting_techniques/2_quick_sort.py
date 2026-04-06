# Quick Sort — The Core IdeaOne sentence:
#     pick a pivot, put everything smaller to its left, everything larger to its right — now the pivot is in its permanent position forever. Repeat on both sides.
#     The step that does this rearranging is called partition.
#     That's the heart of Quick Sort. Everything else is just recursion on top of it.

#     Let's build partition first, then Quick Sort naturally falls out of it.


# TC -  O(n^2) — bad pivot choice
# SC -  O(log n) — in-place!
# Best for - Arrays, cache-friendly
def quick_sort(arr, low, high):
    if low < high:                     # base case: single element or empty
        pi = partition(arr, low, high) # pi = partition index — pivot is now at its FINAL position

        quick_sort(arr, low, pi - 1)   # sort left of pivot
        quick_sort(arr, pi + 1, high)  # sort right of pivot


def partition(arr, low, high):
    pivot = arr[high]  # always pick last element as pivot
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