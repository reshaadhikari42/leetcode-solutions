class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openCount, closeCount = 0,0
        res = []
        for i in range(len(s)):
            if openCount == closeCount and s[i] == '(':
                openCount += 1
                continue
            else:
                if s[i] == '(':
                    openCount += 1
                    res.append('(')
                else:
                    closeCount += 1
                    if closeCount != openCount:
                        res.append(')')
        return ''.join(res)
                