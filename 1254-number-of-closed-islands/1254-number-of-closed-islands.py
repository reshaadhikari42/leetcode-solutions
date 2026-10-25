class Solution:
    '''
same as counting maximum islands but the islands should not be touching the border
0 land
1 water
since we have a restriction that the border cannot be touched, we start from border and mark every 0 as somthing (1 or 2 or anything)
then we do a second pass and now see at 0s.
these 0s do not touch the border. but to get the correct count, we need dfs on those too so do dfs again
'''
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfsEdges(r,c): #marks all 0s that touch edges as 1
            if r < 0 or c < 0 or r >=rows or c >= cols or (r,c) in visited or grid[r][c] == 1:
                return
            grid[r][c] = 1 #if its 0 set to 1 bc we don't need that anymore
            visited.add((r,c))

            dfsEdges(r + 1,c)
            dfsEdges(r - 1, c)
            dfsEdges(r, c + 1)
            dfsEdges(r, c - 1)

        # we start dfs from edges
        for r in range(rows):
            dfsEdges(r, 0)
            dfsEdges(r, cols-1)

        for c in range(cols):
            dfsEdges(0, c)
            dfsEdges(rows-1, c)

        def dfsCount(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in seen or grid[r][c] == 1:
                return
            seen.add((r,c))
            dfsCount(r + 1, c)
            dfsCount(r - 1, c)
            dfsCount(r, c + 1)
            dfsCount(r, c - 1)

        #after converting all edges 0 to 1, we go thru dfs again and count
        seen = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == 0:  #counting the unmarked 0s
                    dfsCount(r,c)
                    res += 1
        return res