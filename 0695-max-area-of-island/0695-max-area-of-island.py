class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int):
            nonlocal area
            nonlocal max_area

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r,c) in seen:
                return

            area += 1
            max_area = max(max_area, area)
            seen.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        rows , cols = len(grid), len(grid[0])
        seen = set()
        area, max_area = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    area = 0
                    dfs(r,c)
        return max_area