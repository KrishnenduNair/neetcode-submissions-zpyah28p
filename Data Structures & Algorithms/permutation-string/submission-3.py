class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = ''
        isThere = []
        for i in range(len(s1)):
            s = s1[-i:] + s1[:-i]
            print(s)
            if s not in s2:
                isThere.append(False)
            else:
                isThere.append(True)
        return (True in isThere)