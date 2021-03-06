# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


def sortColors(self, nums):

    if not nums: return

    ind = [0] * 3
    
    for k, v in enumerate(nums):
        if k > ind[v]:
            temp = nums.pop(k)
            nums.insert(ind[temp], temp)

        ind[v:] = [i + 1 for i in ind[v:]]

# inplace O(N)
def sortColors(self, nums: List[int]) -> None:
    
    heads = [-1] * 3
    
    for i in range(len(nums)):
        temp = org = nums[i]
        while temp + 1 < len(heads):
            if heads[temp + 1] >= 0:
                if heads[org] < 0: heads[org] = heads[temp + 1]
                nums[heads[temp + 1]], nums[i] = nums[i], nums[heads[temp + 1]]
                heads[temp + 1] += 1
            temp += 1
        if heads[org] < 0: heads[org] = i
            
    return nums