# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        node_p, node_q = p, q
        stack = [[node_p, node_q]]
        
        while len(stack) > 0:
            cur_p, cur_q = stack.pop()
            print(cur_p.val, cur_q.val)
            if cur_p.val != cur_q.val:
                return False
            else:
                leftp, rightp = cur_p.left, cur_p.right
                leftq, rightq = cur_q.left, cur_q.right

                if leftp and leftq:
                    stack.append([leftp, leftq])
                elif leftp is None and leftq is None:
                    1
                else:
                    return False

                if rightp and rightq:
                    stack.append([rightp, rightq])
                elif rightp is None and rightq is None:
                    1
                else:
                    return False

        return True