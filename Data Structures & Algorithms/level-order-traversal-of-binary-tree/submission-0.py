# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # very beneficial to use bfs 
        # have a nested list data structure to store elements where the index for the outer list will be the level starting with 0
        # bfs will use stack and we push node to stack to examine the node 
        # then we pop 
        # we have level so that can append 

        # we use bfs to search through the nodes in the tree
        # we first popleft 
        # append to current level
        # then append node left and node right 

        # then append to the result current level 

        # queue: keep track of incoming nodes and how many nodes in current level
        # current_level => inner list of nodes 
        # result => outer list of nodes 
        
        def bfs(root):
            
            result = []
            if not root:
                return result 

            queue = deque([root])

            while queue: 
                # first determine the size of queue which is the size of the current level 

                level_size = len(queue)
                current_level = []

                for _ in range(level_size):
                    # pop everything in this current level 
                    node = queue.popleft()

                    # append if node has right and left 

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
            
                    # append to current level 
                    current_level.append(node.val)
                
                # append current level to result 
                result.append(current_level)

            return result 

        return bfs(root)
                



            
            






