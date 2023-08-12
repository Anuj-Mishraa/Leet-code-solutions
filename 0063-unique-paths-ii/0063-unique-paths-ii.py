class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        def dfs(i, j, dp, grid):
            if i < 0 or j < 0 or grid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i-1, j, dp, grid) + dfs(i, j-1, dp, grid)
            return dp[i][j]
        
        m, n = len(Grid), len(Grid[0])
        if Grid[0][0] == 1 or Grid[m-1][n-1] == 1:
            return 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        return dfs(m-1, n-1, dp, Grid)
