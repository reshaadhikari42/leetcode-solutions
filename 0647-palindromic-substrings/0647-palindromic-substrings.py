class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
we make a list and save all the palindromic substrings from each position there

in the end we return len of list
this will be done in O(n^2) since we need to find palindromes from each position and extend it till l and r are out of bounds

we will use the same logic for both

for eg: 'aaa' for odd:
from first a, we get a. incrementing left or right causes out of bounds
from second a, we get a, aaa
from third a, we get a. incrementing goes out of bounds.
so we have total a, a, a, aaa

for 'aaa' even:
from first we get aa. after that l will be out of bounds
from second aa, we get, aa. incrementing will go out of bounds

that is all. so we have a,a,a,aaa, aa,aa.
'''
        collection = []

        for i in range(len(s)):
            #odd
            l = r =i
            while l>= 0 and r < len(s) and s[l] == s[r]: #as long as in bounds and is palindromic
                collection.append(s[l:r+1]) #we don't care about maxLength, we just add everything
                l -= 1
                r += 1

            #even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                collection.append(s[l:r+1])
                l -= 1
                r += 1

        return len(collection)