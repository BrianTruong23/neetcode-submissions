# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # we should have a way to find the common ancestor when we go through finding where p and q is 

        def dfs(node):

            if not node:
                return None

            # print("node.val: ", node.val)
            
            if node.val == p.val or node.val == q.val:
                # print("P or Q here: ", node.val, "P: ", p.val, "Q: ", q.val)
                return node 
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node 
            
            return left or right
        
        return dfs(root)


