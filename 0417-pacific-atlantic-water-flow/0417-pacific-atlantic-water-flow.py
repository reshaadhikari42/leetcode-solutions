class Solution:
    def pacificAtlantic(self, height: list[list[int]]) -> list[list[int]]:
        #create two sets pac and atl. return the [r,c] that exists in both
        #we start by coding the edges bc they flow to the oceans. while adding them to the set, we also call dfs on them. same dfs func for both oceans should work

        def dfs(r,c,visit, prevHeight):
            if r < 0 or c<0 or r >= rows or c >= cols or (r,c) in visit or prevHeight > height[r][c]:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, height[r][c])
            dfs(r-1, c, visit, height[r][c])
            dfs(r, c+1, visit, height[r][c])
            dfs(r, c-1, visit, height[r][c])

        rows, cols = len(height), len(height[0])
        pac, atl = set(), set()

        for r in range(rows):
            #add in set is already done in dfs call so no need to do it here
            dfs(r, 0, pac, height[r][0])
            dfs(r, cols-1, atl, height[r][cols-1])
         

        for c in range(cols):
            dfs(0, c, pac, height[0][c]) 
            dfs(rows-1, c, atl, height[rows-1][c])
            

        res = []
        for r,c in pac: #loop thru the sets. better than looping thru the 2d array
            if (r,c) in atl:
                res.append([r,c])

        return res