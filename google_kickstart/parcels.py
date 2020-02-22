# You have been hired recently as the Chief Decision Maker (CDM) at a famous parcel delivery company, congratulations! Customers love speedy deliveries of their parcels and you have decided to decrease the time it takes to deliver parcels around the world to win customers. You have introduced this idea to the authorities and they have allocated you enough budget to build at most one new delivery office.

# The world can be divided into an R × C grid of squares. Each square either contains a delivery office or it does not. You may pick a grid square that does not already contain a delivery office and build a new delivery office there.

# The delivery time of a parcel to a square is 0 if that square contains a delivery office. Otherwise, it is defined as the minimum Manhattan distance between that square and any other square containing a delivery office. The overall delivery time is the maximum of delivery times of all the squares. What is the minimum overall delivery time you can obtain by building at most one new delivery office?

# Note: The Manhattan distance between two squares (r1,c1) and (r2,c2) is defined as |r1 - r2| + |c1 - c2|, where |*| operator denotes the absolute value.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains the number of rows R and number of columns C of the grid. Each of the next R lines contains a string of C characters chosen from the set {0, 1}, where 0 denotes the absence of a delivery office and 1 denotes the presence of a delivery office in the square.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum overall delivery time you can obtain after adding at most one additional delivery office.

# Limits
# Time limit: 15 seconds per test set.
# Memory limit: 1GB.
# 1 ≤ T ≤ 100.
# There is at least one delivery office in the initial grid.

# Test set 1 (Visible)
# 1 ≤ R ≤ 10.
# 1 ≤ C ≤ 10.

# Test set 2 (Hidden)
# 1 ≤ R ≤ 250.
# 1 ≤ C ≤ 250.

# Sample

# Input
    
# Output
 
# 3
# 3 3
# 101
# 000
# 101
# 1 2
# 11
# 5 5
# 10001
# 00000
# 00000
# 00000
# 10001

  
# Case #1: 1
# Case #2: 0
# Case #3: 2

  
# In Sample Case #1, you get a minimum overall delivery time of 1 by building a new delivery office in any one of the five squares without a delivery office.

# In Sample Case #2, all the squares already have a delivery office and so the minimum overall delivery time is 0. Note you have to add at most one delivery office.

# In Sample Case #3, to get a minimum overall delivery time of 2, you can build a new delivery office in any of these squares: (2, 3), (3, 2), (3, 3), (3, 4), or (4, 3). Any other possibility results in a higher overall delivery time than 2.

import collections

def calculateMinDistance(board):
    
    current_stations = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 1]
    
    def getPoints(K):
        
        queue = collections.deque(list(current_stations))
        visited = {pos: 0 for pos in current_stations}
        res = []

        while queue:
            x, y = queue.popleft()
            dis = visited[x, y]
            if dis > K: res.append((x, y))

            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if -1 < x + di < len(board) and -1 < y + dj < len(board[0]) and (x + di, y + dj) not in visited:
                    queue.append((x + di, y + dj))
                    visited[x + di, y + dj] = dis + 1
        
        return res

    def checkPossible(points, K):

        if not points: return True

        upper_s, lower_s = max(i + j for i, j in points), min(i + j for i, j in points)
        upper_d, lower_d = max(i - j for i, j in points), min(i - j for i, j in points)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in current_stations:
                    if max(abs(upper_s - (i + j)), abs(lower_s - (i + j)), abs(upper_d - (i - j)), abs(lower_d - (i - j)))<= K:
                        return True

        return False
    
    l, r = 0, len(board) + len(board[0])
    while l <= r:

        mid = l + (r - l) / 2
        points = getPoints(mid)

        if checkPossible(points, mid):
            r = mid
        else:
            l = mid + 1

    return l

T = int(input())
for i in range(T):
    R, C = map(int, input().split(' '))
    board = []
    
    for _ in range(R):
        board.append(list(map(int, input().split(' '))))

    print("Case #%s: %s" % (i + 1, calculateMinDistance(board)))