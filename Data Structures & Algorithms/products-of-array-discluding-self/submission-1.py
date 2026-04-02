class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for ind1, i in enumerate(nums):
            prod = 1
            for ind2, j in enumerate(nums):
                if ind1 == ind2:
                    continue
                prod *= j
            output.append(prod)

        return output
