class Solution:
    '''
to get the minimum no of jumps in linear time...
we save last_index and max_coverage..
we save the max_coverage for the indices
we incrment counter when i == last_index because that will mean we made a jump
that is also the time we change last_index = maxCoverage so that for the next run, we start with last_index and maxCoverage from same postition
just like how we started at zero.
'''
    def jump(self, nums: list[int]) -> int:
        last_index, maxCoverage = 0,0
        count = 0

        for i in range(len(nums)-1):
            maxCoverage = max(maxCoverage, i + nums[i])

            if i == last_index:
                count += 1
                last_index = maxCoverage

        return count #count is updated till we reach the last element. this is because our for loop goes till the end