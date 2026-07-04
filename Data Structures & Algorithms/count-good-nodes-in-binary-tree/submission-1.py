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
        # no need to use another tracker outside 

        def dfs(node, max_):

            if not node:
                return 0
            
            is_good = node.val >= max_

            max_ = max(max_, node.val)

            return (
                (1 if is_good else 0) + dfs(node.right, max_) + dfs(node.left, max_)
            )

        
        return dfs(root, root.val)

