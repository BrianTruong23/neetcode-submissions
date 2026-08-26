class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        def dfs(index, path):

            # base case 
            if index == len(nums):
                result.append(path[:])
                return 

            # other cases 

            # inclusion part 
            path.append(nums[index])
            dfs(index + 1, path)

            # exclusion part 
            path.pop()
            dfs(index + 1, path)

        dfs(0, [])

        return result 
