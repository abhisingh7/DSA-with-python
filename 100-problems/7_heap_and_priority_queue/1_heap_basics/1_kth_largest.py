#  LeetCode 215 (Medium)
import heapq

# Time Complexity: O(n log n)
def kth_largest(nums, k):
    heapq.heapify(nums)
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    return nums[0]


# TC - O(n log k)
def kth_largest_opt(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# TEST
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums,k))

# After heapify
# heap = [1, 2, 3, 5, 6, 4]

# # Pop len(nums) - k = 6 - 2 = 4 times
# pop → 1,  heap = [2, 4, 3, 5, 6]
# pop → 2,  heap = [3, 4, 6, 5]
# pop → 3,  heap = [4, 5, 6]
# pop → 4,  heap = [5, 6]

# return heap[0] = 5 ✅

