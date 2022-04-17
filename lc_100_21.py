"""
Runtime: 43 ms, faster than 72.85% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 82.49% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            t = head = ListNode(list1.val)
            list1 = list1.next
        else:
            t = head = ListNode(list2.val)
            list2 = list2.next
        
        
        
        
        while list1 is not None and list2 is not None :
            if list1.val < list2.val:
                head.next =  ListNode(list1.val)
                list1 = list1.next
            else:
                head.next =  ListNode(list2.val)
                list2 = list2.next
            head = head.next
            

            
            
        while list1 is not None:
            head.next =  ListNode(list1.val)
            head = head.next
            list1 = list1.next
        
        while list2 is not None:
            head.next =  ListNode(list2.val)
            head = head.next
            list2 = list2.next
            
        
        return t
