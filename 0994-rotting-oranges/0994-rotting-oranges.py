class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_count = 0  #to determine if we have any fresh apples at the end
        rows, cols = len(grid), len(grid[0])
        q, visit = deque(), set()
        time_taken = 0

        def addtoq(r,c):
            nonlocal fresh_count  #fresh_count is nonlocal
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh_count -= 1 #the apples have rotten as soon as we see them
                #not when we pop them in bfs
                q.append([r,c])
                visit.add((r,c))            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        if fresh_count == 0: #no need to traverse if there are no fresh apples
            return 0 
        #bfs starting at rotten cells
        while q and fresh_count > 0: 
            #stop as soon as fresh_count is 0. else it will do extra loop & time goes up
            for _ in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 0:
                    return
                addtoq(r+1,c)
                addtoq(r-1,c)
                addtoq(r,c+1)
                addtoq(r,c-1)
            
            time_taken += 1
        
        return time_taken if fresh_count == 0 else -1

