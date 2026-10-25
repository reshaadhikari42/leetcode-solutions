class Solution:
    '''
dp top down
'''
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= goal: #nums[i] + i is the max jump that can be made. we directly check that max.
                #if it goes beyond goal, its still good. we move the goal to i after we found that its reachable
                goal = i
        return True if goal == 0 else False