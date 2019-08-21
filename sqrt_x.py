# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

# cheating
def mySqrt(self, x):
    return int(x ** 0.5)

# binary search
def mySqrt(self, x):
    if x == 1: return 1
    low, high = 0, x

    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid