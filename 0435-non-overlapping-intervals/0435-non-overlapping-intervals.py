class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        '''
we sort the intervals
then we compare the start with prevEnd and if that merges then we need to remove one of them right
if it doesn't merge we save prevend as intervals[i][1]
if it merges, we save prevEnd as smaller interval
this is because selecting the smaller interval means we have space for other intervals
also we increment count everytime there is a merge and we choose smaller interval

'''
        count = 0
        intervals.sort()
        prevEnd = intervals[0][1] #since constraint says interval length is atleast 1

        for s, e in intervals[1:]:
            if prevEnd > s: #overlapping
                count += 1 #we have to get rid of 1
                prevEnd = min(prevEnd, e)
            else:
                prevEnd = e

        return count