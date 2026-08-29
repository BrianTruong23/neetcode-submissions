class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        

        result = []

        used = [False] * len(nums)

        def dfs(path):

            # base case 
            if len(path) >= len(nums):
                result.append(path[:])
                return
        
            # other cases 
            for i in range(len(nums)):

                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                dfs(path)

                used[i] = False
                path.pop()


        dfs([])
        return result 


