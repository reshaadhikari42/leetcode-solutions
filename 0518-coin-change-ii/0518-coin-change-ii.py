class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        '''
lets try with recursion first. so we try two combinations: include and exclude
since we have infinite number of coins, we can include a number multiple times. if we exclude, we exclude it
if we find the valid combinations, we return 1. we add include + exclude as all those combinations included the answer
'''
        dp = {}

        def dfs(i, currSum):
            if currSum == amount:
                return 1  #found 1 combination

            if i >= len(coins) or currSum > amount:
                return 0 #no answer

            if (i, currSum) in dp:
                return dp[(i, currSum)]

            include = dfs(i, currSum + coins[i]) #include
            exclude = dfs(i + 1, currSum) #exclude

            count = include + exclude
            dp[(i, currSum)] = count
            return count

        return dfs(0, 0)