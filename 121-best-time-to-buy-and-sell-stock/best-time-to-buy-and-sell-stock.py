class Solution:
    def maxProfit(self, p: List[int]) -> int:
        i = 0
        j = len(p)-1
        mx = 0
        mn = float("inf")
        ans = 0
        for i in range(len(p)):
            ans = max(ans,p[i]-mn)
            mn = min(p[i],mn)
        return ans
