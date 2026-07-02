# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # two helper functions 

        def sameTree(node, subNode):
            # return boolean 
            # check the both tree 
            if not node and not subNode:
                return True 
            elif node and not subNode:
                return False 
            elif not node and subNode:
                return False 
            elif node.val != subNode.val:
                return False 

            return sameTree(node.left, subNode.left) and sameTree(node.right, subNode.right)

        subTree = False 
        def dfs(node, subNode):
            nonlocal subTree
            if not node: 
                return 
            
            if (node.val == subNode.val):
                if sameTree(node, subNode):
                    subTree = True 
                    return 
                
            dfs(node.left, subNode)
            dfs(node.right, subNode)
            return 
            
        dfs(root, subRoot)

        return subTree 

    # space complexity: recursion stack at worst O(n)
    # time complexity: 
