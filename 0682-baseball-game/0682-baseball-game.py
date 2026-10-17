class Solution:
    '''
since we need to look back at one of the scores, we use stack[-1] to peek
we keep adding scores to the stack and do the operations and in the end just return stack[-1]
we need to pop only when we invalidate the score.. else we are only adding the scores
constraints say that it cannot be invalid.
but in the end while returning the stack can be empty if theres invalidate operation
in that case we return 0 else we have to apparently return sum of all the values we have
'''
    def calPoints(self, ops: list[str]) -> int:
        stack = []
        operators = ['+','C','D'] #we cannot use isdigit() because neg number will cause false for '-1' due to minus sign

        for i in range(len(ops)):
            if ops[i] not in operators:
                stack.append(int(ops[i]))
            else:
                if ops[i] == '+':
                    stack.append(stack[-1] + stack[-2])
                elif ops[i] == 'D':
                    stack.append(2 * stack[-1])
                elif ops[i] == 'C':
                    stack.pop() #constraint says will always have an element to pop

        return sum(stack) if stack else 0