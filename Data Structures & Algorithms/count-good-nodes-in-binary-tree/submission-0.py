# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # always trace from the root of the tree or the path (parent node from the root to that node)
        # improvement: only keep track of the max along the path. 
        # use dfs 
        # keep track of max so far in the path 

        result = 0

        def dfs(node, max_):

            if not node:
                return 

            nonlocal result

            # print("node.val: ", node.val)
            # print("max_: ", max_)
            # print("Result: ", result)

            if node.val >= max_:
                result += 1 
            
                dfs(node.right, node.val)
                dfs(node.left, node.val)
            else:
                dfs(node.right, max_)
                dfs(node.left, max_)

            return 

            
        dfs(root, -111)
        return result 