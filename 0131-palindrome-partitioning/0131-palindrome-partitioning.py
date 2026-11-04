class Solution:
    def partition(self, s: str) -> list[list[str]]:
        subset, res = [], []

        def isPalindrome(string):
            l, r = 0, len(string)-1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(substring):
            if substring == '':
                res.append(subset.copy())
                return

            for i in range(len(substring)):
                if isPalindrome(substring[0:i+1]):
                    subset.append(substring[0:i+1])
                    dfs(substring[i+1:])
                    subset.pop()
        dfs(s)
        return res