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

        count, ans = 0, None

        def dfs(node):

            nonlocal count, ans

            if not node or ans is not None:
                return 
            
            dfs(node.left)

            count += 1
            if count == k:
                ans = node
            
            dfs(node.right)
        
        dfs(root)
        return ans.val

            

