# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        node_stack = [root]
        while len(node_stack) > 0:
            cur_node = node_stack.pop(-1)
            left, right = cur_node.left, cur_node.right
            cur_node.left = right
            cur_node.right = left
            if right:
                node_stack.append(right)
            if left:
                node_stack.append(left)



        return root