class Solution:
    def finalPrices(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        res[-1] = nums[-1]
        stack = [nums[-1]]

        for i in range(len(nums)-2,-1,-1):
            while stack and stack[-1] > nums[i]:
                stack.pop()
            if stack:
                res[i] = nums[i] - stack[-1]
            else:
                res[i] = nums[i] - 0
            stack.append(nums[i])
        return res
