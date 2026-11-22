class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        #need to mark obstacle cells as inf
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1 or obstacleGrid[0][0] == 1: #last cell in unreachable
            return 0

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = float('inf')

        obstacleGrid[rows-1][cols-1] = 1 #the last cell that is target

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == float('inf') or (r,c) == (rows-1, cols-1): #if its not reachable
                    continue
                else:
                    if c+1 >= cols:
                        right = 0
                    else:
                        right = obstacleGrid[r][c+1] if obstacleGrid[r][c+1] != float('inf') else 0

                    if r+1 >= rows:
                        down = 0
                    else:
                        down = obstacleGrid[r+1][c] if obstacleGrid[r+1][c] != float('inf') else 0

                    obstacleGrid[r][c] = down + right
        print(obstacleGrid)
        return obstacleGrid[0][0]