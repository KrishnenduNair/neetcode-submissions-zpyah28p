class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        import array as arr
        store = arr.array('i', [0]*26)

        for i in range(len(s)):
            store[ord(s[i])-ord('a')] += 1
            store[ord(t[i])-ord('a')] -= 1
            
        return all(count == 0 for count in store)
        
        
        