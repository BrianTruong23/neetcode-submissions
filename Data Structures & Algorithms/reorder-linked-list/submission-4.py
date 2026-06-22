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

        # identify midpoint 
        slow = head 
        fast = head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next 

        # identify midpoint: checked! 
        # phase 2: reverse from midpoint 

        # print(fast.val)
        # print(slow.val)

        # split 
        second = slow.next 
        slow.next = None 

        # reversion 
        current = second # mid point 
        prev = None 
        while current is not None:
            next_ = current.next 
            current.next = prev 
            prev = current 
            current = next_

        # print(prev.val)

        # merge alternating list 
        first = head 
        second = prev 

        while second is not None:
            next_first = first.next 
            next_second = second.next 

            first.next = second 
            second.next = next_first 

            first = next_first 
            second = next_second 


        # l1 = head 
        # l2 = prev 

        # last = None
        # while l2 != None and l1 != None: 
        #     next_l1 = l1.next 
        #     next_l2 = l2.next

        #     l1.next = l2
        #     l2.next = next_l1

        #     if next_l1 == None:
        #         last = l2 

        #     l1 = next_l1 
        #     l2 = next_l2

        # last.next = l2 



         
        