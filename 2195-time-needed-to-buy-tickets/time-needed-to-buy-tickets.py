class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        n=len(t)
        x=t[k]
        time=sum(min(y,x) for y in t[:k+1])
        time+=sum(min(y, x-1) for y in t[k+1:])
        return time