# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tempnode = second.next
            second.next = prev
            prev = second
            second = tempnode
        
        fnode, snode = head, prev
        while snode:
            node1, node2 = fnode.next, snode.next
            fnode.next = snode
            snode.next = node1
            fnode, snode = node1, node2
        