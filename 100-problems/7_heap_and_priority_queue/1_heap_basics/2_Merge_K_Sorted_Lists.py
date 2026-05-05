# LeetCode 23 (Hard)
# Merge K Sorted Lists — asked at Google, Facebook, Amazon regularly.
# Input:  lists = [[1,4,5], [1,3,4], [2,6]]
# Output: [1,1,2,3,4,4,5,6]

import heapq

# 1. Brute Force
# TC - O(n log n)
def merge_k_lists_bf(lists):
    flat = []
    for lst in lists:
        flat.extend(lst)
    flat.sort()
    return flat

# 2. optimized heap approach
# TC - O(n logk)
# n = total elements across all lists
# k = number of lists = heap size
def merge_k_lists(lists):
    heap = []
    result = []

    # Step 1: Push first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    # Step 2: Keep popping minimum
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = element_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result

# Test
lists = [[1,4,5], [1,3,4], [2,6]]
print(merge_k_lists(lists))  # [1,1,2,3,4,4,5,6]