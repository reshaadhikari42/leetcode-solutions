class Solution:
    '''
dp top down
'''
    def canJump(self, nums: list[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            max_possible = min(len(nums)-1, i + nums[i]) #making sure we don't go overbound. max is len(nums)-1
            for j in range(1, nums[i]+1): #nums[i] + 1 because its not included
                if i + j > max_possible:
                    break
                if dp[i+j]: #reaches the last index
                    dp[i] = True
                    break
                    
            #dp[i] = False no because its already defaulted to False
        return dp[0]