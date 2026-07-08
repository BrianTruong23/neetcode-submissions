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
        
        current = head 
        dummy = Node(0)
        headCopy = dummy
        mapping = {}

        while current:

            # create new node
            newNode = Node(current.val)

            # assign currentCopy.next to this new new
            dummy.next = newNode

            # assign to hash map 
            mapping[current] = newNode

            # get to the next one for current copy 
            dummy = dummy.next 
            # get to the next one for current
            current = current.next 

        current = head 
        dummy = headCopy.next

        while current:
            # print(current.val)
            # assign random pointer now
            dummy.random = mapping.get(current.random) 

            current = current.next 
            dummy = dummy.next 
        
        return headCopy.next


# time complexity: O(n)
# space complexity: O(n)



