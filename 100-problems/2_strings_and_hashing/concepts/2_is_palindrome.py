# check if a word is palindrome or not.
def is_palindrome(word):
    left = 0
    right = len(word) -1
    
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# print(is_palindrome('poops'))


# Leetcode (Easy difficulty)- Check if a string contains only alphanumeric characters is palindrome or not 
# - using two pointers.

# Example - 
# "A man, a plan, a canal: Panama" → True
# "race a car"                     → False

def is_palindrome_str(sentence):
    sentence = sentence.lower()
    left = 0
    right = len(sentence) -1

    while left < right:
        if not sentence[left].isalnum():
            left += 1
            continue
        
        elif not sentence[right].isalnum():
            right -= 1
            continue
        elif sentence[left] == sentence[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

# sentence = "A man, a plan, a canal: Panama" 
sentence = "race a car" 
print(is_palindrome_str(sentence))