class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def Lbinarysearch(l, r):
            idx = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    idx = mid
                    r = mid-1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx

        def Rbinarysearch(l, r):
            idx = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    idx = mid
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
            
                


        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                idx = mid
                leftidx = Lbinarysearch(0, mid)
                rightidx = Rbinarysearch(mid, len(nums)-1) #if only one pos then need to return [1,1]
                return [leftidx, rightidx]
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return [-1,-1]
        
        