class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf =1, 1 
        n = len(nums)
        output = [1] * n
        for i in range(n):
            output[i] *= pre
            pre *= nums[i]

        for i in range(n-1, -1, -1):
            output[i] *= suf
            suf *= nums[i]

        return output
