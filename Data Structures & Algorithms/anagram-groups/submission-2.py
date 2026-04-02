class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            sort = tuple(sorted(word))
            if sort in anagram:
                anagram[sort].append(word)
            else:
                anagram.setdefault(sort, [word])

        return list(anagram.values())
 