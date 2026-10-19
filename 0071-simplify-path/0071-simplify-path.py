class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        strings = path.split('/')
        print(strings)
        i = 0
        while i < len(strings):
            if strings[i] == '':
                i += 1
                continue
            if strings[i] == '.':
                i += 1 #move i to the next string after /
                continue
            elif strings[i] == '..':
                if stack: stack.pop() #removing the prev directory
            else:
                stack.append(strings[i])
            i += 1
        print(stack)
        return '/' + '/'.join(stack)