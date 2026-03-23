"""
Problem - Given two strings s and t. Find the minimum length substring of s that contains all characters of t(including duplicates)

Example 1 - 
s = "ADOBECODEBANC"
t = "ABC"
output = "BANC"

Example 2 - 
s = "MBADBC"
t = "BBC"
output = "BADBC"
"""



# Solution 1 - TC -  O(n * k) where k = unique chars in t
# SC - O(n + m) where m = len(t)
def is_valid(t_count, window_count):
    for k in t_count:
        if t_count[k] > window_count.get(k, 0):
            return False
    return True


def minimum_window_substring(s, t):
    t_count = {}
    window_count = {}
    slow = 0
    min_len = float('inf')
    start = 0

    for i in t:
        t_count[i] = t_count.get(i, 0) + 1

    for fast in range(len(s)):
        window_count[s[fast]] = window_count.get(s[fast], 0) + 1

        while is_valid(t_count, window_count):
            if fast - slow + 1 < min_len:
                min_len = fast - slow + 1
                start = slow
            window_count[s[slow]] -= 1
            slow += 1

    return "" if min_len == float('inf') else s[start:start + min_len]


# Test
# s = "ADOBECODEBANC"
# t = "ABC"
# print(minimum_window_substring(s, t))  # "BANC"

#########################################################################################

# Solution 2 - TC -  O(n) but faster because of filtering irrelevant characters
# SC - O(n + m) where m = len(t)

def minimum_window_substringX(s, t):
    # count required frequency of each character in t
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1

    window_count = {}       # tracks current frequency of chars in window
    slow = 0                # left boundary of window
    min_len = float('inf')  # infinity = no valid window found yet
    start = 0               # start index of the minimum window
    required = len(t_count) # no. of unique chars that need to be satisfied
    formed = 0              # no. of unique chars currently satisfied in window

    for fast in range(len(s)):
        c = s[fast]

        # skip characters that aren't in t — they can't help satisfy the window
        if c not in t_count:
            continue

        # expand window: include current character
        window_count[c] = window_count.get(c, 0) + 1

        # check if this character just became fully satisfied
        if window_count[c] == t_count[c]:
            formed += 1

        # window is valid — try shrinking from left to find minimum
        while formed == required:

            # skip irrelevant chars from left — they don't affect validity
            while s[slow] not in t_count:
                slow += 1

            # update minimum window if current one is smaller
            if fast - slow + 1 < min_len:
                min_len = fast - slow + 1
                start = slow  # record where minimum window starts

            # shrink window: remove leftmost character
            window_count[s[slow]] -= 1

            # check if removing this char broke its satisfaction
            if window_count[s[slow]] < t_count[s[slow]]:
                formed -= 1

            slow += 1  # move left boundary forward

    # if min_len never updated, no valid window existed
    return "" if min_len == float('inf') else s[start:start + min_len]


# Tests
print(minimum_window_substringX("ADOBECODEBANC", "ABC"))  # "BANC"
print(minimum_window_substringX("AABCBBA", "AAB"))        # "AAB"
print(minimum_window_substringX("MBADBC", "BBC"))         # "BADBC"
print(minimum_window_substringX("ABC", "XY"))             # ""

"""
Note - Pattern for shortest window sliding problem
1. Expand window by including s[fast]
2. Shrink window from left as long as condition is SATISFIED
3. Update minimum window while shrinking
"""