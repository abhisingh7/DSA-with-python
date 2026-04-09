# Given a list of intervals, merge all overlapping ones.

# Input:  [[1,3], [2,6], [8,10], [15,18]]
# Output: [[1,6], [8,10], [15,18]]

# Explanation: [1,3] and [2,6] overlap → merged into [1,6]

# The full approach is:-

# 1. Sort intervals by start time — so we process them left to right
# 2. Scan through and check if current interval overlaps with previous
# 3. Merge if they overlap — merged interval end = max(a_end, b_end)
# 4. Add if they don't overlap — just push as new interval


# TC - O(n logn), SC - O(n)
def merge_intervals(intervals):
    # Step 1: sort by start time
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]  # start with first interval

    for i in range(1, len(intervals)):
        last = result[-1]      # last merged interval
        current = intervals[i] # interval we're examining

        # Step 2: check overlap condition
        if current[0] <= last[1]: # b_start <= a_end  →  they overlap
            # Step 3: merge — update the end of last interval
            result[-1][1] = max(last[1], current[1]) # max(a_end, b_end)
        else:
            # Step 4: no overlap — add as new interval
            result.append(current)

    return result


# Edge case 1: Normal overlapping
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# [[1,6],[8,10],[15,18]] ✅

# Edge case 2: One interval completely inside another
print(merge_intervals([[1,8],[2,3]]))
# [[1,8]] ✅ — max(8,3) = 8, correctly keeps the larger end

# Edge case 3: No overlaps at all
print(merge_intervals([[1,2],[3,4],[5,6]]))
# [[1,2],[3,4],[5,6]] ✅

# Edge case 4: All intervals merge into one
print(merge_intervals([[1,4],[2,5],[3,6]]))
# [[1,6]] ✅

# Edge case 5: Already sorted
print(merge_intervals([[1,3],[2,6]]))
# [[1,6]] ✅

# Edge case 6: Single interval
print(merge_intervals([[1,5]]))
# [[1,5]] ✅

# Edge case 7: Touching intervals — [1,3] and [3,5]
print(merge_intervals([[1,3],[3,5]]))
# [[1,5]] ✅ — 3 <= 3 triggers merge, correct!