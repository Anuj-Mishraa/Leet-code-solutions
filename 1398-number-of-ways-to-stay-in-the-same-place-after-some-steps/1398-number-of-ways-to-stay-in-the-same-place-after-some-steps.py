from collections import defaultdict 
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def dfs(step,idx):
            if idx-0>step:
                return 0
            if idx >= arrLen or idx<0:
                return 0
            if step==0:
                if idx==0:
                    return 1
                else:
                    return 0
            if (step,idx) in cache:
                return cache[step,idx]
            temp = 0
            temp += dfs(step-1,idx-1)
            temp += dfs(step-1,idx)
            temp += dfs(step-1,idx+1)
            cache[step,idx] = temp%MOD
            return cache[step,idx]
        MOD = (10**9) + 7
        cache = defaultdict()
        return dfs(steps,0)