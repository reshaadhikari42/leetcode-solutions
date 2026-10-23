class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hMap1 = {i:0 for i in range(26)}
        hMap2 = {i:0 for i in range(26)}
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            hMap1[abs(ord('a') - ord(s1[i]))] += 1

        l,r = 0, 0
        while r<len(s2):
            hMap2[abs(ord('a') - ord(s2[r]))] += 1
            window = r - l + 1


            if window == len(s1) and hMap1 == hMap2:
                return True

            if window == len(s1) and hMap1 != hMap2:
                hMap2[abs(ord('a') - ord(s2[l]))] -= 1
                l += 1
            
            r += 1 #move r always

        return False    
        