# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head

        while curr:
            sz += 1
            curr = curr.next

        x = sz - n
        curr = head
        prev = None

        if not x:
            return head.next

        while curr and x:
            prev = curr
            curr = curr.next
            x -= 1
        
        prev.next = curr.next
        return head