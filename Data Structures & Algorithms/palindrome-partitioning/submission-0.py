class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        result = []

        def palindrome(s1):
            return s1 == s1[::-1]

        def dfs(start, path):

            # base case 
            if start >= len(s):
                result.append(path[:])
                return 
            
            for end in range(start, len(s)):

                substring = s[start:end+1]

                if palindrome(substring):

                    # if palindrome we continue 
                    path.append(substring)

                    dfs(end + 1, path)

                    path.pop()
        
        dfs(0, [])
        return result
