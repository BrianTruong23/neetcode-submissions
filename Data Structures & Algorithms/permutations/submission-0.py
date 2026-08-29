class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        used = [False] * len(nums)

        def dfs(path):
        
            # base case 
            # we only return when the length of path is equal to length of nums
            if len(path) >= len(nums):
                result.append(path[:])
                return

            # other cases 

            for i in range(len(nums)):
                
                if used[i]:
                    continue 
    
                path.append(nums[i])
                used[i] = True

                dfs(path)

                used[i] = False
                path.pop()
        
        dfs([])
        return result 

    
