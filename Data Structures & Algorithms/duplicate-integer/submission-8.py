class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj = set()
        for num in nums:
            if num in obj:
                return True
            else:
                obj.add(num)
        return False
         