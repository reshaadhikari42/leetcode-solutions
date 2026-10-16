class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        prevLen = len(intervals)
        for i in range(len(intervals)):
                if newInterval[0] <= intervals[i][0]:
                    intervals.insert(i, newInterval) #insert happens only once so this loop is O(n) + 1 time insert is total O(2n) which is not O(n^2)
    #but if the newInterval is supposed to be at the end?

        if len(intervals) == prevLen:
            intervals.append(newInterval) #was the largest so appended at last manually as this case was't checked in loop above

        #now all intervals are connected. now we merge them if they are overlapping
        res = []  #we don't wanna add first interval here so that we don't have to add the edge case of intervals being emptpy separately

        for i in range(len(intervals)):
            if not res:
                res.append([intervals[i][0], intervals[i][1]])
            elif res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])

        return res