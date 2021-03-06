# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the i-th domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

 

# Example 1:



# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.

# using set
def minDominoRotations(A, B):
    s = {A[0], B[0]}
    d = collections.defaultdict(int)
    length = len(A)
    
    for i in range(len(A)):
        s = s.intersection({A[i], B[i]})
        if not s:
            return -1
        for t in s:
            if t == B[i] and t == A[i]:
                length -= 1
            elif t == B[i]:
                d[t] += 1
           
        
    return min(d[list(s)[0]], length - d[list(s)[0]])

# use dictionary to track
def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    if A[0] != B[0]:
        to_swap = {A[0]: {0: 0, 1: 1}, B[0]: {0: 1, 1: 0}}
    else:
        to_swap = {A[0]: {0: 0, 1: 0}}
    
    for i in range(1, len(A)):
        temp = {}
        if A[i] == B[i]:
            if A[i] in to_swap:
                temp[A[i]] = to_swap[A[i]]
                to_swap = temp
                continue
            else:
                return -1
        else:
            if A[i] in to_swap:
                to_swap[A[i]][1] += 1
                temp[A[i]] = to_swap[A[i]]
       
            if B[i] in to_swap:
                to_swap[B[i]][0] += 1
                temp[B[i]] = to_swap[B[i]]
        
        if not temp:
            return -1
        
        to_swap = temp
    
    return min(min(to_swap[i][0], to_swap[i][1]) for i in to_swap)