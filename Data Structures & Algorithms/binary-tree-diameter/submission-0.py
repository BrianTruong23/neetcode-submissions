# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0 

        def dfs(node):
        #    height: how many downward node along the path 
        #    diameter height of left + height of right subtree
        # we need to calculate the left + right height of the subtree and then plus 1

            nonlocal diameter 

            if not node:
                return 0

            # print("node:val", node.val)
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            # print("diameter: ", diameter)

            return max(left, right) + 1

        dfs(root)

        return diameter 