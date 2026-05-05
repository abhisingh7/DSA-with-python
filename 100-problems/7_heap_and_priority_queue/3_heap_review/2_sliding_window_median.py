# LeetCode → Problem 480 (Hard) - Sliding Window Median
# Problem Statement -
# Given an array nums and window size k, find the median of each window as it slides from left to right.

# Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1,-1,-1,3,5,6]

# Window 1: [1, 3,-1] → median = 1
# Window 2: [3,-1,-3] → median = -1
# Window 3: [-1,-3, 5] → median = -1
# Window 4: [-3, 5, 3] → median = 3
# Window 5: [5, 3, 6]  → median = 5
# Window 6: [3, 6, 7]  → median = 6

# Note - For Median, First sort the array.
# If its odd array picks middle value.
# if it's even, take average of the two middle values

import heapq


# Step 1: Decide which half new element belongs to
# Step 2: Insert it
def insert(num, max_heap, min_heap):
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)  # negate for max heap
    else:
        heapq.heappush(min_heap, num)


# Step 3: Rebalance if size difference > 1
def rebalance(max_heap, min_heap):
    if len(max_heap) > len(min_heap) + 1:
        # move max_heap's top to min_heap
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap) + 1:
        # move min_heap's top to max_heap
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

# Step 4: Find median from tops of both heaps
def get_median(max_heap, min_heap):
    if len(max_heap) == len(min_heap):
        # even total → average of both tops
        return (-max_heap[0] + min_heap[0]) / 2
    else:
        # odd total → larger heap's top
        return float(-max_heap[0]) if len(max_heap) > len(min_heap) else float(min_heap[0])

# main function
def median_sliding_window(nums, k):
    max_heap = []  # left half (negated)
    min_heap = []  # right half
    to_remove = {} # lazy deletion tracker
    result = []

    # Step 1: Build first window
    for num in nums[:k]:
        insert(num, max_heap, min_heap)
    rebalance(max_heap, min_heap)
    result.append(get_median(max_heap, min_heap))

    # Step 2: Slide the window
    for i in range(k, len(nums)):
        incoming = nums[i]
        outgoing = nums[i - k]

        # Add incoming element
        insert(incoming, max_heap, min_heap)

        # Mark outgoing element for lazy deletion

        # Note - "We use lazy deletion because heaps have no efficient remove(value) operation —
        # searching and removing from the middle costs O(n). Lazy deletion keeps everything O(log n)."
        # "It is safe to wait because a buried invalid element never affects heap[0] — and we only use heap[0] for median. We only need to discard it when it floats to the top."
        to_remove[outgoing] = to_remove.get(outgoing, 0) + 1

        # Clean tops of both heaps if marked
        # while max_heap and -max_heap[0] in to_remove:
        #     val = -max_heap[0]
        #     to_remove[val] -= 1
        #     if to_remove[val] == 0:
        #         del to_remove[val]  # clean up!
        #     heapq.heappop(max_heap)

        # while min_heap and min_heap[0] in to_remove:
        #     val = min_heap[0]
        #     to_remove[val] -= 1
        #     if to_remove[val] == 0:
        #         del to_remove[val]  # clean up!
        #     heapq.heappop(min_heap)

        # Replacement of both while loop
        for heap, sign in [(max_heap, -1), (min_heap, 1)]:
            while heap and sign * heap[0] in to_remove:
                val = sign * heap[0]
                to_remove[val] -= 1
                if to_remove[val] == 0:
                    del to_remove[val]
                heapq.heappop(heap)

        # Rebalance and get median
        rebalance(max_heap, min_heap)
        result.append(get_median(max_heap, min_heap))

    return result

# Test
print(median_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
