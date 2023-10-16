class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex+1
        dp=[]
        for i in range(1,n+1):
            dp.append([0]*i)
        for i in range(0,n):
            for j in range(0,i+1):
                if(j==0 or j==i):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex]