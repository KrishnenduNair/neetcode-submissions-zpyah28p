class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for ind, val in enumerate(nums):
            if val > 0:
                break

            if ind > 0 and val == nums[ind-1]:
                continue

            l, r = ind+1, len(nums)-1
            while l < r:
                sum3 = val + nums[l] + nums[r]
                if sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
