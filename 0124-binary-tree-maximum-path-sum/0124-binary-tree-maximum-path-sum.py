# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftmax = max(dfs(root.left), 0)
            rightmax = max(dfs(root.right), 0)

            maxsum[0] = max(maxsum[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        return maxsum[0]