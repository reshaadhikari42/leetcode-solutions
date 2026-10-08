class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        same as house robber. we just call it twice to exclude either the first or last
        but if the length of nums = 1, we just return 1 before calling the helper func because helper would call only [] twice

'''
        if len(nums) == 1:
                return nums[0]
        def helper(nums):
            
            dp = [0] * len(nums)
            if len(nums) < 3:
                return max(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[0:len(nums)-1]))