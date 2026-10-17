class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
we scan thru the array and add it to the stack only if the top of the stack doesn't match with s[i]
if it matches, we pop out of stack and never append.
if it doesn't match we append
there will never be a case wehere there will be a match after popping because we are scanning the array one by one.

'''
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)  #returns empty when stack is empty
