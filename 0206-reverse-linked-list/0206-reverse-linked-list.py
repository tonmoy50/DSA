# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, h = None, head
        while h and h.next:
            t = h.next
            h.next = prev
            prev = h
            h = t
        
        if h:
            h.next = prev
            new_head = ListNode(next=h)
        return h