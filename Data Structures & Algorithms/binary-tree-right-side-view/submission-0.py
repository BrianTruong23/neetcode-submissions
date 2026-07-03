# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs 
        # only append the rightmost element of the current level list to the result 
        # one improvement if we dont need to hold every element in the current level 

        def bfs(root):

            if not root:
                return []

            result = []

            queue = deque([root])

            while queue:

                right_most = -111
                level_size = len(queue)

                for _ in range(level_size):

                    node = queue.popleft()

                    if node.right:
                        queue.append(node.right)
                    
                    if node.left:
                        queue.append(node.left)

                    if right_most == -111:
                        right_most = node.val

                result.append(right_most)
            
            return result 
        
        return bfs(root)



