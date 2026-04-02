from typing import List  

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        time_taken = []
        for p, s in pair:
            if not time_taken or (target - p) / s > time_taken[-1]:
                time_taken.append((target - p) / s)
        
        return len(time_taken)  


