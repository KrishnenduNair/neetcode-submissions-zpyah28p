class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        for i in s:
            if i in match:
                if not stack or stack[-1] != match[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0
        