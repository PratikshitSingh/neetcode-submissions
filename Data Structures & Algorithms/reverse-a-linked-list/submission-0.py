"""
Idea:
1. Iteration:
    -> prev, curr, next
    -> curr.next = prev
    -> prev = curr
    -> curr = next
    -> next = curr.next

until curr != null

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        curr = prev.next
        prev.next = None 
        nest = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nest
            if curr:
                nest = curr.next
        
        return prev