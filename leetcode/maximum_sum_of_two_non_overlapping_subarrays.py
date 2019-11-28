# Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

# Example 1:

# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
# Example 2:

# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
# Example 3:

# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

# Note:

# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000

# dynamic programming + prefix sum
def maxSumTwoNoOverlap(self, A, L, M):
    dp_1, dp_2 = [0] * len(A), [0] * len(A)
    
    prefix = sum(A[:L])
    dp_1[L - 1] = prefix
    
    for l in range(L, len(A)):
        prefix += A[l] - A[l - L]
        dp_1[l] = max(dp_1[l - 1], prefix)
        
    suffix = sum(A[len(A) - L:])
    dp_2[len(A) - L] = suffix
    
    for l in range(len(A) - L - 1, -1, -1):
        suffix += A[l] - A[l + L]
        dp_2[l] = max(dp_2[l + 1], suffix)
        
    start = sum(A[:M])
    max_val = start + dp_2[M]
    
    for s in range(M, len(A)):
        start += A[s] - A[s - M]
        if s == len(A) - 1:
            max_val = max(max_val, start + dp_1[s - M])
        else:
            max_val = max(max_val, start + dp_2[s + 1], start + dp_1[s - M])
        
    return max_val