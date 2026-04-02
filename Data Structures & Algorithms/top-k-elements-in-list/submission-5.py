from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = defaultdict(int)
        ans = []

        for i in nums:
                topk[i] += 1

        sorted_items = sorted(topk.items(), key=lambda item: item[1], reverse=True)
    
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans
         
    




