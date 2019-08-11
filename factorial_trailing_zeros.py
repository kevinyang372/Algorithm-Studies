# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:

# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.

# O(log_5(N))
def trailingZeroes(self, n):
    div, res = 5, 0
    
    while n >= div:
        res += n // div
        div *= 5
        
    return res