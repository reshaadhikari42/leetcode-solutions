class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        #make a hashmap of all combinations in a and b array
        #look for -sum of c and d array and add to res
        #DONT decrement the count of the hashmap bc other combinations will need it too
        res = 0
        hMap = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                hMap[nums1[i]+nums2[j]] += 1

        for i in range(len(nums1)):
            for j in range(len(nums1)):
                s = nums3[i] + nums4[j]
                if -s in hMap:
                    res += hMap[-s]
        return res
