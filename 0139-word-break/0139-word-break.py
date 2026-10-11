class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
DP solution
we create a DP array of len(s) + 1 and set DP[-1] = True and everything else to False
in order to not backtrack, we loop thru the wordDict instead and not check every character in s
we only check s[i: i+ len(w)] == word when i + len(w) < len(s) since we are going backwards
what this means is for string abcd, words = [a, abc], since we are going back we don't even need to check when we are at d because checking for abc at pos d would go out of bounds
at every time we find the match we set dp[i] = dp[i + len(w)] meaning that latter part of the combination was alr found

for s= 'abcd' , wordDict = ['a', 'abc', 'd'], dp will look like: dp = [ True, False, False, True, True] and we fill them backwards.
###for s= 'aaaaaaa', wordDict = ['aaa', 'aaaa'], dp = [True, True, False, True, True, False, False, True]
good example of why this doesn't need recursion but covers all cases

'''


        dp = [False] * (len(s)+1)
        dp[len(s)] = True #base case

        for i in range(len(s)-1, -1, -1): #we check from backwards
            for word in wordDict: #we check every word not every letter in s. also bc of this we don't need to create dictionary
                if i + len(word) <= len(s) and s[i:i+len(word)] == word: #check only if doesn't go out of bounds and is equal
                    dp[i] = dp[i + len(word)]

                if dp[i] == True:
                    break
        return dp[0]


#Time is O(n × m × L): n positions, m words, L for the slice and compare. Space is O(n).
#neither top down or bottom up is better as they both lean towards O(n^3) with three variables.