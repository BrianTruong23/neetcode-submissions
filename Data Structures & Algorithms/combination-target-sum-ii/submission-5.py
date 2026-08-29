class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        candidates = sorted(candidates)
        # print(candidates)
        result = []

        def dfs(index, remaining, path):

            # print(path)

            if remaining == 0:
                result.append(path[:])
                return 
            
            if remaining < 0:
                return 

            if index >= len(candidates):
                return

            cand_num = candidates[index]

            # print(cand_num, remaining)
            if cand_num > target or cand_num > remaining:
                return 
            
            path.append(cand_num)
            dfs(index + 1, remaining - cand_num, path)

            path.pop()
            
            while index < (len(candidates) - 1) and (candidates[index] == candidates[index + 1]):
                index += 1
            
            dfs(index + 1, remaining, path)

        dfs(0, target, [])

        return result 
