class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        def dfs(index: int, path: List[int]):

            if index == len(nums):
        
                result.append(path[:])
        
                return

            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1 

            dfs(index + 1, path)

        dfs(0, [])

        return result
