# LeetCode → Problem 347 (Medium) -
# Given nums = [1,1,1,2,2,3] and k = 2, the answer is [1,2] in any order.

import heapq

# 1. Brute Force
# TC - O(n log n)
def top_k_freq_elements(nums, k):
    # Step 1: Count frequencies
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    print(freq)  # {1:3, 2:2, 3:1}
    # sorting dict
    sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

    # Extract first k keys
    result = list(sorted_dict.keys())[:k]
    print(result)

# 2. Optimized
# TC -  O(n log k)
def top_k_frequent(nums, k):
    # Step 1: frequency dict
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: heap of size k
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: extract result
    return [num for freq, num in heap]

# Test
nums = [1,1,1,2,2,3]
k = 2
top_k_freq_elements(nums, k) # [1, 2]

print(top_k_frequent(nums, k))