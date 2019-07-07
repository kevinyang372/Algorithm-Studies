# There are n flights, and they are labeled from 1 to n.

# We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

# Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

# Example 1:

# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]
 

# Constraints:

# 1 <= bookings.length <= 20000
# 1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
# 1 <= bookings[i][2] <= 10000

def corpFlightBookings(bookings, n):
        
    res = [0] * n
        
    for i in bookings:
        res[i[0] - 1] += i[2]
        
        if i[1] < n:
            res[i[1]] -= i[2]
        
    print(res)
    a = res[0]
    
    for i in range(1, n):
        res[i], a = a + res[i], a + res[i]
    
    return res