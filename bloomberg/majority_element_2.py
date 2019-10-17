# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

def majorityElement(self, nums):
    if not nums: return
    bound = len(nums) // 3
    d = []
    
    for i in set(nums):
        if nums.count(i) > bound:
            d.append(i)
    
    return d