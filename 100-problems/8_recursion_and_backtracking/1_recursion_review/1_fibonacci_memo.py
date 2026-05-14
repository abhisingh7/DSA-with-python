# Leetcode - 509 Easy - Fibonacci Number - leetcode.com/problems/fibonacci-number

# Memoization = "If I already calculated this answer before, just remember it. Don't calculate again."
# Why -  because Fibonacci has overlapping subproblems.
# Overlapping Subproblems = same calculation needed multiple times → memoization saves the day.
# Fibonacci series are the sum of previous two numbers like - [0,1,1,2,3,5,8....]
# n = nth number in fibonacci sequence like fib(6) = 8


# 1 - Using Memorization technique
memo = {}

def fib(n):
    if n <= 1:
        return n

    # Step 1: Check if answer already exists in memo
    # Step 2: If yes → return that
    if n in memo:
        return memo[n]

    # Step 3: If no → calculate, STORE it, then return
    result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result

# 2 - Using Python's built-in decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

# Note - @lru_cache maintains the memo dictionary internally.
# Same logic, less code. Both approaches are valid in interviews