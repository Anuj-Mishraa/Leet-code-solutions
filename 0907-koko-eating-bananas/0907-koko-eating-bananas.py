import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.can_eat_all(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1
        return hi
    def can_eat_all(self,piles, k, h):
        total_time = sum(math.ceil(pile/k) for pile in piles)
        return total_time <= h
