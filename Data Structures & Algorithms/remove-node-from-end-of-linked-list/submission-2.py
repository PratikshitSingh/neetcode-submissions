# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1. n=0: => head.next
        2. i+=1 until i==n-1
            - c.next = c.next.next
        """
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        f = l-n

        if f == 0:
            return head.next
        
        curr = head
        i = 0
        while i < f-1:
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        return head
