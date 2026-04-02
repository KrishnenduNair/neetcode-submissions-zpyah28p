class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        
        def backtrack(current, openN, closeN):
            if len(current) == 2*n:
                stack.append(current)
                return
            
            if openN < n:
                backtrack(current + '(', openN + 1, closeN)
            if closeN < openN:
                backtrack(current + ')', openN, closeN + 1)

        backtrack("", 0, 0)
        return stack
                