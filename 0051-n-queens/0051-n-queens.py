class Solution:
    def isSafe(self, board, row, col):
        i = 1
        while (i <= row):

            if board[row-i][col] == 'Q':
                return False
            if col-i >=0 and row-i >= 0 and board[row-i][col-i] == 'Q':
                return False
            if col+i < len(board[0]) and row-i >= 0 and board[row-i][col+i] == 'Q':
                return False
            i+= 1
        return True


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for i in range(n)]

        def dfs(i):
            if i == n:
                res.append([''.join(i) for i in board])
                return

            for j in range(n): #cols
                if self.isSafe(board, i, j):
                    board[i][j] = 'Q'
                    dfs(i+1)
                    board[i][j] = '.'

        dfs(0)
        return res
