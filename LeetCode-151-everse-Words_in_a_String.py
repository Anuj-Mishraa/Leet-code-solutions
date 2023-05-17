class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        ans = " ".join(a[::-1])
        return ans
