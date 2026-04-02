class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        l, r = 1, 1

        for i in range(len(nums)):
            prod[i] = l
            l *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            prod[i] *= r
            r *= nums[i]

        return prod