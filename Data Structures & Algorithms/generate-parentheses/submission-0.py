class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # at any point you have two choices: one is open parenthesis and the other one is close parenthesis. 
        # 
        result = []
        def dfs(num_o, num_c, path):

            if num_o == n and num_c == n:
                # valid answer 

                result.append(path)
                return 
            
            if num_o < n:
                dfs(num_o + 1, num_c, path + "(")
            
            if num_o > num_c:
                dfs(num_o, num_c + 1, path + ")")
            
        
        dfs(0, 0, "")
        return result 