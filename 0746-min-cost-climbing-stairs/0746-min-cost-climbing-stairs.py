class Solution:
    '''
DPP problem again...
in DPP, we make sure to use the previous calculation to the next step. that is the main logic.
imagine this is the array cost: [1,2,1,99,100] we can take only one or two steps.
lets calculate min cost at every step:
to calculate min cost at each step, logic = cost of that position + min cost of getting there.
cost of that position is easy. but how to calculate min of a particular position??
to get to a position, we can get there from i-1 position or i-2 position because that is all we can do (make 2 jumps max)
so min cost at a position is always : cost of that position + min(cost of i-1 pos, cost of i-2 pos)
then in the end we can return min cost between the last and the second last pos's cost because we can make 2 steps again.

we will do this first using a dp array. and then again using fibonacci sequence code
'''
    def minCostClimbingStairs(self, cost: list[int]) -> int:
       
        dp = [0]* len(cost)
        dp[0], dp[1] = cost[0], cost[1] #min cost for pos 2 is always itself, as cost[1] < cost[0] + cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])
'''
def minCostClimbingStairs(self, cost: list[int]) -> int:
#this one has a little more hard coded cases but this uses less space.
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return min(cost[-1],cost[-2])
    if len(cost) == 3:
        return min(cost[0]+cost[2], cost[1])
    a, b = cost[0], cost[1]
    c = 0
    for i in range(2, len(cost)):
        c = cost[i] + min(a, b)
        a = b
        b = c
    return min(b,c)  #in the end you have to return the min between last two elements
#uses O(1) time but this is irrelavant for such small input (constraint says <1000)
#first logic is to use dp array and then we can optimize this by using fibonacci since we only need the last 2 elements and don't need full array.
'''

