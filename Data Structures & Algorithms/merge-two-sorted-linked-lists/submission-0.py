# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        head = None
        curr = None

        while p1 and p2:
            if p1.val <= p2.val: 
                n = p1
                p1 = p1.next
            else: 
                n = p2
                p2 = p2.next

            if not curr: 
                head = n
                curr = n
            else:
                curr.next = n
                curr = n
        
        while p1:
            if not curr: 
                head = p1
                curr = p1
            else:
                curr.next = p1
                curr = p1
            p1 = p1.next

        while p2:
            if not curr: 
                head = p2
                curr = p2
            else:
                curr.next = p2
                curr = p2
            p2 = p2.next

        return head