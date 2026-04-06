# Merge Sort - The Core Idea First

# Imagine you have a messy deck of cards. You're too overwhelmed to sort all of them at once. So you split the deck in half, give one half to your left hand and one to your right.
# Each half still feels too big, so you split again. You keep splitting until every pile has just 1 card — and a single card is already sorted by definition.
# Now you merge those piles back together — always picking the smaller card first from either pile.
# Two sorted piles of 1 become a sorted pile of 2. Two sorted piles of 2 become a sorted pile of 4. And so on, until you have one fully sorted deck.

# That's Merge Sort. Split until trivial. Merge back up.

# Best, Worst, Average - TC - O(nlogn), SC- O(n) - extra arrays created.

# Why O(n log n) time?

# You split log n times (halving each time → log n levels)
# At each level, you do O(n) work to merge
# Total: n × log n

# Why O(n) space?

# You create new arrays during merging — that's the cost. Merge Sort is not in-place.

# Best For - Linked lists, external sort

def merge_sort(arr):
    # BASE CASE: array of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # SPLIT: find the midpoint and divide
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])   # recursively sort left half
    right = merge_sort(arr[mid:])   # recursively sort right half

    # MERGE: combine two sorted halves into one sorted array
    print(f"left-{left}, right-{right}")
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0  # pointer for left array
    j = 0  # pointer for right array

    # Compare elements one by one from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One of the arrays is exhausted — dump the remainder
    # (remainder is already sorted, so just extend)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --- Test it ---
arr = [38, 27, 43, 3, 9, 82]
print(merge_sort(arr))  # [3, 9, 27, 38, 43, 82]