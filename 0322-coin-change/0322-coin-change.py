class Solution:
    '''
on the high level, this is a combination sum problem. this is combination because order doesn't matter- [1,2,2] and [2,2,1] are same.
difference between combination and permutation is the position.
if you're doing combination/two sums, you need position i because you need to be persistent with positions
for permutations you can use for loop and not care about i

lets try to solve this in combination sum format first and then make it better

    def coinChange(self, coins: list[int], amount: int) -> int:
         # subset = [] not needded
        res = float('inf')

        def combinationDFS(start, currSum, count):
            nonlocal res
            if currSum == amount:
                if count < res:
                    res = count
                return
            if currSum > amount: # no need to check i == len(coins)
                return

            for i in range(start, len(coins)):
                #subset.append(coins[i])
                combinationDFS(i, currSum + coins[i], count + 1)
            # subset.pop()

        combinationDFS(0,0,0)
        return -1 if res == float('inf') else res
        
        we create a memo called cache.
        we store memo[(i, currSum)] = min(include, exclude)
        this way we store all positions like memo[(1,0)] = min(include, exclude) meaning we take minimum of include and exclude
        here we use formula to caculate height of tree for include and exclude using 1 + dfs call
        since we don't need the subset, this will work.
        
        lets try to do this bottom up. we create a dp array of size len(amount) + 1
        we add values such that every position is the amount of coins needed to fill that spot

        [1,4,5] and amount = 12
        dp = [0,1,2,3,1,2,3,2,2,2,3,3]
        for dp[4] we need number of coins needed to sum 4
        we loop thru all coins array of 1,4,5
        loop coin = 1
        4 -1 =3
        dp[4] = dp[1] + dp[3] which we alreay have = 1 + 3 = 4
        loop when coin = 4
        4-4 = 0
        dp[4] = dp[4] + dp[0] where we don't have dp[4] tho. so for such case we just hardcode to 1? if the diff is 0?

        if pos-coin == 0: dp[pos] = 1 
        dp[pos] = min(dp[coin] + dp[pos-coin], dp[pos]) where we set dp[pos] = float('inf') before every inet for loop
        '''
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 #base case to make zero coins, we need 0 coins

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue  # dp[2], coins[1,4,5], we don't need to try coin 4 and 5 because they are bigger than 2
                elif coin == i:
                    dp[i] = 1
                    continue  #1 is always going to be minimum
                else:
                    dp[i] = min(dp[coin] + dp[i-coin], dp[i])

        return -1 if dp[amount] == float('inf') else dp[amount]