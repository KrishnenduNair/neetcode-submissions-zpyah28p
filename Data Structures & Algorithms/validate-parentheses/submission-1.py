class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for i in s:
            if i in bracket.keys():
                stack.append(i)
            else:
                if not stack or bracket[stack.pop()] != i:
                    return False

        return not stack
