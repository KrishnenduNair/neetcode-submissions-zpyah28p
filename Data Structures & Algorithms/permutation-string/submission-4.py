class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = s1
        isThere = []
        for i in range(len(s1)):
            s = s[-i:] + s[:-i]
            print(s)
            if s not in s2:
                isThere.append(False)
            else:
                isThere.append(True)
        return (True in isThere)