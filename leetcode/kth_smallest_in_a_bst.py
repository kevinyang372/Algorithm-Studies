# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, k):

    if not root: return

    stack = [root]
    seen = set()
    count = 0

    while stack:
        node = stack[-1]

        if node.left and node.left not in seen:
            stack.append(node.left)
        else:
            count += 1
            if count == k: return node.val

            stack.pop()
            seen.add(node)
            if node.right: stack.append(node.right)

    return 

def kthSmallest(self, root, k):
        
    def traverse(node, t):
        origin = t
        if node.left:
            res, num = traverse(node.left, t)
            if res is not None: return res, None
            t -= num
            
        if t == 1: 
            return node.val, None
        
        if node.right:
            res, num = traverse(node.right, t - 1)
            if res is not None: return res, None
            t -= num
            
        return None, origin - t + 1
    
    return traverse(root, k)[0]


def kthSmallest(self, root: TreeNode, k: int) -> int:
    d = {}
    def traverse(node, kth):
        if node.left: kth = traverse(node.left, kth) + 1
        d[kth] = node.val
        if node.right: kth = traverse(node.right, kth + 1)
        return kth
    
    traverse(root, 1)
    return d[k]