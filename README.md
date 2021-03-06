# Algorithm Studies

## 1. Arrays

### Time Complexities
* Retrieval and update - O(1)
* Insertion (with resizing) - O(1)
* Deletion (moving all successive elements to the left) - O(N)
* Slicing - O(k) k is the slice size
* __IMPORTANT!__ - Set functions differently from array which needs only O(1) time for lookup

### Key Functions
* `bisect.bisect`: find a position in list where an element needs to be inserted to keep the list sorted
  * `bisect_left` and `bisect_right`: only different when the element is already in the list. `bisect_left` inserts into the leftmost position and `bisect_right` inserts into the rightmost position
  * You could also pass a `lo` (default: 0) or `hi` (default: length of the input) parameter to find the index within that range
* `insort`: insert an element to the list while keeping the list as sorted.
```python
import bisect
a = [1,2,3,5]
bisect.bisect(a, 4)
# returns 3
bisect.insort(a, 4)
# a = [1,2,3,4,5]
bisect.bisect(a, 4, lo=0, hi=2)
# returns 2
```
* How copy works: <br>
  __shallow copy__: constructing a new collection object and then populating it with references to the child objects found in the original <br>
  __deep copy__: first constructing a new collection object and then recursively populating it with copies of the child objects found in the original
```python
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # shallow

xs[1][0] = 'X'
print(ys) # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]

import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.deepcopy(xs) # deep

print(ys) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* List comprehension with multiple levels of looping
```python
A = [1,3,5]
B = ['A','B','C']
[(x, y) for x in A for y in B]
```
* Slicing `list[x:y:z]` means slice the list starting from x and ending at y with step size of z
```python
a = list(range(100))
# Most common - reversing
a[::-1]

# Every even element in a
a[::2]

# Every odd element in a
a[1::2]

# Every 3rd element before 50
a[:50:3]
```
* Sort one array based on the value of another
```python
a = [2, 6, 1]
b = [1, 2, 3]

