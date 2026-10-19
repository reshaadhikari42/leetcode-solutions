class Solution:
    '''
using a stack. adding everything to stack until we find a ].
we pop after reaching a close bracket.
we then pop the num and alpha and do num * alpha and append to stack again
we need to be careful with the order though because popping can give reverse order in stack
'''
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        for i in range(len(s)):
            alpha = ''
            num = ''
            if s[i] == ']':
                while stack and stack[-1] != '[':
                    alpha = stack.pop() + alpha #rverse order we want bc but stack pops as cb
                stack.pop() #one extra pop for '['
                while stack and stack[-1].isdigit(): #since no negative number, isdigit() will work fine
                    num = stack.pop() + num
                ans = int(num) * alpha
                stack.append(ans)
            else:
                stack.append(s[i])
                print(stack)

        return ''.join(stack)
            