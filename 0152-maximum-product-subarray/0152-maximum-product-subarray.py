class Solution:
    '''
because of the negative signs, this can get a little tricky.
[2, -3, -4] here if you just store max(nums[i], dp[i-1] * nums[i]), this will produce : dp = [2,-3, 12] but should be [2,-3/-6, 12/24]
and 24 is the answer. you need to store both min and max. because you can have negative number later in the array and
negative * negative can produce the max positive number

since this is a subarray, it will be continuous
because of that you only need both min and max at previous value. you don't need 2 different arrays for both min and max
just a variable is fine
in fact since you just need min and max from previous loop, you don't even need a dp array.
just use min and max variable.
but make sure to use base case res= nums[0]
'''
    def maxProduct(self, nums: list[int]) -> int:
        minP = nums[0]
        maxP = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            temp = minP #storing this to not change it
            minP = min(minP * nums[i], maxP * nums[i], nums[i])
            maxP = max(maxP * nums[i], temp * nums[i], nums[i])
            res = max(res, maxP)

        return res