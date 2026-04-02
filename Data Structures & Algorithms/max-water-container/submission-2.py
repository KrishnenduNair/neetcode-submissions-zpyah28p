class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea= 0
        l, r = 0, len(heights)-1
        
        while l < r:
            hl = heights[l]
            hr = heights[r]
            area = min(hl, hr) * (r - l)
            maxArea = max(maxArea, area)

            if hl <= hr:
                l += 1
            else:
                r -= 1
            
        return maxArea
