# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            if not a and not b:
                return True 
            
            if not a or not b:
                return False 
            
            return (a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right))
        
        def dfs(node):

            if not node:
                return False 
            
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True 

            return dfs(node.left) or dfs(node.right)  

        return dfs(root)

    # space complexity: recursion stack at worst O(n) and balanced at O(log n)
        # but at any moment you could have O(m) so worst case is O(n + m) => worst case for how much memory exist 

    # time complexity: O(n * m) where n is the height of root in worst case and m is the height of subRoot in worst case

