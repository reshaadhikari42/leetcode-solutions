class Solution:
    '''
for str abde and ace: ans is ae so 2
we start with i = 0 and j = 0 which is starting pos of both strings
then if we find a match, we move both i and j by +1
if we no match is found, we can either move ptr on first string or on second string
we actually do both. because if string was abd and acb then moving ptr on second string would make sense
'''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2): #out of bounds
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
                return dp[(i, j)] #go to the end
            else:  #not matching
                moveptr1 = dfs(i, j+1)
                moveptr2 = dfs(i + 1, j)
                ans = max(moveptr1, moveptr2)
                dp[(i,j)] = ans
                return ans

        return dfs(0,0)