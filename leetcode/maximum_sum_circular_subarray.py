# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

# Example 1:

# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# Example 2:

# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# Example 3:

# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# Example 4:

# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# Example 5:

# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 

# Note:

# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000

def maxSubarraySumCircular(self, A):
    if not A: return 0
    
    dp = [0] * len(A) * 2
    min_sum = float('inf')
    res = -float('inf')
    
    for i, v in enumerate(A):
        if i == 0:
            dp[i] = v
        else:
            dp[i] = dp[i - 1] + v
            
        res = max(res, dp[i] - min_sum)
        min_sum = min(dp[i], min_sum)
    
    sums = [float('inf')] * len(A)
    
    for t in range(len(A) - 1, -1, -1):
        if t == len(A) - 1:
            sums[t] = dp[t]
        else:
            sums[t] = min(sums[t + 1], dp[t])
    
    for i, v in enumerate(A):
        dp[i + len(A)] = dp[i + len(A) - 1] + v
        res = max(res, dp[i + len(A)] - sums[i])
        
    return res

# min queue
def maxSubarraySumCircular(self, A: List[int]) -> int:
    total = 0
    min_sum = collections.deque([0])
    record = [0]
    res = -float('inf')
    
    for i, v in enumerate(A + A):
        total += v
        if i - len(A) > -1 and record[i - len(A)] == min_sum[0]: min_sum.popleft()
        
        if min_sum:
            res = max(res, total - min_sum[0])
        else:
            res = max(res, total)
        
        while min_sum and min_sum[-1] > total: min_sum.pop()
        min_sum.append(total)
        record.append(total)
        
    return res