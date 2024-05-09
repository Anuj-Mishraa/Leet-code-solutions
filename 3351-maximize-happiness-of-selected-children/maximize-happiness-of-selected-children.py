class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        return sum(max(0, x - i) for i, x in enumerate(sorted(h, reverse=True)[:k]))