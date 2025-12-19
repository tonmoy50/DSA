# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 1
        stack = [[root, max_depth]]
        while len(stack) > 0:
            cur, depth = stack.pop()
            left, right = cur.left, cur.right
            if left:
                stack.append([left, depth+1])
                max_depth = max(max_depth, depth+1)
            if right:
                stack.append([right, depth+1])
                max_depth = max(max_depth, depth+1)
            
        
        return max_depth
    