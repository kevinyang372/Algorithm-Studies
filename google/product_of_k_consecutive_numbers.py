# Given an array of number nums and an int k. Return the product of every k consecutive numbers.

# Example:

# Input: nums = [1, 3, 3, 6, 5, 7, 0, -3], k = 3
# Output: [1, 3, 9, 54, 90, 210, 0, 0]
# Explanation: 1 (1), 3 (1x3), 9 (1x3x3), 54 (3x3x6), 90 (3x6x5), 210 (6x5x7), 0 (5x7x0), 0 (7x0x3)

def consecutiveProduct(nums, k):

    if k < 0 or not nums: return

    res = [1] * len(nums)
    product = 1
    behind = 1

    for i, v in enumerate(nums):

        if i >= k:
            behind = nums[i - k]

        product = product * v // behind
        res[i] = product

    return res