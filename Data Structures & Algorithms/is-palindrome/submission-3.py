class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for char in s:
            if char.isalnum():
                res += char.lower()
        res = res.strip()

        l, r = 0, len(res)-1
        while l<r:
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
            
