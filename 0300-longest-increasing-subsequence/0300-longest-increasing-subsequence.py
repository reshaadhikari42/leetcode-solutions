class Solution:
    '''
im thinking of this way..
dp = [1] * len(nums)
and we go from backwards
we have to loop twice- i, j
for every nums[i] < nums[j]: we set dp[i] = max(dp[i], dp[i] + dp[j]) and j goes till the end of the loop
same logic had to set temp = dp[i] so as to not overwrite dp[i]'s value after every max()
this is a big O(n^2) solution. first lets try this and if it works we can try to make it better.
'''
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            temp = dp[i]  #setting this so it won't change inside the loop
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: #we found increasing subsequence
                    dp[i] = max(temp + dp[j], dp[i])
        print(dp)
        return max(dp)