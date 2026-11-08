class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergeSort(left, right):
            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res


        
        def divide(nums):
            if len(nums) <= 1:
                return nums
            l,r = 0, len(nums)-1
            mid = (l+r)//2
            left = divide(nums[0:mid+1])
            right = divide(nums[mid+1:])

            return mergeSort(left, right)

        return divide(nums)
            
