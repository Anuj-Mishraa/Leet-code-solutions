class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        start = 0
        end = n - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            elif s[start] < s[end]:
                s[end] = s[start]
                start += 1
                end -= 1
            else:
                s[start] = s[end]
                start += 1
                end -= 1

        return ''.join(s)
