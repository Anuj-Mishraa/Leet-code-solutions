class Solution:
    def jobScheduling(self, st: List[int], en: List[int], p: List[int]) -> int:
        n = len(st)
        jobs = sorted(zip(st,en,p), key=lambda x: x[1])
        en.sort()
        n = len(jobs)
        dp = [0]*n
        dp[0] = jobs[0][2]
        for i in range(1,n):
            cur_st,_,cur_p = jobs[i]
            idx = self.latest_end(en,cur_st)-1
            if idx>=0:
                cur_p += dp[idx]
            dp[i] = max(cur_p,dp[i-1])
        return dp[-1]
    def latest_end(self,arr, x):
        hi = len(arr)
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > x:
                hi = mid
            else:
                lo = mid + 1
        return lo