[y for x, y in sorted(zip(a, b))]
```
* (set) `A.issubset(B)` - check if a set is the subset of another
* (set) Get first element in a set - `next(iter(s))`

### Tips
* Filing an array from the front is slower than from behind (append)
* Overwritting is more time efficient than deleting

## 2. Strings

### Time Complexities
Strings are immutable
* Concatenating a single character - O(N)

### Key Functions
* `s.strip()`: remove the starting and ending empty spaces
* `s.startswith(prefix)` and `s.endswith(suffix)`
* `s.lower()`
* `s.isalnum()`: check if the string contains only alphanumeric character ('a-z/A-Z')
* `s.count(substring)`: count the number of substrings that exist in the given string

### Find All Substrings of A Given String
```python
s = 'abbac'
[s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
```

### Pattern Matching: KMP (Knuth Morris Pratt)
Given two strings s (the "search string") and t (the "text"), find the first occurrence of s in t
* Naive appoarch time complexity: O(MN)
* KMP optimize the time by precomputing a prefix-to-suffix table for the pattern
```python
def kmp(pattern, s):
    dp = [0] * len(pattern)
    
    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            dp[i] = j
            i += 1
        elif j == 0:
            i += 1
        else:
            j = dp[j - 1]
    
        
    i = j = 0
    while i < len(s):
        if s[i] == pattern[j]:
            i += 1
            j += 1
            
            if j == len(pattern):
                return i - j
        elif j > 0:
            j = dp[j - 1]
        else:
            i += 1
            
    return -1
```

### Pattern Matching: Rabin Karp
Given two strings s (the "search string") and t (the "text"), find the first occurrence of s in t
* Compute the hash of substrings and find matches for the hashs
* Optimize the time complexity to O(M + N) by using the 'rolling hashes' technic
```python
def rabin_karp(pattern, s):

    mod = 2 ** 63 - 1
    p = pow(26, len(pattern), mod)
    to_match = 0
    
    for c in pattern:
        to_match = (to_match * 26 + ord(c)) % mod
    
    start = 0
    for i in range(len(pattern)):
        start = (start * 26 + ord(s[i])) % mod
    
    if start == to_match: return True
    for i in range(0, len(s) - len(pattern)):
        start = (start * 26 + ord(s[i + len(pattern)]) - ord(s[i]) * p) % mod
        if start == to_match: return True
        
    return False
```

## 3. Linked Lists

### Time Complexities
* Insertion and deletion - O(1)
* Obtaining the kth element - O(N)

### Tips
* Use a _dummy head_ (with null value) to avoid having to check for empty lists
* Algorithms on linked lists usually benefit from using two iterators with one move faster than the other

### Linked List in Practice - OrderedDict
* Python's OrderedDict library maintains the key pair in the order of their insertion
  * `d.popitem()` removes the most recent key pair while `d.popitem(last=False)` removes the least recent one
* The OrderedDict is built with a hashmap and double linkedlist (keeps track of the head and tail)

## 4. Stacks And Queues

Stacks: LIFO (Last in first out)

Queues: FIFO (First in first out)

### Stack: Design A Stack That Includes A Max Operation
* Using heap / BST / Hash Table - time complexity could be reduced to O(logN) / space complexity increases to O(N)
* Using single variable to record the max is very time consuming on popping action
* Improve time complexity by caching (Every insertion records the element as well as the current max)

```python
class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.cache = []

    def push(self, x):
        self.stack.append(x)
        if self.cache:
            self.cache.append((max(x, self.cache[-1]), min(x, self.cache[-1])))
        else:
            self.cache.append((x, x))

    def pop(self):
        self.cache.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMax(self):
        return self.cache[-1][0]
        
    def getMin(self):
        return self.cache[-1][1]
```
* Max Frequnency Stack (Stack of stacks approach)

```python
class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.stacks = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        self.freq[x] = self.freq.get(x, 0) + 1
        if self.freq[x] > self.maxfreq:
            self.maxfreq = self.freq[x]
        self.stacks[self.maxfreq].append(x)

    def pop(self):
        x = self.stacks[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.maxfreq]:
            self.maxfreq -= 1
        return x
```

### Monotonic Stack
Given an unsorted list, find all indexes (i, j) such that j > i, A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, select the smallest possible j.
* Naive approach: O(N^2)
* Monotonic stack: O(NlogN)

```python
def findPairs(A):
   min_ind = [-1] * len(A)

   inds = sorted(range(len(A)), key=lambda x: (A[x], x))
   stack = []

   for i in range(len(inds)):
       while stack and inds[i] >= stack[-1]:
           n = stack.pop()
           min_ind[n] = inds[i]
       stack.append(inds[i])
      
   return min_ind
```

### Monotonic Queue
[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
* `Max`, `Push`, `Remove` all in O(1) time
```python
class MonotonicQueue:
    # the q keeps track of two elements
    # 1 - the value
    # 2 - how many elements have been deleted between two nodes
    def __init__(self):
        self.q = collections.deque()
        
    def push(self, ele):
        if not self.q:
            self.q.append([ele, 0])
            return
        
        count = 0
        while self.q and self.q[-1][0] < ele:
            _, num = self.q.pop()
            count += num + 1
        
        self.q.append([ele, count])
    
    # remove from front
    def remove(self):
        if self.q[0][1] == 0:
            self.q.popleft()
        else:
            self.q[0][1] -= 1
    
    def max(self):
        return self.q[0][0]
```

## 5. Binary Trees

### Traversing
* Inorder traversal (left - root - right)
* Preorder traversal (root - left - right)
* Postorder traversal (left - right - root)
* Morris inorder traversal (inorder traversal with constant space)

Morris inorder traversal
```python
def morrisInorder(root):

    res = []

    while root:
        if not root.left:
            res.append(root.val)
            root = root.right
        else:
            predecessor = find_predecessor(root.left)

            if not predecessor.right:
                predecessor.right = root # link node to remember the sequence
                root = root.left
            else:
                predecessor.right = None
                res.append(root.val)
                root = root.right

    return res

def find_predecessor(root):
    base = root.val
    while root.right and root.right.val < base:
        root = root.right

    return root
```

Iterative Inorder traversal
```python
def inorderTraversal(self, root):
    if not root: return []
    
    stack = [root]
    res = []
    visited = set()
    
    while stack:
        node = stack[-1]
        
        if node.left and node.left not in visited: #check if left child has been visited
            stack.append(node.left)
        else:
            res.append(node.val)
            stack.pop()
            visited.add(node)
            if node.right:
                stack.append(node.right)
                
    return res
```

Segment Tree (For Range Sum questions)
```python
class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.start = start
        self.end = end
        self.sums = val # can also be max / min
        self.left = None
        self.right = None
    
# O(N) time
def buildTree(start, end, vals):
    if start == end:
        return SegmentTreeNode(vals[start], start, end)
    mid = (start + end) // 2
    left = buildTree(start, mid, vals)
    right = buildTree(mid + 1, end, vals)
  
    cur = SegmentTreeNode(left.sums + right.sums, start, end)
    cur.left = left
    cur.right = right
  
    return cur

# O(logN) time
def updateTree(root, index, val):
    if root.start == root.end == index:
        root.sums = val
        return root
    mid = (root.start + root.end) // 2
  
    if index > mid:
        updateTree(root.right, index, val)
    else:
        updateTree(root.left, index, val)
   
    root.sums = root.left.sums + root.right.sums
  
# O(logN + k) time
def querySum(root, i, j):
    if root.start == i and root.end == j:
        return root.sums
    mid = (root.start + root.end) // 2
  
    if i > mid:
        return querySum(root.right, i, j)
    elif j <= mid:
        return querySum(root.left, i, j)
    else:
        return querySum(root.left, i, mid) + querySum(root.right, mid + 1, j)
```

Binary Indexed Tree (For Prefix Sum)
```python
class BinaryIndexedTree:
    def __init__(self, arr):
        self.bit = [0] * (len(arr) + 1)
        self.construct(arr)
        
    def update(self, ind, val):
        
        ind += 1
        while ind < len(self.bit):
            self.bit[ind] += val
            ind += ind & -ind
    
    def construct(self, arr):
    
        for i, v in enumerate(arr):
            self.update(i, v)
    
    def sums(self, ind):
    
        ind += 1
        s = 0
        while ind > 0:
            s += self.bit[ind]
            ind -= ind & -ind
        
        return s
```

### Time Complexities
Most tree problems could be solved with recursion, whose time complexity depends on the depth of recursion (O(h) - h is the tree height). Notice this could be translated to `O(logN)` for balanced trees and `O(N)` for skewed trees.

### Serialization and Deserialization
* Use pre-order traversal to serialize the binary tree (add special token when the node doesn't have left/right child)
* Deserialize the tree by breaking down the string recursively

```python
def serialize(root):
    if not root: return "#"
    left = serialize(root.left)
    right = serialize(root.right)
    res = ','.join([str(root.val), left, right])
    return res
    
def deserialize(str):
    s = data.split(',')
        
    def deserializer(s):
        root = s.pop()
        if root == '#': return None
        node = TreeNode(root)
        node.left = deserializer(s)
        node.right = deserializer(s)

        return node
        
    return deserializer(s[::-1])
```

### Serialization and Deserialization of BST
* Use pre-order traversal (no special token needed)
* Deserialize by utilizing the lower and upper bound

```python
def serialize(root):
    if not root: return ""
    res = [str(root.val)]
    if root.left:
        res.append(serialize(root.left))
    if root.right:
        res.append(serialize(root.right))
    res = ','.join(res)
    return res

def deserialize(str):
    if not data: return 
    s = data.split(',')
        
    def deserializer(s, lower, upper):
        if not s or int(s[-1]) < lower or int(s[-1]) > upper: return None
        root = int(s.pop())
        node = TreeNode(root)
        node.left = deserializer(s, lower, root)
        node.right = deserializer(s, root, upper)

        return node
        
    return deserializer(s[::-1], -float('inf'), float('inf'))
```

## 6. Heaps

_heap property_: the key at each node is at least as great as the keys stored at its children

### Time Complexities
* Insertion - O(logN)
* Lookup for max/min - O(1)
* Deletion of max/min - O(logN)
* Searching for arbitrary keys - O(N)

### Key Functions
* `heapq.heapify(L)`: transforms the element in L into a heap in-place
* `heapq.nlargest(k, L)` / `heapq.nsmallest(k, L)`: returns k largest/smallest elements in L
* `heapq.heappush(h, e)`: pushes a new element on the heap
* `heapq.heappop(h)`: pops the smallest element from the heap
* `heapq.heappushpop(h, a)`: pushes a on the heap and then pops the smallest element
* `e = h[0]`: returns the smallest element on the heap

### Tips:
* Use a heap when all you care about is the largest or smallest elements (with no need to support fast lookup / search / delete for arbitrary elements)
* A heap is a good choice when you need to compute k largest or k smallest elements

## 7. Searching

### Binary Search - Elimination-based Strategy

```python
def bsearch(t, A):
  L, U = 0, len(A) - 1
  while L <= U:
    M = L + (U - L) / 2 # Using (U + L) // 2 may cause overflow
    if A[M] > t:
      L = M + 1
    elif A[M] == t:
      return M
    else:
      U = M - 1
  return -1
```

### Search a Sorted Array for First Occurrence of k
Naive Solution: Use binary search to find k. Then continue from the resulting index forward until it does not equal to k.
* Average Time Complexity: O(logN)
* Worst-case Time Complexity: O(N)

Improved Solution: Use binary search to find k. Record the occurrence and continue to use binary search.
* Average Time Complexity: O(logN)
* Worst-case Time Complexity: O(logN)

```python
def findFirstOccurrence(t, A):
    L, U = 0, len(A) - 1
    occurrence = len(A)
  
    while L <= U:
        M = L + (U - L) / 2
        if A[M] > t:
            L = M + 1
        elif A[M] == t:
            occurrence = M
            U = M - 1
        else:
            U = M - 1
      
    return occurrence 
```

### Find the kth Smallest / Largest Element in an Unsorted Array
Naive Solution: Sort the array and find the kth element (O(NlogN))

Improved Solution: Quick Select (O(N))

```python
def kthLargest(num, k):
    if k < 1: return -1
    pivot = random.randint(0, len(num) - 1)
    smaller, equal, larger = [], [], []
    
    for i in num:
        if i < num[pivot]:
            smaller.append(i)
        elif i == num[pivot]:
            equal.append(i)
        else:
            larger.append(i)
            
    if len(smaller) >= k:
        return kthLargest(smaller, k)
    elif len(smaller) + len(equal) >= k:
        return equal[0]
    else:
        return kthLargest(larger, k - len(smaller) - len(equal))
```

### Standard BFS:
DFS could be done with simple recursion. But BFS needs to be done with queues.

```python
def bfs(d):
    dist, m, n = 1, nRows, nColumns
    queue = [(0, 0)]
    visited = set([(0, 0)])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  
    while queue:
        temp = []
        for i, j in queue:
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if success:
                        temp.append((ni, nj))
                        visited.add((ni, nj))
            
        queue = temp
        dist += 1
    return dist
```

### A* Algorithm
A* is another path-finding algorithm with better performance in both time and space. It discovers the shortest path by maintaining a priority queue ordered by the estimated sum of distance traveled from the start point and heuristic distance from the end point (usually the manhattan distance `abs(end_x - cur_x) + abs(end_y - cur_y)`)
* Find all the reachable points one step away from the current position
* Add them into the priority queue (if the point is already in the priority queue, update its cost if the current cost is lower)
* Continue the same process until reaching the target position

```python
import heapq

def astar(mat, sx, sy, tx, ty):
    lx, ly = len(mat), len(mat[0])
    heap = [(0, 0, sx, sy)]
    cost = {(sx, sy): 0}
  
    while heap:
        cur_cost, distance, x, y = heapq.heappop(heap)
        if x == tx and y == ty: return distance
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= x + dx < lx and 0 <= y + dy < ly and mat[x + dx][y + dy] != obstacle:
                nx, ny = x + dx, y + dy
                new_cost = distance + 1 + abs(tx - nx) + abs(ty - ny)
                if new_cost < cost.get((nx, ny), float('inf')):
                    cost[nx, ny] = new_cost
                    heapq.heappush(heap, (new_cost, distance + 1, nx, ny))
          
    return -1
```

### Union Find
DSU (Disjoint Set Union) is a data structure that can be used to maintain the knowledge of connected components in a graph. Union Find is an algorithm that allows path compression and quick query over DSU. It contains two main operations:
1. `find`: finds the 'ancestor' of a node in the graph
2. `union`: draws an edge (x, y) in the graph, connecting the two components together.

```python
class DSU:
    def __init__(self):
        self.p = range(1001)
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
```

### Minimum Spanning Tree
Given a connected weighted undirected graph, find the subset that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
* Greedy approach:
  * Find the edge with minimum weight
  * If the edge won't cause a cycle, add it to the tree
  * Continue until finding N - 1 edges where N is the number of vertices

```python

# edges is in the format of (cost, node 1, node 2)

def minimumSpanningTree(n, edges):
        
    uf = range(n + 1)
    
    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]
    
    res = 0

    for cost, n1, n2 in sorted(edges):
        x, y = find(n1), find(n2)
            
        if x != y:
            uf[x] = y
            res += cost
            n -= 1
        
        if n == 0:
            return res
