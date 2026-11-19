# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteration
        if not head or not head.next: return head

        prev = None
        curr = head # 0->1->2
        nxt = curr.next
        
        while nxt: # 2
            prev = curr # p=1
            curr = nxt #c=2
            nxt = curr.next #n=None

            curr.next = prev # 0-><-1<-2
        
        head.next=None
        return curr