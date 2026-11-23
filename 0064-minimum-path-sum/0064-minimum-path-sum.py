class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0]*cols for i in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if (r,c) == (rows-1,cols-1):
                    continue

                down = float('inf') if r+1 >= rows else dp[r+1][c]
                right = float('inf') if c + 1 >= cols else dp[r][c+1]

                dp[r][c] = grid[r][c] + min(down, right)
        return dp[0][0]