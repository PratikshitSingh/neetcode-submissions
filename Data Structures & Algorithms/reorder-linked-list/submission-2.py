# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        n = 0
        
        while curr:
            stack.append(curr)
            curr = curr.next
            n += 1

        i = 0
        curr = head
        while i < n//2:
            nxt = curr.next
            lst = stack.pop()
            curr.next = lst
            lst.next = nxt

            curr = nxt

            i += 1
        
        curr.next = None