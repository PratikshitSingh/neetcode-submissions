# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr and stack:
            print(cur.val)

            if curr == stack[-1]: break
            if curr.next == stack[-1]: break

            next = curr.next
            curr.next = stack.pop()
            curr = curr.next
            curr.next = next

            curr = next
        
        return