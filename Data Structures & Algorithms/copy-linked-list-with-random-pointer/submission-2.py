"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # have a copy head 
        # the problem is how to copy the random node
        # without random, we have 
        # first pass: create the copy of all nodes
        # create a hash map to map the original nodes to the copy of its node 
        # then second pass: assign random pointers

        if not head:
            return None 
        
        mapping = {}
        current = head 

        # first pass: create deep copy of the original list in interleaving fashion
        while current:
            nextCurrent = current.next 
            newNode = Node(current.val)
            current.next = newNode
            newNode.next = nextCurrent
            current = nextCurrent

        current = head
        # second pass 
        while current:
            if current.random:
                    current.next.random = current.random.next 
            current = current.next.next   
        # A -> A' -> B -> B' -> C -> C'
        # A's random is C
        # Then how do we get A' to connect with C'
        # current: A 
        # current.next.random = current.random.next 
        # only do this when counter is even 

        # third pass: separate into the list 
        current = head 
        copyHead = head.next 
        copyReturnedHead = head.next 

        while current:
            current.next = copyHead.next 

            if copyHead.next:
                copyHead.next =  copyHead.next.next
            
            current = current.next

            if current:
                copyHead = current.next 
        # head -> copyHead 
        # A -> A' -> B -> B'
        # at A: we want it connect to B
        # then move on to B next 

        return copyReturnedHead 
     


# more optimized technique includes O(1) for space when using interleaving nodes in the original list 
# then we have three passes: one pass, create the copies in the list, second pass: assign random pointer and third pass get a separate list for the copy and return the head 

# time complexity: O(n)
# space complexity: O(n)

#    if not head:
#             return None 
        
#         current = head 
#         dummy = Node(0)
#         headCopy = dummy
#         mapping = {}

#         while current:

#             # create new node
#             newNode = Node(current.val)

#             # assign currentCopy.next to this new new
#             dummy.next = newNode

#             # assign to hash map 
#             mapping[current] = newNode

#             # get to the next one for current copy 
#             dummy = dummy.next 
#             # get to the next one for current
#             current = current.next 

#         current = head 
#         dummy = headCopy.next

#         while current:
#             # print(current.val)
#             # assign random pointer now
#             dummy.random = mapping.get(current.random) 

#             current = current.next 
#             dummy = dummy.next 
        
#         return headCopy.next



