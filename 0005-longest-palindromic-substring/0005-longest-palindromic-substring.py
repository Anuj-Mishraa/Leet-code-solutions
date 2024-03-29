class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for j in range(n)] for i in range(n)]
        start = 0
        max_len = 1
        
        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        
        # Check for palindromes of length 3 and above
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k
        
        return s[start:start+max_len]
            