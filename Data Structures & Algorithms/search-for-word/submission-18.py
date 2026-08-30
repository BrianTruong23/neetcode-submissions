class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        # search recursively to find the word in the board 
        # we go through the board and if we stumble on the 1st letter of the word then we search recursively through different path of the boards until we find the word
        # if not then we return false 

        first_array = []
        total_len = len(board) * len(board[0])
        row_len = len(board)
        column_len = len(board[0])

        # how your break down 2d -> 1d 
            # so if it is i , j and i is row and j is column
            # index in went from i and j: i * len(row) + j + 1 
        def return_index_went(i, j):
            return i * column_len + j  

        def dfs(i, j, index, went):

            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or index >= len(word):
                return False 
            
            # if we already went this character then return False 
            index_went = return_index_went(i, j)
            if went[index_went]:
                return False 

            # if it does not hit the next index of the word, return 
            if board[i][j] != word[index]:
                return False 
            
            if board[i][j] == word[index] and index == len(word) - 1:
                # at the end 
                return True 

            went[index_went] = True 
        
          # Explore 4 directions
            found = (
                dfs(i, j + 1, index + 1, went) or
                dfs(i + 1, j, index + 1, went) or
                dfs(i, j - 1, index + 1, went) or
                dfs(i - 1, j, index + 1, went)
            )

            # Backtrack
            went[index_went] = False

            return found


        went = [False] * (total_len)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, went):
                        return True 


        return False 


            
                    



