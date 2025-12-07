# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedlist = m = ListNode()
        l1, l2 = (list1 if list1 else None), (list2 if list2 else None)

        while 1:
            if l1 == None:
                m.next = l2
                break
            elif l2 == None:
                m.next = l1
                break
            
            if l1.val <= l2.val:
                m.next = l1
                l1 = l1.next
            else:
                m.next = l2
                l2 = l2.next
            m = m.next
        
        return mergedlist.next