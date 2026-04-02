class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n+1):
            h = heights[i] if i < n else 0 
            
            while stack and h < heights[stack[-1]]:
                ind = stack.pop()
                w = i - stack[-1] - 1 if stack else i
                h_val = heights[ind]
                area = h_val * w
                max_area = max(max_area, area)
            else: 
                stack.append(i)

        return max_area

                
        