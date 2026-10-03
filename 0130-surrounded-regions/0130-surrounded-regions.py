class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c,visit):
            if r<0 or c<0 or r>=rows or c>= cols or (r,c) in visit or board[r][c] == 'X':
                return
            visit.add((r,c))
            board[r][c] = 'S'
            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)


        rows, cols = len(board), len(board[0])
        zero = set()
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0, zero)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1, zero)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c, zero)
            if board[rows-1][c] == 'O':
                dfs(rows-1, c, zero)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
        return board


