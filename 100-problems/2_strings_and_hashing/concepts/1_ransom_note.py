# Given two strings ransomNote and magazine, return true if ransomNote can be constructed using the letters from magazine.
# Each letter in magazine can only be used once.

# Example - 
# ransomNote = "aa", magazine = "ab" → False
# ransomNote = "aa", magazine = "aab" → True
from collections import Counter


# Solution 1
# TC - O(n+m), n = len(ransomNote), m = len(magazine)
# SC - O(k) - unique characters only storing
def is_ransom_note(ransomNote, magazine):
    if len(magazine) < len(ransomNote):
        return False
    ransom_dict = {}
    for i in ransomNote:
        ransom_dict[i] = ransom_dict.get(i,0) + 1
    
    for j in magazine:
        ransom_dict[j] = ransom_dict.get(j,0) - 1
    print(ransom_dict)
    return all(val <= 0 for val in ransom_dict.values())

# Solution 2: Using Counter
# TC - O(n)
def is_ransom_noteX(ransomNote, magazine):
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)
    
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True

# Solution 3: Using Counter, more pythonic
def is_ransom_noteY(ransomNote, magazine):
    return not (Counter(ransomNote) - Counter(magazine))


ransomNote = "aa"
magazine = "aaab"
print(is_ransom_note(ransomNote, magazine))