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
            print(curr.val)

            if curr == stack[-1] or curr.next == stack[-1]: 
                stack[-1].next = None
                break

            next = curr.next
            curr.next = stack.pop()
            curr = curr.next
            curr.next = next

            curr = next
        
        return