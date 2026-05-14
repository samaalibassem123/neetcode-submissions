class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [0]
        cars = sorted(list(zip(position, speed)))
        for i in range(len(cars)-1, -1, -1):
            to_take = target - cars[i][0]
            n_time = to_take / cars[i][1]
            if n_time > stack[-1] :
                print(n_time)
                stack.append(n_time)
 
        return len(stack)-1