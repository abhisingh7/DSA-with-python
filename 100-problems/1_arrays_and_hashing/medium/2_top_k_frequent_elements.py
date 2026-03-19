# Leetcode Problem 6: Top k frequent elements
# Link - https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List
import heapq

# 1. Brute Force Solution -  TC - O(nlogn), SC- O(n)

def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        count_list = list(count.keys())
        
        for i in range(k):
            output.append(count_list[i])
        return output

# 2. optimized solution - TC - O(nlogk) , SC - O(n)

def topKFrequentX(nums: List[int], k: int) -> List[int]:
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    # Keep a min-heap of size k
    return heapq.nlargest(k, count.keys(), key=lambda x: count[x])

# 3. Most Optimized solution- Bucket Sorting - TC - O(n), SC - O(n)
def topKFrequentY(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]  # index = frequency

    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    for n, c in count.items():
        freq[c].append(n)       # place number in its frequency bucket

    result = []
    for i in range(len(freq) - 1, 0, -1):   # iterate from highest freq
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result                


nums = [1,1,1,2,2,3]
k = 2

print(topKFrequentY(nums, k))