class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        sortedI = sorted(intervals, key = lambda x:x[0])

        prevS, prevE = sortedI[0][0], sortedI[0][1]
        res = []
        res.append([prevS, prevE])

        for i in range(1,len(sortedI)):
            if sortedI[i][0] <= prevE:
                sortedI[i][0] = min(prevS, sortedI[i][0])
                sortedI[i][1] = max(prevE, sortedI[i][1])
                res.pop()
            
            prevS = sortedI[i][0]
            prevE = sortedI[i][1]
            res.append([sortedI[i][0],sortedI[i][1]])

        return res


                
            