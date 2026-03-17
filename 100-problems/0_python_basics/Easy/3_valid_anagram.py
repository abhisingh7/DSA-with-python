# Leetcode Problem 3: Valid Anagram
# Link - https://leetcode.com/problems/valid-anagram/description/

from collections import Counter


# 1. Simplest Brute Force solution - Time Complexity O(nlogn) -  Space Complexity - O(n)
def isAnagram(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# 2. Using Dictionary without any module - Time Complexity O(n) -  Space Complexity - O(1)    
def isAnagramX(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        return True


# 3. Cleanest Python way using Counter
# Time Complexity - O(n) - Space Complexity - O(n) if not all character lowercase otherwise O(1)
def isAnagramY(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# 4. Most Optimized Solution with one loop 
# Time Complexity - O(n) - Space Complexity - O(1)
def isAnagramZ(s: str, t: str) -> bool:
    if len(s) != len(t):
            return False
    freq = {}
    
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0) + 1
        freq[t[i]] = freq.get(t[i],0) - 1
    
    return all(val == 0 for val in freq.values())    

print(isAnagramZ("anagram", "nagaram"))