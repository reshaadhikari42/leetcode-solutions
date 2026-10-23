class Solution:
    '''
since we have to look at nums2 for greater element but need indices of nums1, we use hashmap to map the indices in the second array
we have hashmap with num:index for nums2
for nums2 we try to find the greater element to the right using stack.
we create a stack and try to fill it with elements.
for [1,3,4,2] we traverse from back. stack starts with [2] and res = [0,0,0,-1] the last element is going to be pre-inserted
now we look at second last element, stack[-1] is not bigger than 4, so we pop stack and add 4. for res we do -1 in the same index
we can pop the smaller element because we won't need the 2 anymore. for next element, the biggest will be 4.
once we have res.
we can use mapping and res to return the solution
'''
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap = defaultdict(int)
        #added nums2:index to hashMap
        for i,e in enumerate(nums2):
            hashMap[e] = i

        stack = [nums2[-1]] #last element at top as it will be the biggest we have had
        res = [0] * len(nums2)
        res[-1] = -1 #last element will not have anything greater so it will always be -1

        for i in range(len(nums2)-2,-1,-1):
             #after cleaning the if and else cases. don't need a lot here.
            while stack and stack[-1] <= nums2[i]:
                stack.pop() #we don't need smaller elements
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(nums2[i])

        #map back to hashMap
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            pos = hashMap[nums1[i]]
            ans[i] = res[pos]
        return ans