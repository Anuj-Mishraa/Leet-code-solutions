class Solution:
    def maxEnvelopes(self, env: List[List[int]]) -> int:
        env.sort(key = lambda x:(x[0],-x[1]))
        dp = []
        for _,j in env:
            idx = self.find(dp,j)
            if idx<len(dp):
                dp[idx]=j
            else:
                dp.append(j)
        return len(dp)
    def find(self,arr, x):
        hi = len(arr)
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < x:
                lo = mid+1
            else:
                hi = mid
        return lo
