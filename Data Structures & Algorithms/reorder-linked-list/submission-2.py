# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #   Stage 1: mid point 
    #   Stage 2: reverse from mid point forward 
    #   Stage 3: reorder by connecting l1 and l2 reverse. 

        l0 = None
        l1 = head 
        l2 = head 

        while l2 != None and l2.next != None:
            l0 = l1 
            l1 = l1.next 
            l2 = l2.next.next 

        if l0 != None:
            l0.next = None

        # identify midpoint: checked! 
        # phase 2: reverse from midpoint 

        # reversion 
        current = l1 # mid point 
        prev = None 
        while current != None:
            next_ = current.next 
            current.next = prev 
            prev = current 
            current = next_

        print(prev.val)

        l1 = head 
        l2 = prev 

        last = None
        while l2 != None and l1 != None: 
            next_l1 = l1.next 
            next_l2 = l2.next

            l1.next = l2
            l2.next = next_l1

            if next_l1 == None:
                last = l2 

            l1 = next_l1 
            l2 = next_l2

        last.next = l2 



         
        