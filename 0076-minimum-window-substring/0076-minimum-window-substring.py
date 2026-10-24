class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hMap1, hMap2 = defaultdict(int), defaultdict(int)
        min_len, res = float('inf'), ''

        for ch in t:
            hMap1[ch] += 1
        
        l,r = 0, 0
        have, need = 0, len(hMap1)
       
        while r < len(s):
            if have != need:
                if s[r] in hMap1:
                    hMap2[s[r]] += 1
                    if hMap2[s[r]] == hMap1[s[r]]:
                        have += 1
            
            while have == need:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in hMap1:  #making window smaller by moving l
                    hMap2[s[l]] -= 1
                    if hMap2[s[l]] < hMap1[s[l]]: #s= AABC, t = ABC. need to check this before decrementing have
                        have -= 1
                l += 1
            r += 1
        return res

