class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # permutations 
        # 345
        # def, ghi, jkl
        # d g j, d g k, d g l 

        
        maps = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

        result = []

        if len(digits) == 0:
            return []
        def dfs(index, path):
            
            # base case 
            if index == len(digits):
                result.append("".join(path[:]))
                return 
            
            digit_current = digits[index]
            for char in maps[digit_current]:
                
                path.append(char)
                dfs(index + 1, path)
                path.pop()
        
        dfs(0, [])
        return result