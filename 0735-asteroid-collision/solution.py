class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(asteroids)):

            if asteroids[i] > 0:
                stack.append(asteroids[i])
            
            else:
                while stack and stack[-1] > 0 and abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                
                if stack and stack[-1] > 0 and abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                elif stack and stack[-1] > 0:
                    continue
                else:
                    stack.append(asteroids[i])
        
        return stack
