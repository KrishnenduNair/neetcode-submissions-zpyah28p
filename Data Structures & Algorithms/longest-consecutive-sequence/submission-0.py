class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for n in nset:
            if n-1 not in nset:
                cnt = 1
                curr = n

                while curr+1 in nset:
                    curr += 1
                    cnt += 1

                longest = max(longest, cnt)
        
        return longest

