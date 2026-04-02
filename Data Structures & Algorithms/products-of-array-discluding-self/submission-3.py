class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from operator import mul
        from functools import reduce
        output = [1] * len(nums)
        for i in range(len(nums)):
                output[i] *= reduce(mul, nums[:i]+nums[i+1:]) 

        return output
