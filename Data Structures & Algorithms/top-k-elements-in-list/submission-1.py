class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for val in nums:
            dict1[val] = dict1.get(val, 0) + 1

        sorted_dict = sorted(dict1.items(), key = lambda x:x[1], reverse=True)
        result = [item[0] for item in sorted_dict[:k]]
        return result