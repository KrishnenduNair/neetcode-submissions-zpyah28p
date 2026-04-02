class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count, max_count = 1, 0
        if len(nums) <= 1:
            count = len(nums)
            return count
            
        for i in range(1, len(nums)):    
            if nums[i] - nums[i-1] == 1:
                count += 1
            max_count = max(count, max_count)
            if nums[i] - nums[i-1] != 1:
                count = 1

        return max_count