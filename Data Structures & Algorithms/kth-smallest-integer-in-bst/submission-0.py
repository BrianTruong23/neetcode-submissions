# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # actually we can merge the left and right 
        # at the end we return k for the list 

        def dfs(node):

            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left + [node.val] + right
        
        array = dfs(root)

        return array[k - 1]




            
            

