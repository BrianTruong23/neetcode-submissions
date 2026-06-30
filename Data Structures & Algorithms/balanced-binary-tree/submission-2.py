# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get the height for left and right 
        # if height for left is larger than right or right larger by left more than 1 then return false 
        # apply dfs to this and determine the height for right and left at each node
        # if right > left + 1 or left > right + 1 then return False 
        # so this function return True or False but also we keep track of height for left and right 
        # height
        # how about we have nonlocal variable to keep track true or false 

        def dfs(node):
            if not node:
                return 0 
            
            right = dfs(node.right)
            if right == -1:
                return -1
            left = dfs(node.left)
            if left == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return dfs(root) != -1


