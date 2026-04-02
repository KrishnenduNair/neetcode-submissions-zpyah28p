class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        increase = 0
        for ind, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                index = stack.pop()
                res[index] = ind - index
            stack.append(ind)
        
        return res

                
