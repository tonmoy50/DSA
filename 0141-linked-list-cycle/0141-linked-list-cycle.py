# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeF, nodeS = head, head

        while nodeF and nodeF.next:
            nodeF = nodeF.next.next
            nodeS = nodeS.next
            if nodeF == nodeS:
                return True
        
        return False