class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}        
        for key, val in enumerate(nums):
            if (target - val) in num:
                return [num[target-val], key]
            else:
                num[val] = key
        