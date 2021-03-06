# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

 

# Example 1:



# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

# Note:

# You must return the copy of the given head as a reference to the cloned list.

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

cache = {}
def copyRandomList(head):

    if not head: return
    if head in cache: return cache[head]

    h = Node(head.val, None, None)
    cache[head] = h

    h.next = copyRandomList(head.next)
    h.random = copyRandomList(head.random)

    return h

# O(N) hashmap
def copyRandomList(self, head):
    if not head: return
    d = {}
    new_head = Node(head.val, None, None)
    d[head] = new_head
    
    while head:
        cur = d[head]
        
        if head.next in d:
            cur.next = d[head.next]
        elif head.next:
            node = Node(head.next.val, None, None)
            d[head.next] = node
            cur.next = d[head.next]
        
        if head.random in d:
            cur.random = d[head.random]
        elif head.random:
            node = Node(head.random.val, None, None)
            d[head.random] = node
            cur.random = d[head.random]
        
        head = head.next
    
    return new_head

def copyRandomList(self, head: 'Node') -> 'Node':
    node = head
    
    d = {}
    while node:
        d[node] = Node(node.val)
        node = node.next
    
    node2 = head
    while node2:
        d[node2].random = d.get(node2.random, None)
        d[node2].next = d.get(node2.next, None)
        node2 = node2.next
    
    return d.get(head, None)