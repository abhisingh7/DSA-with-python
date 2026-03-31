# Leetcode Problem 10: group-anagrams
# Link - https://leetcode.com/problems/group-anagrams/description/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3
# Input: strs = ["a"]
# Output: [["a"]]

from typing import List
from collections import defaultdict


# 1. Brute Force - TC - O(n^2), SC - O(n)
def groupAnagram(strs: List[str]) -> List[List[str]]:
    output = []
    seen = set()
    if len(strs) == 0 or strs == [""]:
        output.append([""])
        return output
    elif len(strs) == 1:
        output.append([strs[0]])
        return output
    sorted_strs = [ ''.join(sorted(str)) for str in strs]
    
    for i in range(len(sorted_strs)):
        if i in seen:
            continue
        temp = [strs[i]]
        seen.add(i)
        for j in range(len(strs)):
            if i!=j:
                if (sorted_strs[i] == sorted_strs[j]) and (j not in seen):
                    temp.append(strs[j])
                    seen.add(j)
        output.append(temp)

    return output

# 2. optimized solution(Dictionary + sorted) - TC - O(n* klog k) , SC - O(n)
# sorting each word taking klogk
def groupAnagramX(strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

# Same solution Using default dict
# TC - O(n · k log k), SC - O(n · k)
def groupAnagramY(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())

# 3. Most Optimized(Dict + char count)
# TC - O(n*k) - Count characters in O(k) instead of sorting in O(k log k)
def groupAnagramOptimized(strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    
    for word in strs:
        # Count character frequencies - O(k)
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        
        # Use tuple as key (must convert list to tuple for hashing)
        key = tuple(char_count)

        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Same Solution using default dict
def groupAnagramOptimizedX(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        anagram_map[tuple(count)].append(word)
    
    return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagramY(strs))
# print(groupAnagramOptimized(strs))