# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeD = ListNode(0, head)
        nodeS = nodeD
        nodeF = head
        
        while n > 0:
            nodeF = nodeF.next
            n -= 1
        
        while nodeF:
            nodeS = nodeS.next
            nodeF = nodeF.next
        
        nodeS.next = nodeS.next.next

        return nodeD.next