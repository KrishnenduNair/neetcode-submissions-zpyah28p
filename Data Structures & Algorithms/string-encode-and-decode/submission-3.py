class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            for j in range(i, len(s)):
                if s[j] == '#':
                    break
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        return res



