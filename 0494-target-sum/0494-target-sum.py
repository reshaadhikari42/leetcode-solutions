class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        '''
this seems like combination sum, but we have to use all the digits
and we can only use them once. we cannot reuse them.
we make two choices: + and - for each number.
this should work. having 2d dp array will make it faster.
'''
        dp = {}

        def dfs(i, currSum):
            if currSum == target and i == len(nums): #reached end and sum equal to target
                return 1

            if i == len(nums): #can't say currSum > target bc we will also subtract
                return 0 #reached end but sum is not equal to target

            if (i, currSum) in dp:
                return dp[(i, currSum)]

            add = dfs(i+1, currSum + nums[i])
            sub = dfs(i+1, currSum - nums[i])

            ans = add + sub
            dp[(i, currSum)] = ans
            return ans

        return dfs(0,0)