class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = ''
        for i in range(len(s1)):
            isThere = True
            s = s1[0:i] + s1[i:]
            if s not in s2:
                isThere = False
        return isThere