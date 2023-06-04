class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        i = 0

        while i < len(asteroids) and asteroids[i] < 0:
            ans.append(asteroids[i])
            i += 1

        while i < len(asteroids):
            if asteroids[i] < 0:
                while ans and ans[-1] > 0:
                    if ans[-1] < -asteroids[i]:
                        ans.pop()
                    elif ans[-1] == -asteroids[i]:
                        ans.pop()
                        break
                    else:
                        break
                else:
                    ans.append(asteroids[i])
            else:
                ans.append(asteroids[i])
            i += 1
        return ans