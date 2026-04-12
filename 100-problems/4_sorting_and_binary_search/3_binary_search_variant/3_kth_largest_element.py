# Given an unsorted array, find the Kth largest element.

# Input:  arr=[3, 2, 1, 5, 6, 4], k=2
# Output: 5

# Input:  arr=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4
# Output: 4


# 1. Brute Force Solution
# Time - O(n log n),
# Space - O(1)
def find_kth_largest_brute(arr, k):
    # sort in descending order
    arr.sort(reverse=True)
    # kth largest is at index k-1
    return arr[k-1]

# Test
# print(find_kth_largest_brute([3,2,1,5,6,4], 2))  # 5 ✅
# print(find_kth_largest_brute([3,2,3,1,2,4,5,5,6], 4))  # 4 ✅


# The Heap Idea — One Sentence

# Keep a bucket of exactly k elements — always throwing out the smallest one when the bucket gets too full.

# Why a Heap?
# Because at every step you need two things fast:

# Find the smallest element in bucket → O(1)
# Remove smallest and add new element → O(log k)

import heapq

# Time - O(n log k) — n elements, each push/pop costs log k
# Space - O(k) — heap never exceeds k elements
def find_kth_largest(arr, k):
    heap = []

    for num in arr:
        heapq.heappush(heap, num)  # add current number

        if len(heap) > k:                       # bucket too full?
            heapq.heappop(heap)                 # throw out smallest

    return heap[0]                  # kth largest element at top

# Normal case
# print(find_kth_largest([3,2,1,5,6,4], 2))      # 5 ✅

# # k = 1 (largest element)
# print(find_kth_largest([3,2,1,5,6,4], 1))      # 6 ✅

# # k = len(arr) (smallest element)
# print(find_kth_largest([3,2,1,5,6,4], 6))      # 1 ✅

# # Duplicates
# print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4)) # 4 ✅

# # Single element
# print(find_kth_largest([1], 1))                 # 1 ✅

# # All same elements
# print(find_kth_largest([2,2,2,2], 2))           # 2 ✅


# 3. kth largest by removing duplicates
def find_kth_largest_unique(arr, k):
    heap = []
    arr = list(set(arr))  # Remove duplicates

    # guard clause — k is invalid
    if k > len(arr):
        raise ValueError("K exceeds unique elements")

    for num in arr:
        heapq.heappush(heap, num)  # add current number

        if len(heap) > k:                       # bucket too full?
            heapq.heappop(heap)                 # throw out smallest

    return heap[0]                  # kth largest element at top

print(find_kth_largest_unique([3,2,3,1,2,4,5,5,6], 3))