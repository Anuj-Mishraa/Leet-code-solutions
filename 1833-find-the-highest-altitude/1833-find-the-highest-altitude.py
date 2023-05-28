class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        a = 0
        for i in gain:
            a = a+i
            ans.append(a)
        return max(ans)