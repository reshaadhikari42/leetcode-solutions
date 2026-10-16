class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #find minimum first
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        #r is the smallest index
       
        
       # [0,1,2,3,4,5] [5,0,1,2] [5,6,7,0]
       #check whether the target is on left or right
        if nums[r] == target:
            return r
        elif target >= nums[0] and target > nums[-1]:
            l,r = 0, r - 1
        else:
            l,r = r + 1, len(nums)-1
   
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1