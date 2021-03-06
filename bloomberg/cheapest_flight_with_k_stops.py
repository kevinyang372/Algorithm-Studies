# There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
# Note:

# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.

def findCheapestPrice(self, n, flights, src, dst, K):
        
    costs = {}
    graph = collections.defaultdict(list)
    
    for x, y, c in flights:
        graph[x].append(y)
        costs[x, y] = c
        
    frontier = [(costs[src, y], y, 0) for y in graph[src]]
    heapq.heapify(frontier)
    
    visited = {}
    visited[src, 0] = 0
    
    while frontier:
        cost, node, trans = heapq.heappop(frontier)
        if node == dst: return cost
        
        if trans < K:
            trans += 1
            for n in graph[node]:
                if visited.get((n, trans), float('inf')) > cost + costs[node, n]:
                    visited[n, trans] = cost + costs[node, n]
                    heapq.heappush(frontier, (cost + costs[node, n], n, trans))
    return -1

# TLE
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    d = collections.defaultdict(dict)
    
    for s, e, c in flights:
        d[s][e] = c
    
    @lru_cache
    def search(node, k):
        if node == dst: return 0
        if k == 0 or not d[node]: return float('inf')
        
        return min(d[node][other] + search(other, k-1) for other in d[node])
    
    res = search(src, K +  1)
    if res == float('inf'): return -1
    return res