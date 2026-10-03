class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in zero or board[r][c] == 'X':
                return
            zero.add((r,c))
            board[r][c] = 'S'  #if its 'O' now its 'S'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        rows, cols = len(board), len(board[0])
        zero = set()
        for r in range(rows):  #calling dfs on left and right edge
            dfs(r, 0)      #don't need to check if its 'O' or 'X'. dfs returns if its 'X'
            dfs(r, cols-1)

        for c in range(cols):
            dfs(0, c)    #calling dfs on top and bottom edge
            dfs(rows-1, c)  #don't need to check if its 'O' or 'X'. dfs returns if its 'X'

        #final conversion
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'