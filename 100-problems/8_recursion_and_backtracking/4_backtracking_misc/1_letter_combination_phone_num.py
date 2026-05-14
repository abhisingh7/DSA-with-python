# LeetCode - 17 - Letter Combinations of a Phone Number (Medium)

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Problem - In a classic phone keypad -
# 2 → a, b, c
# 3 → d, e, f
# 4 → g, h, i
# 5 → j, k, l
# 6 → m, n, o
# 7 → p, q, r, s
# 8 → t, u, v
# 9 → w, x, y, z

# Input = 23 -> find all possible letter combinations:

# 2 → a, b, c
# 3 → d, e, f

# Answer: [ad, ae, af, bd, be, bf, cd, ce, cf]


def letter_combinations(digits):
    if not digits:
        return []

    result = []

    phone_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                 "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def solve(index, current):
        # base case
        if index == len(digits):
            result.append(current)
            return

        # get letters for current digit
        letters = phone_map[digits[index]]

        # iterate over each letter
        for letter in letters:
            solve(index+1, current + letter)

    solve(0, "")
    return result


# Test
input = "23"
print(letter_combinations(input))
# Result = [ad, ae, af, bd, be, bf, cd, ce, cf]
