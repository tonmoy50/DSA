# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = 0
        l1_t = l1
        i = 0
        while l1_t:
            l1_num += l1_t.val * (10**i)
            
            i += 1
            l1_t = l1_t.next
        
        l2_num = 0
        l2_t = l2
        i = 0
        while l2_t:
            l2_num += l2_t.val * (10**i)
            
            i += 1
            l2_t = l2_t.next
        
        result = l1_num+l2_num
        rt = result_node = ListNode(result % 10)
        result = result // 10
        while result != 0:
            rt.next = ListNode(result % 10)
            rt = rt.next

            result = result // 10
        
        return result_node