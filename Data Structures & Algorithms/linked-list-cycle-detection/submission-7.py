# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow cycle 
        # if fast and slow arrives at the same node then there is a cycle
        # if fast.next is None then we don't have a cycle 

        slow = head 
        fast = head 

        while fast and fast.next:
           
            slow = slow.next 
            fast = fast.next.next 

            if slow is fast:
                return True 

        return False 