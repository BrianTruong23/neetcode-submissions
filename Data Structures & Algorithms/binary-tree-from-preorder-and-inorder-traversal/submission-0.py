# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # root is the first eleemnt of preorder 
        # the element in the inorder effectively separate into left and right subtree 

        # global variable index
        # hash map for inorder array
        # dfs approach to build out this recursively cutting the range for left and right so that i can build out this tree 

        g_index = 0
        hash_map = {}

        for index, value in enumerate(inorder):
            hash_map[value] = index

        def dfs(l, r):

            nonlocal g_index
            if l > r:
                return None 
            # print("L: ", l, " R: ", r)
            rootVal = preorder[g_index]
            root = TreeNode(rootVal)

            # print("Root Val: ", rootVal)

            # find this root in inorder 
            r_index = hash_map[rootVal]
            g_index += 1

            # left and right DFS
            root.left = dfs(l, r_index - 1)
            root.right = dfs(r_index + 1, r)

            return root 
        
        return dfs(0, len(preorder) - 1)




            
            