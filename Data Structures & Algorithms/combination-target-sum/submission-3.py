class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        # sort 
        nums.sort()
        # result array 
        result = []

        # write dfs with backtracking 

        def dfs(index: int, path: List[int]):

            # print(path)
            # base case 
            if sum(path) >= target or index >= len(nums) or nums[index] > target: 
                if sum(path) == target: 
                    result.append(path[:])
                
                return 

            path.append(nums[index])
            dfs(index, path)

            path.pop()

            # print(path, index + 1, nums[index + 1])
            if (index + 1 < len(nums)) and ((sum(path) + nums[index + 1]) > target):
                return
            
            dfs(index + 1, path)


        dfs(0, [])

        return result

        # other cases 

        # keep track of the path 

            # base case 
            # append to result if the path sum = target 
            # return when the sum is larger 

        # at any decision, we have a choice to move index forward or not move forward 
            # but we always include the nums[index] to the path 
        
