# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # two helper functions 

        subTree = False 
        def dfs(node, subNode):

            nonlocal subTree

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
                
                # both have the same values
                left = sameTree(node.left, subNode.left)
                right = sameTree(node.right, subNode.right)

                return left and right

            if not node: 
                return 
            
            if sameTree(node, subNode):
                subTree = True 
                return 

            dfs(node.left, subNode)
            dfs(node.right, subNode)
            return 
            
        dfs(root, subRoot)

        return subTree 
