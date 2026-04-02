class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = {}
        for i in numbers:
            num[i] = target - i

        for i in numbers:
            if i in num.values() and numbers.index(i) < numbers.index(target-i) and numbers.index(i) != numbers.index(target-i):
                return [numbers.index(i)+1, numbers.index(target-i)+1]
        