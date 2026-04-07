class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == ' ':
            return 1
        curr_win, max_win = 0, 0
        window = s[0]
        for i in range(1, len(s)):
            if s[i] not in window:
                window += s[i]
            else:
                curr_window = len(window)
                max_win = max(max_win, curr_win)
                window = window[window.index(s[i])+1:]
                window += s[i]
            max_win = max(max_win, len(window))
        return max_win           
            
            