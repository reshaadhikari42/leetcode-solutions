class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        '''
we sort the intervals using lamda sorted function first
and then create a new array called res and append if non overlapping
if overlapping, we take the min of start, max of end and append
'''

        intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]: #res empty or non overlapping
                res.append([intervals[i][0], intervals[i][1]])

            elif res[-1][1] >= intervals[i][0]: #or just use else
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res