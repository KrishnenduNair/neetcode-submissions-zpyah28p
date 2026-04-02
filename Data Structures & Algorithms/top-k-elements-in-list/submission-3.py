class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = {}
        res = []
        for n in nums:
            if n in num:
                num[n] +=1
            else:
                num[n] = 1

        while k != 0:
            max_key = max(num, key = num.get)
            res.append(max_key)
            num.pop(max_key)
            k -= 1

        return res