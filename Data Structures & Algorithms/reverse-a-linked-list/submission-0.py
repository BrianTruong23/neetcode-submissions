# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # we have val and next 
        # we can have another value for current and prev to keep track of current value and prev 
        # and using prev, current to make the reverse happen 

        # so we go through each element starting with the first head starter and then 
            # prev initialized as None 
            # while next != None 
                # next_el = current.next
                # current.next = prev 
                # prev = current 
                # current = next_el 
            # then go through the list while applying these three operations
            # return prev

        prev = None 
        current = head 

        while current != None:
            next_el = current.next 
            current.next = prev 
            prev = current 
            current = next_el 
        
        return prev 