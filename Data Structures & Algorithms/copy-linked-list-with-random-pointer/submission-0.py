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
        currentCopy = Node("0")
        copyHead = currentCopy
        hashMap = {}

        while current != None:

            # create new node
            newNode = Node(current.val)

            # assign currentCopy.next to this new new
            currentCopy.next = newNode

            # assign to hash map 
            hashMap[current] = newNode

            # get to the next one for current copy 
            currentCopy = currentCopy.next 
            # get to the next one for current
            current = current.next 

        current = head 
        currentCopy = copyHead.next

        while current != None:
            # print(current.val)
            # assign random pointer now 
            if current.random != None:
                currentCopy.random = hashMap[current.random] 
            else:
                currentCopy.random = None

            current = current.next 
            currentCopy = currentCopy.next 
        
        return copyHead.next


