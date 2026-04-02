class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        for i in cars:
            time = (target - i[0])/ i[1]
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
        
        return len(stack)
            