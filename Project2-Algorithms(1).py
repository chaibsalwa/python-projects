"""
Algorithmic Problem Solver
Author: Salwa Chaib
Description: Efficient solutions for common coding interview problems
"""

def find_two_sum(nums, target):
    """Find indices of two numbers that add up to target - O(n) solution"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def is_palindrome(s: str) -> bool:
    """Check if string is palindrome ignoring spaces and case"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def fibonacci(n: int) -> int:
    """Efficient Fibonacci with memoization"""
    memo = {0: 0, 1: 1}
    def fib(k):
        if k not in memo:
            memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    return fib(n)

# Tests
if __name__ == "__main__":
    print("Two Sum:", find_two_sum([2,7,11,15], 9))  # [0,1]
    print("Palindrome 'A man a plan':", is_palindrome("A man, a plan, a canal: Panama"))  # True
    print("Fibonacci 10:", fibonacci(10))  # 55
    print("All tests passed!")
