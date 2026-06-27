# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def returnDepth(node, n):

            if not node:
                return n

            return max(returnDepth(node.left, n + 1), returnDepth(node.right, n + 1)) 
        
        return returnDepth(root, 0)
            
        