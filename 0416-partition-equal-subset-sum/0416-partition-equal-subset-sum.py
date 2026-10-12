class Solution:
    '''
the regular dp solution is not that simple
here we create a dp called set() and add 0 to it. after that we loop thru the nums and add new_dp.add(t + nums[i]) and then after loop completes we do dp = new_dp
t is for t in dp
lets try this.. the code is simple but getting here wouldn't be easy...
'''
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            new_dp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                new_dp.add(t + nums[i])
            dp = new_dp | dp
        return False