class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        if len(nums) == len(num):
            return False
        else:
            return True