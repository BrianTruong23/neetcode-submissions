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

        # move nth step ahead for one pointer 
        # remove the node after the slow pointer because that is before the node need to be eliminated 
        # first move fast up to nth node (O(n))
        # then move fast all the way to the end: O(L)
        # move slow all the way to L - n: O(L - n)
        # so we have O(n) + O(L) + O(L - n) + O(1) for removal because n < L so still O(L)
        # therefore, it is O(L) 
        # also we have a dummy node for special case where we remove the head 
        

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy 
        count = 0 
        # first move fast up to n + 1 
        while fast != None and count < n + 1:
            count += 1
            fast = fast.next 
        
        if fast != None:
            print(fast.val)

        while fast != None:
            slow = slow.next
            fast = fast.next 
        
        slow.next = slow.next.next 

        return dummy.next 
