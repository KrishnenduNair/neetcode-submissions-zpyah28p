class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count, max_count = 1, 0
        for n in nums:
            if n-1 not in nums:
                curr = n
                count = 1

                while curr+1 in nums:
                    curr += 1
                    count += 1

                max_count = max(max_count, count)
        
        return max_count