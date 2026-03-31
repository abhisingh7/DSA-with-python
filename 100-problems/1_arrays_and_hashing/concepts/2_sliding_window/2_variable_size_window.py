"""
Problem - Find the length of longest substring without repeating characters.
s = "abcabc"
"""
# TC - O(n), SC - O(k)
def longest_unique_substring(s):
    seen = {}  # char -> index
    slow = 0
    max_len = 0

    for fast in range(len(s)):
        if s[fast] in seen and seen[s[fast]] >= slow:
            slow = seen[s[fast]] + 1       # jump past the duplicate
        seen[s[fast]] = fast               # update/store latest index
        max_len = max(max_len, fast - slow + 1) 
        # fast - slow + 1 — since fast always moves forward now, window length is just the distance between the two pointers.
    # print(s[slow:fast+1])
    return max_len

s = "abcabc"
print(longest_unique_substring(s))


"""
Note - Pattern for longest window sliding problem
for fast in range(len(input)):
    1. Expand window by including s[fast]
    2. Shrink window from left to right if condition violated
    3. Update answer based on current window.
"""