class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = [(p, s) for p, s in zip(position, speed)]
        car_speed.sort(reverse=True)
        stack = list()
        stack.append(car_speed[0])
        for pos, speed in car_speed:
            if (target-pos)/speed > (target - stack[-1][0])/stack[-1][1]:
                stack.append((pos, speed))
        
        return len(stack)