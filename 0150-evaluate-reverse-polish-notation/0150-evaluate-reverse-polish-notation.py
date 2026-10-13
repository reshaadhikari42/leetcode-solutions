class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []

        for each in tokens:
            if each not in operations:
                stack.append(int(each))
            else: #in operations
                operation1 = stack.pop()
                operation2 = stack.pop()
                if each == '+':
                    stack.append(operation1 + operation2)
                elif each == '*':
                    stack.append(operation1 * operation2)
                elif each == '/':
                    stack.append(int(operation2/operation1)) #truncate to zero
                else:
                    stack.append(operation2 - operation1)
        
        return stack[-1]

        

        