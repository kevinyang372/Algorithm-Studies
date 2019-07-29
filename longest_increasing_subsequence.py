# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

# O(NlogN)
def lengthOfLIS(self, nums):

    d = [0] * len(nums)
    size = 0

    for x in nums:
        i, j = 0, size
        while i != j:
            mid = (i + j) // 2
            if d[mid] < x:
                i = mid + 1
            else:
                j = mid
        d[i] = x
        size = max(i + 1, size)

    return size