```

## 8. Sorting

### Topological Sort
A _topological ordering_ is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B. (__Topological sort can only be appplied upon Directed Acyclic Graph (DAG)__)
* Pick a node with zero incoming edges
* Adding the node to topological ordering
* Decrease the incoming edges count for neighbors of the node

```python
def topologicalSort(graph):
    degree = collections.defaultdict(int)
    
    for node in graph:
        for neighbor in graph[node]:
            degree[neighbor] += 1
    
    queue = collections.deque([node for node in graph if degree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)
         
   return order
```

## Idiomatic Python

### For / Else
* Help get rid of the flag variables
* Two scenarios:
  * Finish the loop without encountering `break` -> entering else
  * Finish the loop encountering `break` -> exit
```python
for item in items:
    if encounter(conditions):
        dosomething()
        break
else:
    # conditions not satisfied
    dosomethingelse()
```

### Delete items in Dictionary in Iteration
* Use `list(d)`: create a copy of keys
* (For set): use filter e.g. `set(filter(lambda x: x % 2 == 0, A))`

```python
for i in list(d):
    if somecondition(i):
        del d[i]
```

### Creating Dictionary from Two Lists

```python
a = [1,2,3]
b = ['a','b','c']

d = dict(zip(a, b))
```

### @lru_cache
* Simple decorator fix for memoization
* Default maximum size of `@lru_cache` is 128 (Could be set to None)

```python
@lru_cache(maxsize=None)
def fib(N):
    if N < 2:
        return N
    return fib(N - 1) + fib(N - 2)
```

## Design Patterns

### Listener / Observer
* Observer has a list of listeners
* An update on observer is broadcasted to all listeners

### Singleton
* Limit Creation of a class to only one object
* Examples: caches, thread pools, registries
* Class initiation within a class (nested inner class)

### Model View Controller
* Model - Store the data
* View - Display the data
* Controller - Modify the data

### Factory Method
* Allow the creation of product objects without specifying thier concrete classes (interface)
* Create a class that defines a method that is used for creating objects

## Tricky Questions

### Finding All Prime Numbers within a Given Limit - Sieve of Eratosthenes
1. Initially, let p equal 2, the smallest prime number.
2. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list.
3. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Let p equal to that new number. Repeat step 2.
4. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

__e.g. Count the number of prime numbers less than a non-negative number, n.__
```python
def countPrimes(n):
    if n < 2: return 0

    filled = [1] * n
    filled[0] = 0
    filled[1] = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if filled[i] == 1:
            for j in range(i*i, n, i):
                filled[j] = 0

    return sum(filled)
```

### Greatest Common Divisor of Strings
Input: str1 = "ABCABC", str2 = "ABC"<br>
Output: "ABC"
1. Initially, set str1 to be the longer string and str2 to be the shorter string
2. Check if str2 is the prefix of str1
3. Recursively check for the remainder of str1 and str2

```python
def gcdOfStrings(str1, str2):

    if len(str1) == len(str2):
        return str1 if str1 == str2 else ''
    else:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[:len(str2)] == str2:
            return gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
```

### Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

```python
def reverseBits(n)
    res = 0
    for _ in range(32):
        res = (res << 1) + (1 & n) # notice the parentheses here as bit operation has low priority
        n >>= 1
  return n
```

### Longest Increasing Subsequence
Given an unsorted array of integers (`nums`), find the length of longest increasing subsequence.

__O(N^2) solution intuition__
* The longest subsequence at index i equals to the longest subsequence at j (where `nums[i]` > `nums[j]`) + 1
* To solve the entire problem, we can create an array with length n (which equals to len(nums))
* Loop through 1 to len(n) - 1 and calculate the LIS at each index
```python
def LIS(nums):
    if not nums: return 0
  
    LIS = [1] * len(nums)
    for i in range(1, len(LIS)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
  
    return max(LIS)
```

__O(NlogN) solution intuition__
* Maintain a list `N` where `N[i]` represents the tail of the increasing subsequence with length i + 1
* Apply one of the two actions for each element in the list:
  * When the new element is larger than every tail, increase the size by one to insert the new element (LIS size + 1)
  * When the new element is smaller than `N[x]`, replace largest `N[x]` with the new element (LIS size unchanged)
  
```python
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

# or with bisect_left
def lengthOfLIS(self, nums):
    d = [0] * len(nums)
    size = 0

    for x in nums:
        i = bisect.bisect_left(d[:size], x)
        d[i] = x
        size = max(i + 1, size)

    return size
```

### Longest Common Subsequence (LCS)

_A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements._

Given two strings `word1` and `word2`. Find the length of longest common subsequence between them.<br>
Intuition:
* If `word1[-1] == word2[-1]`, then the longest common subsequnce is equal to `1 + lcs(word1[:-1], word2[:-1])`
* If `word1[-1] != word2[-1]`, then the longest common subsequnce is equal to `max(lcs(word1[:-1], word2), lcs(word1, word2[:-1]))`

Dynamic Programming Approach (O(N^2))
```python
def minDistance(self, word1, word2):
    h1, h2 = len(word1) + 1, len(word2) + 1
    mat = [[0] * h1 for _ in range(h2)]
        
    mat[0][0] = 0
        
    for i in range(1, h2):
        for t in range(1, h1):
            if word1[t - 1] == word2[i - 1]:
                mat[i][t] = 1 + mat[i - 1][t - 1]
            else:
                mat[i][t] = max(mat[i - 1][t], mat[i][t - 1])
        
    return mat[h2 - 1][h1 - 1]
```

### Minimum Window Substring - Sliding Window
General Approach for Sliding Window Questions:
* We have two pointers: the _right pointer_ expands the current window while the _left pointer_ contracts it
* At any point in time, only one of these pointers move and the other remains fixed

__Minimum Window Substring question:__

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n). Example: Input: S = "ADOBECODEBANC", T = "ABC"; Output: "BANC"

```python
def minWindow(s, t):

    if not s or not t: return ''

    l = r = 0
    ans = (float('inf'), 0, 0)

    dic = collections.Counter(t)
    required = len(dic)
    formed = 0

    window = collections.defaultdict(int)

    while r < len(s):
        cur = s[r]
        window[cur] += 1

        if cur in dic and window[cur] == dic[cur]:
            formed += 1

        if formed == required:
            while l <= r and formed == required:
                window[s[l]] -= 1

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    formed -= 1

                l += 1
        r += 1

    return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
```

### Compare Strings with BitMask
Given two strings (with only lower characters), find if they have common letters.
* The most common approach would be converting both strings to sets and check their intersection
  * This takes O(M * N) time and O(M + N) space
* We could convert each string into a bitmask with size 26 (1 if the string has that character, 0 if not)
* Use bit operation `&` to check the intersection
* This takes O(M + N) time and O(1) space

```python
def checkIntersection(s1, s2):

    # bitmask of size 26
    bitmask = lambda ch: ord(ch) - ord('a')
    b1 = b2 = 0
    
    for i in s1:
        b1 |= 1 << bitmask(i)
    for t in s2:
        b2 |= 1 << bitmask(t)
    
    return b1 & b2 != 0
```

### 0-1 Knapsack Problem (Dynamic Programming)
Given a list of items with weight and value as well as the maximum weight you can carry. Find the most value you are able to bring.
* This could be framed as a recursion problem:
  * `maxVal(list, max_weight)` = `max(maxVal(list[1:], max_weight), maxVal(list[1:], max_weight - list[0].weight) + list[0].value)`
  * In other words, given an item in the list, select the item or not.
* The time complexity could be optimized with dynamic programming

```python
def knapSack(W, wt, val, n): 
    K = [[0 for _ in range(W+1)] for _ in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]
```

### N-Sum
Given a list of integers. Find N integers that give the sum of `target` value.
* Recursively reduce N to N - 1
* Handle the subproblem when reduced to 2 sum

```python
def Wrapper(nums, target, N):
    results = []
    nSum(sorted(nums), target, N, [], results)
    return results

def nSum(nums, target, N, result, results):
    if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N: return 
    
    for i in range(0, len(nums) - N + 1):
        if i == 0 or nums[i] != nums[i - 1]:
            if N == 3:
                twoSum(nums[i + 1:], target - nums[i], result + [nums[i]], results)
            else:
                nSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

def twoSum(nums, target, result, results):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            results.append(result + [nums[i], nums[j]])
            i += 1
            
            while i < j and nums[i] == nums[i - 1]:
                i += 1
        elif s < target:
            i += 1
        else:
            j -= 1
```

### Best Time to Buy and Sell Stock (General Approach)
* There are three possible actions to do: `buy`, `sell`, `hold`
* We could define one specific state with three variables:
  * i - day number
  * k - number of transactions left
  * h - whether we are holding the stock or not
* Initial state:
  * T[-1][k][0] = 0 (Profit is zero to start with)
  * T[-1][k][1] = -infinity (It is impossible to hold a stock before start)
  * T[i][0][0] = 0 (Profit will always be zero if transaction is not possible)
  * T[i][0][1] = -infinity (It is impossible to hold a stock if one could do zero transaction)
* Update Function
  * T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i]) -- holding / selling
  * T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i]) -- holding / buying

### Median of Two Sorted Array
* We are trying to find a point X in arr1 and Y in arr2 which satisfies the following condition:
  * `X + Y = (len(arr1) + len(arr2)) // 2`
  * `max(arr1[X - 1], arr2[Y - 1]) <= min(arr1[X], arr2[Y])`
* We could progressively achieve that condition by applying binary search on the shorter array. Time complexity: O(log(N))
```python
def findMedianSortedArrays(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)

    if not nums1:
        if len(nums2) % 2 == 1:
            return nums2[len(nums2) // 2]
        else:
            return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2.0
        
    if nums1[0] >= nums2[-1]:
        if total % 2 == 1:
            return nums2[total // 2]
        else:
            if len(nums1) == len(nums2):
                return (nums1[0] + nums2[-1]) / 2.0
            else:
                return (nums2[total // 2] + nums2[(total - 1) // 2]) / 2.0
    elif nums1[-1] <= nums2[0]:
        if total % 2 == 1:
            return nums2[total // 2 - len(nums1)]
        else:
            if len(nums1) == len(nums2):
                return (nums1[-1] + nums2[0]) / 2.0
            else:
                return (nums2[total // 2 - len(nums1)] + nums2[(total - 1) // 2 - len(nums1)]) / 2.0

    i = len(nums1) // 2
    j = total // 2 - i

    lower, upper = 0, len(nums1)

    while max(nums1[i - 1], nums2[j - 1]) > min(nums1[i], nums2[j]):
        print(i, j)
        if nums1[i - 1] > nums2[j]:
            upper = i
        else:
            lower = i + 1
        i = (lower + upper) // 2
        j = total // 2 - i

    if total % 2 == 1:
        return min(nums1[i], nums2[j])
    else:
        return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2.0
```

### LRU Cache
* Solve the problem using doubly linked list
  * Define two dummy node ('head' and 'tail')
  * When a key is set/get, unlink the node and move it to the front
  * When the capacity is reached, unlink and delete the last node
```python
class LRUCache(object):
    
    class Node(object):
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.cap = capacity
        self.d = {}
        self.head = self.Node('head', 'head')
        self.tail = self.Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1
        self.insertatfront(self.unlinknode(self.d[key]))
        return self.d[key].val

    def put(self, key, value):
        if key in self.d:
            self.d[key].val = value
            self.insertatfront(self.unlinknode(self.d[key]))
        else:
            if len(self.d) >= self.cap:
                del self.d[self.unlinknode(self.tail.prev).key]
            self.d[key] = self.Node(key, value)
            self.insertatfront(self.d[key])
    
    def unlinknode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        
        return node
    
    def insertatfront(self, node):
        node.next, self.head.next = self.head.next, node
        node.prev, node.next.prev = self.head, node
```

### [Reservoir Sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
Assume we have a linked list with unknown length, how do we sample one node uniformly from the list in __one pass__?
* Pick first element (probability 1).
* Traverse through the linked list. For the kth node, pick it with probability 1/k (replace the current pick).
```python
class RandomLinkedListSampler(Object):

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        chosen = None
        node = self.head
        i = 1
        
        while node:
            if random.random() <= 1/i:
                chosen = node.val
            node = node.next
            i += 1
        
        return chosen
```
