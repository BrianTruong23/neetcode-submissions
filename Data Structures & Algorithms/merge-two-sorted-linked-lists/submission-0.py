# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # we should have nodes from list1 and list2 
        # Dummy nodes for the head of the resulting linked list and go through each list to build up this resulting linked list 
        # we have a  marker at list1 and list2 
        # marker_list_1 will be the head of list_1 and marker_list_2 will be the head of list2 
        # if  list_1.val < list2.val:
        #       append a new node for list_1 into the resulting list 
                # the list 1 will get incremented 
        # else:
        #       append an new node for list_2 into the resulting list 
        #       the list 2 will get incremeneted 

        # do this until list_1 | list_2 are None
        # if list 1 is still not empty append to the resulting list 
        # if list 2 is still not empty append to the resulting list 

        head = ListNode()
        current = head 

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next 
                
            current = current.next

        while list1:
            current.next = ListNode(list1.val)
            list1 = list1.next 
            current = current.next 

        while list2:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next  

        return head.next  


