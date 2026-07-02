# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # we should have a way to find the common ancestor when we go through finding where p and q is 

        # so interesting, if we go through and we dont find p or q then we assign this to be LCA
        # if we find p 
        # if we find q 
        #  what about a function to find p and q in the left and right 

            # if p and q are in opposites end: then this is LCA 
            # if not in the opposite end, then we only move in that direction that contain both p or q
            # we repeat this operation: move to one node, examine sides of p and q
                # if the node that we examine are p or q, then return.
                # if p and q are in opposites, return this node 

        node_LCA = root 

        def dfs(node):

            nonlocal node_LCA 

            if not node:
                return 

            find_p = False 
            find_q = False 

            def search_p_q(node):
                nonlocal find_p
                nonlocal find_q

                # find p, q or both 
                if not node:
                    return 

                if node.val == p.val:
                    find_p = True 
                
                if node.val == q.val:
                    find_q = True 
                
                if find_p and find_q:
                    return 

                search_p_q(node.left)
                search_p_q(node.right)
                return 

            print("node.val:", node.val)
            
            # if the node examined is p or q then return because we find p and q 
            if node.val == p.val or node.val == q.val:
                node_LCA = node
                return 
            
            search_p_q(node.left)

            # print("Find p: ", find_p)
            # print("Find q: ", find_q)
            # if we find both in left then we go to left 
            if find_p and find_q:
                # we go left 
                dfs(node.left)

            elif find_p or find_q:
                # we find only one in the left which means there is one on the right 
                # we return 
                node_LCA = node 

            else:
                # both in the right 
                dfs(node.right)
            
            return 

        dfs(root)

        return node_LCA