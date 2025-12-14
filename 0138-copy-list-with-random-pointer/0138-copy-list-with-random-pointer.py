"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maps = {None: None}

        old = head
        while old:
            maps[old] = Node(old.val)
            old = old.next

        old = head
        while old:
            new_ref = maps[old]
            new_ref.next = maps[old.next]
            new_ref.random = maps[old.random]


            old = old.next
        
        return maps[head]