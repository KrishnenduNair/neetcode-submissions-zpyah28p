class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for (key, val) in enumerate(nums):
            if (target - val) in nums_dict:
                return [nums_dict[target-val], key]
            else:
                nums_dict[val] = key

            
    
        