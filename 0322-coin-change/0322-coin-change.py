class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}
        #top down memoization 

        def dfs(i, currSum):
            if currSum == amount:
                return 0

            if i == len(coins) or currSum > amount:
                return float('inf')

            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            include = 1 + dfs(i, currSum + coins[i])
            exclude = dfs(i + 1, currSum)

            res = min(include, exclude)
            dp[(i, currSum)] = res
            return res

        ans = dfs(0, 0)
        return ans if ans != float('inf') else -1