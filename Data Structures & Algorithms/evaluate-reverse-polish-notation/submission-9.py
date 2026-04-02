class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '/', '*']:
                b = int(stack.pop())
                a = int(stack.pop())
                if i =='/':
                    stack.append(str(int(a/b)))
                elif i =='*':
                    stack.append(str(a*b))
                elif i =='+':
                    stack.append(str(a+b))
                else:
                    stack.append(str(a-b))
            else:
                stack.append(i)

        return int(stack[-1])