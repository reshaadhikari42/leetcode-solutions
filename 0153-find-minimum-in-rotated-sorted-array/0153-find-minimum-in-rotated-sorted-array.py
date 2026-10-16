class Solution:
    def findMin(self, nums: list[int]) -> int:
       # [0,1,2,3,4]  [4,0,1,2,3]  [3,2,0,1]  [4,0,1] [5,4,0]

        l, r = 0, len(nums)- 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
        
        return nums[r]  #after while loop l > r which will make l out of bounds
 