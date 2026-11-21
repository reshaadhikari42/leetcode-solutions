class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)] #creating a dp array
        dp[m-1][n-1] = 1 #one way to reach the last cell

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if dp[i][j] == 0: #only reset values that haven't been changed
                    if i + 1 >=m:
                        down = 0
                    else:
                        down = dp[i+1][j]
                    if j + 1 >= n:
                        right = 0
                    else:
                        right = dp[i][j+1]
                    dp[i][j] = right + down
                    
        return dp[0][0]