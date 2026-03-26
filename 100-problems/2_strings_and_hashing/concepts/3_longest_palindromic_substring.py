# Longest Palindromic Substring - (Medium Difficulty)
# Given a string s, return the longest substring that is a palindrome.

# Example -
# Input:  "babad"  → Output: "bab" or "aba"
# Input:  "cbbd"   → Output: "bb"


# Solution 1 - TC - O(n^2), SC - O(1)
def longest_palindromic_substr(word):
    longest = ""
    for i in range(len(word)):
        # odd center
        odd_palindrome = expand(word,i,i)
        # even center
        even_palindrome = expand(word, i, i+1)
        # max palindrome track
        current  = max(odd_palindrome, even_palindrome, key = len)
        # print(current)   
        if len(current) > len(longest):
            longest = current
    return longest

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # when loop ends, left and right have gone ONE step too far
    # so the actual palindrome is s[left+1 : right]
    return s[left+1 : right]

# print(longest_palindromic_substr("babad"))

# Solution 2 - Index based mathematical calculation (faster but TC, SC same)
def longest_palindromic_substrX(s):
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expandX(s, i, i)     # odd
        len2 = expandX(s, i, i+1)   # even
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2 # (i - distance) => distance = (len -1)//2
            end = i + max_len // 2         # (i + distance) => distance = len//2

    return s[start:end+1]

def expandX(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Python was creating new strings every time → extra hidden cost
    # Using indices for better optimization
    return right - left -1

# print(longest_palindromic_substrX("babad"))

# Solution 3 - Returning all longest palindromes
# Time → O(n²)
# Space → O(k) (number of longest palindromes)
def all_longest_palindromes(s):
    if not s:
        return []

    max_len = 0
    result = set()

    for i in range(len(s)):
        # odd length
        l1 = expandY(s, i, i)
        # even length
        l2 = expandY(s, i, i+1)

        for left, right in [l1, l2]:
            curr_len = right - left + 1

            if curr_len > max_len:
                max_len = curr_len
                result = {s[left:right+1]}   # reset
            elif curr_len == max_len:
                result.add(s[left:right+1])

    return list(result)


def expandY(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return left + 1, right - 1

print(all_longest_palindromes('babad'))

# Solution 4 is also possible with Manacher's algorithm with TC-O(n)
# But it is complext and not required for interview level.
# but good for Competitive level