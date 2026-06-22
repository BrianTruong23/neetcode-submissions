# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # naive: put into array 
        # next better: two counter pass: to get the length and then go through to remove nth node 
        # better: one counter pass: slow start first, fast: start at nth node ahead. 
        # (sz - n)
        # (sz - n) + n = sz 
        # The question is can we get sz - n in the first pass

        # 1, 2, 3, 4, 5, 6, 7, 8 / n = 3 / 8 - 3 = 5 / go back to the head and remove that 
        # or reverse linked list and then go from the head to that nth node and remove it 
        # but need to reverse back to return the right head 
        
        # can we use fast and slow pointer 
        # 1, 2, 3, 4
        # slow: 1, 2, 3 (after slow, we have mid point)
        # fast: 1, 3, none (after fast we have length) 

        # 1, 2, 3, 4, 5 
        # n = 3
        # slow: first (1)
        # fast: n-th node ahead of first (4)
        # slow goes through the list and fast will reach null
        # when fast reaches null, slow is before the node that needs to be eliminated 
        # then set that node to the next of the node to be eliminated 

        # 1, 2, 3, 4, 5 
        # n = 5 




        # 1 
        # n = 1 
        # slow = 1 
        # fast = none 
        # 

        slow = head 
        fast = head 
        count = 0

        while fast != None:
            fast = fast.next 
            count += 1 
            if count == n:
                break 

        if fast == None:
            if n == 1:
                return None 
            else:
                # remove the head 
                return head.next 

        # print(fast.val)

        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next 
        
        # print(slow.val)
        next_ = slow.next 
        slow.next = next_.next

        return head
        



