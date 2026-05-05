# LeetCode → Problem 253 (Medium)

# Input:  intervals = [[0,30],[5,10],[15,20]]
# Output: 2  (minimum meeting rooms required)


# Corrected timeline:-

# Minute: 0    5    10   15    20       30
#         |----A--------------------------|
#              |--B--|
#                         |--C--|

# So:

# [0, 30] → starts at minute 0, ends at minute 30
# [5, 10] → starts at minute 5, ends at minute 10
# [15, 20] → starts at minute 15, ends at minute 20

# Rule - Always reuse the room whose end time is closest to but still before the new meeting's start time.
import heapq

# TC - O(n log n)
# Sorting - O(n log n)
# Heap operation - O(n log n)
# Total - O(n log n)
def min_meeting_rooms(intervals):
    # Step 1: sort by start time
    intervals.sort(key=lambda x: x[0])

    heap = []  # stores end times

    for start, end in intervals:
        if heap and heap[0] <= start:
            # Room is free! Reuse it
            # Pop old end time, push new end time
            heapq.heappushpop(heap, end)
        else:
            # No free room
            # Allocate new room
            # Push new end time
            heapq.heappush(heap, end)

    return len(heap)

# Test
intervals = [[0,30],[5,10],[15,20]]

print(min_meeting_rooms(intervals)) # 2