from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = defaultdict(int)
        ans = []

        for i in nums:
                topk[i] += 1
              
        for num, cnt in topk.items():
            heapq.heappush(ans, (cnt, num))
            if len(ans) > k:
                heapq.heappop(ans)
                
        return [num for cnt, num in ans]  
               
    




