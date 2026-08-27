class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        # sort 
        nums.sort()
        # result array 
        result = []

        # write dfs with backtracking 

        def dfs(index: int, remaining, path: List[int]):
            
            if remaining == 0:
                result.append(path[:])

            if remaining < 0:
                return 
            
            for i in range(index, len(nums)):

                if nums[i] > remaining: 
                    break
                
                path.append(nums[i])

                dfs(i, remaining - nums[i], path)

                path.pop()
      
        
        dfs(0, target, [])

        return result 

                