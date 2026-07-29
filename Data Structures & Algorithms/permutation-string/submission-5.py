class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for i in range(len(s2)):
            if s1 == s2[left:left+len(s1)]:
                return True
            left += 1

        return False 