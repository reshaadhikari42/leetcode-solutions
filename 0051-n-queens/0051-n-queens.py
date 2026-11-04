class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.']*n for i in range(n)] #doing [['.']*n]*n means all rows point to same memory so changing one row can change others too
        res = []

        def isSafe(r,c):
            i = 1
            while i <= r:
                if r-i >= 0 and board[r-i][c] == 'Q': return False #up
                if r-i >= 0 and c-i >= 0 and board[r-i][c-i] == 'Q': return False #left diagonal
                if r-i >= 0 and c+i < n and board[r-i][c+i] == 'Q': return False #right diagonal
                #we don't check for +1s. only check for rows up above.
                i+=1
            return True                

        def dfs(r):
            temp = []
            if r == n:
                for rows in range(n): #we can do this
                    temp.append(''.join(board[rows]))
                res.append(temp)
                return

            for c in range(n): #cols = n as well
                if isSafe(r,c):
                    board[r][c] = 'Q'
                    dfs(r+1)
                    board[r][c] = '.' #backtrack
                #else we do nothing it just returns back to previous call and backtracks
        dfs(0)
        return res

