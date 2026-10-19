class Solution:
    
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0: #condition of collision
                if stack[-1] > abs(asteroids[i]):
                    asteroids[i] = float('inf')  #if left moving asteroid is exploded, we mark it as inf to break out of while loop
                elif stack[-1] == abs(asteroids[i]): #both gets exploded if same size
                    asteroids[i] = float('inf')
                    stack.pop()
                else: #if stack[-1] < asteroids[i] then stack[-1] explodes
                    stack.pop()
            if asteroids[i] != float('inf'):
                stack.append(asteroids[i])
        return stack