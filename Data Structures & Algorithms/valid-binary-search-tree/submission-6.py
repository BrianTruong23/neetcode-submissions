# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left and right 
        # left is awlays less than the node value 
        # right is alway larger than the node value 
        # there is a min and max on both sides 
        # on the irght it should be less than max and larger than min 
        # 

        # it is not only the path but also the entire subtree so at every number we should record the max and min value of the subtree

        def dfs(node, min_, max_):

            if not node:
                return True 
            
            if not (min_ < node.val < max_):
                return False 
            
            # when on the left, we update the max and on the right we update the min. 
            
            return dfs(node.left, min_, min(node.val, max_)) and dfs(node.right, max(node.val, min_), max_)


        return dfs(root, -1001, 1001)
