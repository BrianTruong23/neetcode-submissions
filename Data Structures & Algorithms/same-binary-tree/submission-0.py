# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, node2):

            if not node and not node2:
                return True 
            
            if not node or not node2 or node.val != node2.val:
                return False 
            
            left = dfs(node.left, node2.left)
            if not left:
                return False 
            
            right = dfs(node.right, node2.right)
            if not right:
                return False 
            
            return left and right 

        return dfs(p, q) 

