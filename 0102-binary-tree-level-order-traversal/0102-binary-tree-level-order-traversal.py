# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        val_list = list()
        node_list = [[root]]
        
        while len(node_list) > 0:
            temp_node = list()
            temp_val = list()

            nodes = node_list.pop()
            for node in nodes:
                temp_val.append(node.val)

                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)

            val_list.append(temp_val)
            if len(temp_node) > 0:
                node_list.append(temp_node)
        
        return val_list