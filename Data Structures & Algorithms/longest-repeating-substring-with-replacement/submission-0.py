class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, right = 0, len(s) - 1

        for i in s:
            if i not in count.keys():
                count[i] = 0
            count[i] += 1

        while left <= right:
            if (right-left+1) - max(count.values()) > k:
                left += 1
            else: 
                return (right - left + 1)
        
            
            
        